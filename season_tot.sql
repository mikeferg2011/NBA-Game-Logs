--consider putting names in the season table and adjusted game_logs to improve effeciency
create table nba.season_totals as
select SEASON_ID,
	Player_ID,
	count(Game_ID) as GP,
	sum(MINUTES) as MINUTES,
	sum(FGM) as FGM,
	sum(FGA) as FGA,
	sum(FGM)/sum(FGA) as FG_PCT,
	sum(FG3M) as FG3M,
	sum(FG3A) as FG3A,
	sum(FG3M)/sum(FG3A) as FG3_PCT,
	sum(FTM) as FTM,
	sum(FTA) as FTA,
	sum(FTM)/sum(FTA) as FT_PCT,
	sum(OREB) as OREB,
	sum(DREB) as DREB,
	sum(REB) as REB,
	sum(AST) as AST,
	sum(STL) as STL,
	sum(BLK) as BLK,
	sum(TOV) as TOV,
	sum(PF) as PF,
	sum(PTS) as PTS,
	sum(PLUS_MINUS) as PLUS_MINUS
from nba.game_logs
group by SEASON_ID, Player_ID;