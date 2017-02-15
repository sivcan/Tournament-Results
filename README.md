# Tournament Results

- Project 4  under the Full Stack Web Developer Nanodegree at Udacity

### Details
- This is a SWISS-Pairings game that keeps track of players and matches in a game tournament.
- The goal of the Swiss pairings system is to pair each player with an opponent who has won the same number of matches, or as close as possible.

### Technical Specifications
- It uses PostgreSQL database.
- Backend based on python. 

###How to use this project
- Download / Clone this project to your machine.
- Use vagrant to run PostgreSQL on your machine or directly run it if you've it pre-installed.
- Configure your database settings in the file "tournament.py" for example :
```
    psycopg2.connect(database="tournament", user="postgres", password="sivcan", host="localhost", port=5432)    
```
- Run command : 
```shell
    $ psql -f tournament.sql -U enter_your_username
```
- Run the tests on the database with the command : 
```shell
    $ python tournament_test.py
```
- Enjoy


### Project Guideline 
- Visit this link to find the guideline for this project : https://docs.google.com/document/d/16IgOm4XprTaKxAa8w02y028oBECOoB1EI1ReddADEeY/pub?embedded=true

### Success : All Testcases Passed 

![test-case-screenshot](https://github.com/sivcan/Tournament-Results/blob/master/images/result.png)

