# A generic display class that can display any list in the form of paging and tabulation.
import consts
from tabulate import tabulate

class Display:
    def __init__(self, display_list, header_list):
        """
        Constructor to specify tabulation list and header.
        :param display_list: List to display in the tabular format.
        :param header_list: Headers for the table.
        """
        self.display_list = display_list
        self.header = header_list

    def print_single_page(self, start, num_entries=consts.PAGE_THROUGH_NUM):
        """
        Prints single page info.
        :param start: Start of the entry
        :param num_entries: Number of entries to be displayed on the page.
        :return: None
        """
        tabulation_list = []
        end = start + num_entries
        if end > len(self.display_list):
            end = len(self.display_list)
        for element in self.display_list[start:end]:
            tabulation_list.append(element)
        print(tabulate(tabulation_list, headers=self.header, tablefmt="fancy_grid"))

    def start_paging(self, num_entries=consts.PAGE_THROUGH_NUM):
        """
        Starts paging of entries based on the num_entries mentioned.

        :param num_entries: Number of entries in a single page.
        :return: 1 for individual entry display, None otherwise.
        """
        total_length = len(self.display_list)
        start = 0
        invalid = False
        while(True):
            valid_list = [3, 4]
            self.print_single_page(start)
            if start != 0:
                print("<-- Enter 1 to navigate to the previous page")
                valid_list.append(1)
            if start + num_entries < total_length:
                print("Enter 2 to navigate to the next page -->\n")
                valid_list.append(2)
            print("Enter 3 to view details of an individual entry")
            print("Enter 4 to return to main menu")
            if invalid:
                print(consts.INVALID_MSG)
                invalid = False
            try:
              input_num = int(input())
            except ValueError:
                invalid = True
                continue
            if input_num not in valid_list:
                invalid = True
                continue
            if input_num == 1:
                start = start - num_entries
            if input_num == 2:
                start = start + num_entries
            if input_num == 3:
                return 1
            if input_num == 4:
                return
