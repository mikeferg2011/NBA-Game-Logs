-- create table for team level game stats

create table nba.team_game_box as
select concat(right(season_id,4),'-',right(right(season_id,4)+1,2)) as Season
	, Season_ID
	, GAME_ID
	, GAME_DATE
	, left(matchup,3) as Team
    , right(matchup,3) as Opp
    , case when matchup like '%vs%' then 'H' when matchup like '%@%' then 'A' else 'Other' end as Home_Away
	, WL
	, sum(FGM) as FGM 
	, sum(FGA) as FGA
	, sum(FGM)/sum(FGA) as FG_PCT
	, sum(FG3M) as FG3M
	, sum(FG3A) as FG3A
	, sum(FG3M)/sum(FG3A) as FG3_PCT
 	, sum(FTM) as FTM
	, sum(FTA) as FTA
	, sum(FTM)/sum(FTA) as FT_PCT
	, sum(OREB) as OREB
	, sum(DREB) as DREB
	, sum(REB) as REB
	, sum(AST) as AST
	, sum(STL) as STL
	, sum(BLK) as BLK
	, sum(TOV) as TOV
	, sum(PF) as PF
	, sum(PTS) as PTS
from nba.game_logs_raw
group by 1,2,3,4,5,6,7,8;