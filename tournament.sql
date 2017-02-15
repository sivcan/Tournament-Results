-- Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
--
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.

DROP DATABASE IF EXISTS tournament;

CREATE DATABASE tournament;

\c tournament;

-- Create table 'Players'
CREATE TABLE players(
    ID serial PRIMARY KEY,
    player_name varchar(30)
);


-- Create table 'Matches'
CREATE TABLE matches(
    winner integer references players(ID),
    loser integer references players(ID),
    PRIMARY KEY (winner, loser)
);

-- Create a view that gives the total for table 
CREATE OR REPLACE VIEW GAMES_VIEW AS
SELECT players.ID, COUNT(matches.*) AS games
FROM players LEFT JOIN matches
ON players.ID = matches.winner 
OR players.ID = matches.loser
GROUP BY players.id;

