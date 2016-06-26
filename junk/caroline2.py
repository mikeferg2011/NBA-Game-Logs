# for selenium webdriver you need to download chrome webdriver (https://sites.google.com/a/chromium.org/chromedriver/downloads) if that is your default browser (firefox works fine if default)
import requests
import pandas as pd
import time
from selenium import webdriver


#get PERSONID and PLAYERCODE
all_players = pd.read_csv('C:/Users/Micha/Desktop/NBA_python/NBA-Game-Logs/all_time_players.csv')
players = all_players[['PERSON_ID','PLAYERCODE']]
print players

for row in players.iterrows():
	PlayerID = row[1][0]
	PlayerCode = row[1][1]
	print 'Starting %s'%(PlayerCode)
	LeagueID = '00'
	#PlayerID
	Season = 'ALL' # ALL for career game logs
	SeasonType = 'Regular+Season'
	url = 'http://stats.nba.com/stats/playergamelog?LeagueID=%s&PlayerID=%s&Season=%s&SeasonType=%s'%(LeagueID,PlayerID,Season,SeasonType)
	print url
	driver = webdriver.Chrome('C:/Users/Micha/Downloads/chromedriver_win32/chromedriver.exe')
	driver.get(url)
	# try to put a 1-2 second delay to fully assure that the page has loaded
	time.sleep(1)
	# look into writing a loop to retry for that stupid "No JSON object could be decoded" error
	# add the where response.status code == 200 to continue if not reload
	response = requests.get(url)
	x=1
	print response.status_code, x
	while response.status_code != 200:
		x=x+1
		time.sleep(1)
		#driver.close()
		driver.get(url)
		response = requests.get(url)
		print response.status_code, x
	#time.sleep(3)
	headers = response.json()['resultSets'][0]['headers']
	stats = response.json()['resultSets'][0]['rowSet']
	game_logs = pd.DataFrame(stats, columns = headers)
	#game_logs = pd.DataFrame(stats)
	game_logs.to_csv('C:/Users/Micha/Desktop/NBA_python/NBA-Game-Logs/All_Game_Logs/%s_games.csv'%(PlayerCode), index = False)
	print 'Completed %s'%(PlayerCode)
	del response
	driver.close()

