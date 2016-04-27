# for selenium webdriver you need to download chrome webdriver (https://sites.google.com/a/chromium.org/chromedriver/downloads) if that is your default browser (firefox works fine if default)
import requests
import pandas as pd
import time
from selenium import webdriver

#list of player names
players = ['Michael Jordan','Magic Johnson', 'Larry Bird']

#get PERSONID and PLAYERCODE
all_players = pd.read_csv('C:/Users/Micha/Desktop/GitHub/NBA-Game-Logs/all_time_players.csv')
players = all_players[all_players['DISPLAY_FIRST_LAST'].isin(players)][['PERSON_ID', 'PLAYERCODE']]
players = dict(zip(players.PERSON_ID, players.PLAYERCODE))
print players

#actually pull the data
for key, value in players.iteritems():
	x=1
	print 'Starting %s'%(value)
	LeagueID = '00'
	PlayerID = str(key)
	Season = 'ALL' # ALL for career game logs
	SeasonType = 'Regular+Season'
	url = 'http://stats.nba.com/stats/playergamelog?LeagueID=%s&PlayerID=%s&Season=%s&SeasonType=%s'%(LeagueID,PlayerID,Season,SeasonType)
	print url
	driver = webdriver.Chrome('C:/Users/Micha/Downloads/chromedriver_win32/chromedriver.exe')
	driver.get(url)
	response = requests.get(url)
	print str(response.status_code)+str(x)+'\n'+response.url
	while response.status_code != 200:
		x = x+1
		response = requests.get(url)
		print str(response.status_code)+str(x)+'\n'+response.url
		#time.sleep(0.5)
	# response.raise_for_status()
	print str(response)+'response.raise_for_status()'
	headers = response.json()['resultSets'][0]['headers']
	print headers
	stats = response.json()['resultSets'][0]['rowSet']
	game_logs = pd.DataFrame(stats, columns = headers)
	game_logs.to_csv('C:/Users/Micha/Desktop/GitHub/NBA-Game-Logs/%s_games.csv'%(value), index = False)
	print 'Completed %s'%(value)
	del response
	driver.close()
