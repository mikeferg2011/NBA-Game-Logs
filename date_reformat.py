#convert datetime format "APR 13, 2016" -> 2016-04-13
import pandas as pd
import datetime
import os

for filename in os.listdir('C:/Users/Micha/Desktop/NBA_python/NBA-Game-Logs/All_Game_Logs/'):
	print filename
	path = 'C:/Users/Micha/Desktop/NBA_python/NBA-Game-Logs/All_Game_Logs/%s'%filename
	data = pd.read_csv(path)
	for i in range(len(data['GAME_DATE'])):
		data['GAME_DATE'][i] = datetime.datetime.strptime(data['GAME_DATE'][i], '%b %d, %Y').strftime('%Y-%m-%d')
	data.to_csv(path, index = False)

# data = pd.read_csv('C:/Users/Micha/Desktop/NBA_python/NBA-Game-Logs/HISTADD_larry_bird_games.csv')
# print datetime.datetime.strptime(data['GAME_DATE'][0], '%b %d, %Y').strftime('%Y-%m-%d')
# #for index, row in data.iterrows():
# print len(data['GAME_DATE'])
# for i in range(len(data['GAME_DATE'])):
	# data['GAME_DATE'][i] = datetime.datetime.strptime(data['GAME_DATE'][i], '%b %d, %Y').strftime('%Y-%m-%d')
# data.to_csv('C:/Users/Micha/Desktop/NBA_python/NBA-Game-Logs/HISTADD_larry_bird_games.csv', index = False)