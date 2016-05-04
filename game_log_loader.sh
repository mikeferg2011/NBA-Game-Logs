#!/usr/bin/env bash
cd /c/Users/Micha/Desktop/NBA_python/NBA-Game-Logs/All_Game_Logs
for f in *.csv; do
	winpty mysql -h 127.0.0.1 -u root -pferg -e "USE nba; LOAD DATA LOCAL INFILE '"$f"'INTO TABLE game_logs FIELDS TERMINATED BY ',' LINES TERMINATED BY '\n' IGNORE 1 LINES;"
done