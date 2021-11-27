import requests
import unittest
from main import fetch_tickets
from mock import patch, mock
from tabular_display import Display
from ticket import Ticket

class Test(unittest.TestCase):

    def setUp(cls):
        cls.expected_ticket_list = [{"test_id": ["test_id", "test_sub", "24 November 2021", "1:22:11", "test_sub_id"]}]
        cls.actual_ticket_list = [{"id": "test_id",
                                   "created_at": "2021-11-24T01:22:11Z",
                                   "submitter_id": "test_sub_id",
                                   "subject": "test_sub"}]

    @patch('builtins.print')
    def test_display(self, mock_print):
        actual_dict, actual_list = Ticket.store_tickets(self.actual_ticket_list)
        actual_dict["test_id"].display()
        mock_print.assert_any_call("You are viewing ticket with id: %s\n"
                                   " Details:" % self.actual_ticket_list[0]["id"])
        mock_print.assert_any_call("Ticket title: %s" % self.actual_ticket_list[0]["subject"])

    def test_store_tickets(self):
        actual_dict, actual_list = Ticket.store_tickets(self.actual_ticket_list)
        self.assertEqual(actual_list, self.expected_ticket_list[0])

    def test_display_all_tickets(self):
        with patch('tabular_display.Display.start_paging') as mock:
            mock.return_value = None
            ret = Ticket.display_all_tickets({})
            self.assertEqual(ret, None)

    def test_fetch_tickets(self):
        json = {"tickets": [{"title": "test_ticket", "id": "0"}]}
        # Test 1
        mock_response = mock.Mock()
        mock_response.json.return_value = json
        mock_response.status_code = 200
        with patch("requests.get") as m:
            m.return_value = mock_response
            ret, resp = fetch_tickets()
            self.assertEqual(ret, True)
            self.assertEqual(resp, json["tickets"])

       # Test 2
        mock_response.reset()
        e = requests.HTTPError('error')
        e.response = mock.MagicMock()
        e.response.status_code = 404
        mock_response.raise_for_status.side_effect = e
        with patch("requests.get") as m:
            m.return_value = mock_response
            ret, resp = fetch_tickets()
            self.assertEqual(ret, False)
            self.assertEqual(resp, [])

        # Test 3
        mock_response.reset()
        e = requests.HTTPError('error')
        e.response = mock.MagicMock()
        e.response.status_code = 401
        mock_response.raise_for_status.side_effect = e
        with patch("requests.get") as m:
            m.return_value = mock_response
            ret, resp = fetch_tickets()
            self.assertEqual(ret, False)
            self.assertEqual(resp, [])

    @patch('builtins.print')
    @patch('builtins.input')
    def test_start_paging(self, mock_input, mock_print):
        with patch("tabular_display.Display.print_single_page") as m:
            m.return_value = None
            mock_input.return_value = 4
            display = Display(range(26), [])
            display.start_paging()
            mock_print.assert_any_call("Enter 2 to navigate to the next page -->\n")
            mock_print.assert_any_call("Enter 3 to view details of an individual entry")

if __name__ == "__main__":
    unittest.main()