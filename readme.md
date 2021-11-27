# Zendesk Ticket Viewer

A python CLI ticket viewer to view Zendesk tickets and its details


## Ticket viewer does the following

* Connect to the Zendesk API using Python requests
* Request all the tickets for the account
* Display them in a tabular format
* Display individual ticket details
* Page through tickets when more than 25 tickets are returned


## Steps to use ticket viewer

* Please install pip, python3, setup tools in the OS.
* requirements.txt is included in the package to install all the requirements. 

```pip install -r requirements.txt```

* Run main.py that starts ticket viewer.

```python main.py```

## Design Decisions:

* Ticket class provides a nice abstraction to store all the tickets and its details.
* Ticket class also includes some static methods that performs generic instructions such as displaying all the tickets, storing all the tickets and fetching individual ticket by id.
* Main function is the starting point of ticket viewer and is written in an interactive manner for users to choose different options such as below:
	* View all tickets
	* View individual ticket entry
	* Quit ticket viewer
	* Ctrl+C can also be used to quit
* Display class is written in such a way that it can be used to display any list in tabular paging format and hence is reusable for any other classes and not just restricted to tickets.
* Tabular paging is also done in an interactive manner so that users can choose to navigate to previous/next page, view individual entry details by entering options specified.
* All the tickets are fetched using Zendesk tickets GET api and stored in the dictionary so that we dont have to call the api again for individual ticket entries when tickets are already fetched to view all the tickets.
* Storing in the dictionary also helps in fetching individual tickets without having to go through the entire list of tickets.
* All the functions are written with docstring that explains about the function and its params and return values.
* All the unit tests are written in the file test.py. Can be run using the following.

```python test.py```

