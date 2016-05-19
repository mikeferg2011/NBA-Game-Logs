| Field           | Type         | Null | Key | Default | Extra |
|-----------------|--------------|------|-----|---------|-------|
| SEASON_ID       | int(11)      | NO   | PRI | NULL    |       |
| Player_ID       | int(11)      | NO   | PRI | NULL    |       |
| Game_ID         | int(11)      | NO   | PRI | NULL    |       |
| GAME_DATE       | date         | YES  |     | NULL    |       |
| MATCHUP         | varchar(20)  | YES  |     | NULL    |       |
| WL              | char(1)      | YES  |     | NULL    |       |
| MINUTES         | int(11)      | YES  |     | NULL    |       |
| FGM             | int(11)      | YES  |     | NULL    |       |
| FGA             | int(11)      | YES  |     | NULL    |       |
| FG_PCT          | decimal(5,4) | YES  |     | NULL    |       |
| FG3M            | int(11)      | YES  |     | NULL    |       |
| FG3A            | int(11)      | YES  |     | NULL    |       |
| FG3_PCT         | decimal(5,4) | YES  |     | NULL    |       |
| FTM             | int(11)      | YES  |     | NULL    |       |
| FTA             | int(11)      | YES  |     | NULL    |       |
| FT_PCT          | decimal(5,4) | YES  |     | NULL    |       |
| OREB            | int(11)      | YES  |     | NULL    |       |
| DREB            | int(11)      | YES  |     | NULL    |       |
| REB             | int(11)      | YES  |     | NULL    |       |
| AST             | int(11)      | YES  |     | NULL    |       |
| STL             | int(11)      | YES  |     | NULL    |       |
| BLK             | int(11)      | YES  |     | NULL    |       |
| TOV             | int(11)      | YES  |     | NULL    |       |
| PF              | int(11)      | YES  |     | NULL    |       |
| PTS             | int(11)      | YES  |     | NULL    |       |
| PLUS_MINUS      | int(11)      | YES  |     | NULL    |       |
| VIDEO_AVAILABLE | tinyint(4)   | YES  |     | NULL    |       |

| Field                    | Type        | Null | Key | Default | Extra |
|--------------------------|-------------|------|-----|---------|-------|
| PERSON_ID                | int(11)     | NO   | PRI | NULL    |       |
| DISPLAY_LAST_COMMA_FIRST | varchar(40) | YES  |     | NULL    |       |
| DISPLAY_FIRST_LAST       | varchar(40) | YES  |     | NULL    |       |
| ROSTERSTATUS             | int(11)     | YES  |     | NULL    |       |
| FROM_YEAR                | int(11)     | YES  |     | NULL    |       |
| TO_YEAR                  | int(11)     | YES  |     | NULL    |       |
| PLAYERCODE               | varchar(50) | YES  |     | NULL    |       |
| TEAM_ID                  | int(11)     | YES  |     | NULL    |       |
| TEAM_CITY                | varchar(20) | YES  |     | NULL    |       |
| TEAM_NAME                | varchar(20) | YES  |     | NULL    |       |
| TEAM_ABBREVIATION        | varchar(10) | YES  |     | NULL    |       |
| TEAM_CODE                | varchar(20) | YES  |     | NULL    |       |
| GAMES_PLAYED_FLAG        | char(1)     | YES  |     | NULL    |       |
