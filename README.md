# Ship battle game

This is a text game made for a job interview.
It takes GET parameters with query name "ships" and converts them into a number of
ships and soldiers.
After the app is run, we get a result in a RESTApi browsable API view.

## Description

Task was to develop the battle between N ships in the middle of the ocean. The solution should
be only textual (JSON response) without any GUI - therefore the game is only textual “battle”.
Each ship can have M soldiers - N and M are set in GET parameter in following way:
```
GET …?ships=50,58,68,40
```

## Getting Started

### Dependencies
All the dependencies are listed in requirements.txt, but few notable ones are:
* Windows 11
* Python==3.11
* Django==4.1.7
* djangorestframework==3.14.0



### Executing program

* Start the Django server, and go to the localhost URL.
* Enter the query in a format:
```
localhost:8000/?ships=50,58,68,40
```
* Here number of ships would be 4 and Ship1 has 50 soldiers, Ship2 has 58 soldiers, …, and Ship4 has 40 soldiers.
* After the query is submitted, the response will be given, and the winner displayed
