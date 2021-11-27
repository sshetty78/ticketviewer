# Ticket class that has functions to display individual tickets and some static functions to manage
# tickets in general.
from datetime import datetime
from tabular_display import Display


class Ticket:
	def __init__(self, ticket_info):
		"""
		Populate ticket with ticket info.
		:param ticket_info: Ticket details for a particular ticket.
		"""
		self.id = ticket_info.get("id")
		dt = datetime.strptime(ticket_info.get("created_at"), "%Y-%m-%dT%H:%M:%SZ")
		self.created_on = dt.strftime("%d %B %Y")
		self.created_at = "%s:%s:%s" % (dt.hour, dt.minute, dt.second)
		self.submitter_id = ticket_info.get("submitter_id")
		self.priority = ticket_info.get("priority")
		self.subject = ticket_info.get("subject")
		self.status = ticket_info.get("status")

	def display(self):
		"""
		Display ticket information.
		:return: None
		"""
		print("You are viewing ticket with id: %s\nDetails:" % self.id)
		print("Ticket created on %s at %s" % (self.created_on, self.created_at))
		print("Ticket submitted by: %s" % self.submitter_id)
		print("Ticket status: %s" % self.status)
		print("Ticket title: %s" % self.subject)
		print("Ticket priority: %s\n" % self.priority)

	@staticmethod
	def store_tickets(ticket_list):
		"""
		Store tickets and its details.
		:param ticket_list: List of tickets.
		:return: A tuple of ticket object dict and ticket info dict.
		"""
		ticket_obj_dict = {}
		ticket_info_dict = {}
		for ticket_info in ticket_list:
			ticket = Ticket(ticket_info)
			ticket_obj_dict[ticket.id] = ticket
			# ticket_info_list[ticket.id] = [ticket.id, "Ticket with Subject %s " % ticket.subject, "created on %s at %s " % (
			# 	ticket.created_on, ticket.created_at), "by %s" % ticket.submitter_id]
			ticket_info_dict[ticket.id] = [ticket.id, ticket.subject, ticket.created_on, ticket.created_at,
										   ticket.submitter_id]
		return ticket_obj_dict, ticket_info_dict

	@staticmethod
	def display_all_tickets(ticket_info_dict):
		"""
		Display all tickets in ticket object dictionary.
		:param ticket_info_dict: Ticket dictionary that contains mapping of ticket id to its info.
		:return:
		"""
		header_list = ["Id", "Subject", "Creation Date", "Creation Time", "Submitter id"]
		display = Display(list(ticket_info_dict.values()), header_list)
		return display.start_paging()


