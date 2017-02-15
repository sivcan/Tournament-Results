#!/usr/bin/env python
# 
# tournament.py -- implementation of a Swiss-system tournament
#

import psycopg2


def connect():
    """Connect to the PostgreSQL database.  Returns a database connection."""
#    try : 
#        return 
    return psycopg2.connect(database="tournament", user="postgres", password="sivcan", host="localhost", port=5432)
  
    

def deleteMatches():
    """Remove all the match records from the database."""
    DB = connect()
    c = DB.cursor()
    c.execute("DELETE FROM matches;")
    DB.commit()
    DB.close()
    

def deletePlayers():
    """Remove all the player records from the database."""
    DB = connect()
    c = DB.cursor()
    c.execute("DELETE FROM players;")
    DB.commit()
    DB.close()

    
def countPlayers():
    """Returns the number of players currently registered."""
    DB = connect()
    c = DB.cursor()
    c.execute("SELECT COUNT(*) FROM players;")
    count_of_players = c.fetchone()[0]
    DB.commit()
    DB.close()
    return count_of_players

def registerPlayer(name):
    """Adds a player to the tournament database.
  
    The database assigns a unique serial id number for the player.  (This
    should be handled by your SQL database schema, not in your Python code.)
  
    Args:
      name: the player's full name (need not be unique).
    """
    DB = connect()
    c = DB.cursor()
    c.execute("INSERT INTO players (player_name) VALUES(%s)", (name,))
    DB.commit()
    DB.close()
    


def playerStandings():
    """Returns a list of the players and their win records, sorted by wins.

    The first entry in the list should be the player in first place, or a player
    tied for first place if there is currently a tie.

    Returns:
      A list of tuples, each of which contains (id, name, wins, matches):
        id: the player's unique id (assigned by the database)
        name: the player's full name (as registered)
        wins: the number of matches the player has won
        matches: the number of matches the player has played
    """
    DB = connect()
    c = DB.cursor()
    c.execute("""SELECT ID, player_name, COUNT(matches.winner) AS wins, 
                (SELECT games FROM GAMES_VIEW WHERE games_view.ID = players.ID)
                FROM players LEFT JOIN matches 
                ON players.ID = matches.winner
                GROUP BY players.ID, players.player_name
                ORDER BY wins DESC;
            """)
    winner_table = c.fetchall()
    DB.commit()
    DB.close()
    return winner_table

def reportMatch(winner, loser):
    """Records the outcome of a single match between two players.

    Args:
      winner:  the id number of the player who won
      loser:  the id number of the player who lost
    """
    DB = connect()
    c = DB.cursor()
    c.execute("""INSERT INTO matches (winner, loser)
            VALUES(%s, %s)""", (winner, loser))
    DB.commit()
    DB.close()
    
    
def swissPairings():
    """Returns a list of pairs of players for the next round of a match.
  
    Assuming that there are an even number of players registered, each player
    appears exactly once in the pairings.  Each player is paired with another
    player with an equal or nearly-equal win record, that is, a player adjacent
    to him or her in the standings.
  
    Returns:
      A list of tuples, each of which contains (id1, name1, id2, name2)
        id1: the first player's unique id
        name1: the first player's name
        id2: the second player's unique id
        name2: the second player's name
    """
    playerList = playerStandings()
    
    results = [] 
    for i, player in enumerate(playerList):
        if i%2 == 0:
            pair = (playerList[i][0],
                    playerList[i][1],
                    playerList[i+1][0],
                    playerList[i+1][1])
            results.append(pair)
            
    return results


