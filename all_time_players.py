import requests
import pandas as pd
from selenium import webdriver

IsOnlyCurrentSeason='0' # '0' for All-time '1' for current season
LeagueID = '00'
Season = '2015-16' # use most recent season for all time or for a particular year use season

url = 'http://stats.nba.com/stats/commonallplayers?IsOnlyCurrentSeason=%s&LeagueID=%s&Season=%s'%(IsOnlyCurrentSeason,LeagueID,Season)
print url
driver = webdriver.Chrome('C:/Users/Micha/Downloads/chromedriver_win32/chromedriver.exe')
driver.get(url)

response = requests.get(url)
response.raise_for_status()
headers = response.json()['resultSets'][0]['headers']
players = response.json()['resultSets'][0]['rowSet']
print type(players)
print type(headers)
print headers[0]
print players[0]
players = pd.DataFrame(players, columns = headers)
players.to_csv('C:/Users/Micha/Desktop/GitHub/NBA-Game-Logs/all_time_players.csv', index = False)
print players.columns
driver.close()