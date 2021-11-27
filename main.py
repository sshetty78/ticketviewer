# Main file that starts the ticket viewer.

import consts
import requests
from ticket import Ticket

def fetch_tickets():
	"""
	Fetch tickets from the Zendesk API.
	:return: True and its response, if successful. False, otherwise.
	"""
	try:
		api_call_headers = {'Authorization': 'Bearer ' + consts.ACCESS_TOKEN}
		# response=requests.get(url, auth=HTTPBasicAuth(email,pwd))
		response = requests.get(consts.URL, headers=api_call_headers)
		response.raise_for_status()
		return True, response.json()["tickets"]
	except requests.exceptions.HTTPError as error:
		print(type(error.errno))
		if(error.response.status_code==401):
			print("Invalid authentication credentials")
			return False, []
		if(error.response.status_code==404):
			print("Resource not found. Please verify the url")
			return False, []
		print("Failed to fetch tickets! Please try again!")
		return False, []

if __name__ == '__main__':
	try:
		print("Welcome to the ticket viewer!!\n\n")
		while(True):
			print("*****Main Menu*****\nPress 1 to view all tickets\nPress 2 to view a particular ticket\nPress 3 to quit ticket viewer")
			try:
				input_num = int(input())
			except ValueError:
				print(consts.INVALID_MSG)
				continue
			if input_num not in [1, 2, 3]:
				print(consts.INVALID_MSG)
				continue
			if input_num == 3:
				break
			ret, ticket_list = fetch_tickets()
			if not ret:
				break
			ticket_obj_dict, ticket_info_dict = Ticket.store_tickets(ticket_list)
			if input_num == 1:
				ret = Ticket.display_all_tickets(ticket_info_dict)
				if ret:
					input_num = 2
			if input_num == 2:
				print("Enter ticket number\n")
				try:
					ticket_id = int(input())
				except ValueError:
					print(consts.INVALID_MSG)
					continue
				ticket = ticket_obj_dict.get(ticket_id)
				if not ticket:
					print("Ticket %d not found" % ticket_id)
					continue
				ticket.display()
	except KeyboardInterrupt:
		pass
	finally:
		print("Thanks for using the viewer! Bye!")
