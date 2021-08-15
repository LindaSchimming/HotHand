"""from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd

driver = webdriver.Chrome("/usr/lib/chromium-browser/chromedriver")
gamedatas = []
driver.get("https://gogriz.com/sports/mens-basketball/stats/2019-20/stanford/boxscore/4412")
content = driver.page_source
soup = BeautifulSoup(content)
firstHalf = soup.find('table', class_= 'sidearm-table play-by-play')
for a in tb.findall('td'):
	gamedata =  a.find('td' , attrs = {'class' : 'text-right hide-on-medium-down'})
	print(gamedata.text)
///for a in soup.findAll('a', href = True, attrs = {'class' : 'text-right hide-on-medium-down'}):
	gamedata = a.find('td' , attrs = {'class' : 'text-right hide-on-medium-down'}
	print(gamedata)"""
import requests
from bs4 import BeautifulSoup
import pandas as pd

gamedatas = []
SayeedPridgett = []
Kendal = []
Jared = []
Derrick = []
Timmy = []
url1 = "https://gogriz.com/sports/mens-basketball/stats/2019-20/stanford/boxscore/4412"
url2 = "https://gogriz.com/sports/mens-basketball/stats/2019-20/msu-northern/boxscore/4413#play-by-play"
url3 = "https://gogriz.com/sports/mens-basketball/stats/2019-20/arkansas/boxscore/4414"
url4 = "https://gogriz.com/sports/mens-basketball/stats/2019-20/montana-tech/boxscore/4415"
url5 = "https://gogriz.com/sports/mens-basketball/stats/2019-20/washington/boxscore/4416#play-by-play"
url6 = "https://gogriz.com/sports/mens-basketball/stats/2019-20/texas-southern/boxscore/4417"
url7 = "https://gogriz.com/sports/mens-basketball/stats/2019-20/coppin-state/boxscore/4418"
url8 = "https://gogriz.com/sports/mens-basketball/stats/2019-20/new-mexico/boxscore/4419"
url9 = "https://gogriz.com/sports/mens-basketball/stats/2019-20/north-dakota/boxscore/4420"
url10 = "https://gogriz.com/sports/mens-basketball/stats/2019-20/oregon/boxscore/4421"
url11 = "https://gogriz.com/sports/mens-basketball/stats/2019-20/omaha/boxscore/4422"
url12 = "https://gogriz.com/sports/mens-basketball/stats/2019-20/northern-arizona/boxscore/4423"
url13 = "https://gogriz.com/sports/mens-basketball/stats/2019-20/sacramento-state/boxscore/4424"
url14 = "https://gogriz.com/sports/mens-basketball/stats/2019-20/southern-utah/boxscore/4425"
url15 = "https://gogriz.com/sports/mens-basketball/stats/2019-20/northern-colorado/boxscore/4426"
url16 = "https://gogriz.com/sports/mens-basketball/stats/2019-20/eastern-washington/boxscore/4427"
url17 = "https://gogriz.com/sports/mens-basketball/stats/2019-20/portland-state/boxscore/4428"
url18 = "https://gogriz.com/sports/mens-basketball/stats/2019-20/idaho/boxscore/4429"
url19 = "https://gogriz.com/sports/mens-basketball/stats/2019-20/idaho-state/boxscore/4430"
url20 = "https://gogriz.com/sports/mens-basketball/stats/2019-20/weber-state/boxscore/4431"


def shotRecords(url):
	page = requests.get(url)
	soup = BeautifulSoup(page.content, 'html.parser')
	firstHalfdiv = soup.find('div', {'id':'period-1'})
	firstHalf = firstHalfdiv.find('table', {'class':'sidearm-table play-by-play'})
	secondHalfdiv = soup.find('div', {'id':'period-2'})
	secondHalf = secondHalfdiv.find('table', {'class':'sidearm-table play-by-play'})

	if firstHalf is not None:

		tdColumn1 = firstHalf.find_all('td',{'class':'text-right hide-on-medium-down'})
		tdColumn2 = firstHalf.find_all('td',{'class':'hide-on-medium-down'})
		tdList = tdColumn1 + tdColumn2
		listLength = len(tdList)
		for  i in  range(listLength):
			gamedatas.append(tdList[i].text)
			i += 1
	else:
		print("error empty table")
		
	if secondHalf is not None:

		td2Column1 = secondHalf.find_all('td',{'class':'text-right hide-on-medium-down'})
		td2Column2 =  secondHalf.find_all('td',{'class':'hide-on-medium-down'})
		tdList2 = td2Column1 + td2Column2
		listLength = len(tdList2)
		for  i in  range(listLength):
			gamedatas.append(tdList2[i].text)
			i += 1
	else:
		print("error empty table")
		

	for x in range(len(gamedatas)):
		if  "SAYEED"  in gamedatas[x]:
			if "MISS" in gamedatas[x]:
				SayeedPridgett.append("0")
			elif "GOOD" in gamedatas[x]:
				SayeedPridgett.append("1")
	SayeedPridgett.append("End Game")


	for x in range(len(gamedatas)):
		if  "KENDAL"  in gamedatas[x]:
			if "MISS" in gamedatas[x]:
				Kendal.append("0")
			elif "GOOD" in gamedatas[x]:
				Kendal.append("1")
	Kendal.append("End Game")
				

	for x in range(len(gamedatas)):
		if  "JARED"  in gamedatas[x]:
			if "MISS" in gamedatas[x]:
				Jared.append("0")
			elif "GOOD" in gamedatas[x]:
				Jared.append("1")
	Jared.append("End Game")			

	for x in range(len(gamedatas)):
		if  "DERRICK"  in gamedatas[x]:
			if "MISS" in gamedatas[x]:
				Derrick.append("0")
			elif "GOOD" in gamedatas[x]:
				Derrick.append("1")	
	Derrick.append("End Game")

	for x in range(len(gamedatas)):
		if  "TIMMY"  in gamedatas[x]:
			if "MISS" in gamedatas[x]:
				Timmy.append("0")
			elif "GOOD" in gamedatas[x]:
				Timmy.append("1")	
	Timmy.append("End Game")

shotRecords(url1)
shotRecords(url2)
shotRecords(url3)
shotRecords(url4)
shotRecords(url5)
shotRecords(url6)
shotRecords(url7)
shotRecords(url8)
shotRecords(url9)
shotRecords(url10)
shotRecords(url11)
shotRecords(url12)
shotRecords(url13)
shotRecords(url14)
shotRecords(url15)
shotRecords(url16)
print(" Sayeed Pridgett")	
print(" ".join(SayeedPridgett))

print("Kendal Manuel")
print(" ".join(Kendal))

print("Jared Samuelson")
print(" ".join(Jared))

print("Derrick Carter-Holl")
print(" ".join(Derrick))

print("Timmy Falls")
print(" ".join(Timmy)) 
"""
kendrick 2019-2020 season shotsmade / shots attempted 301/633 = .4755
R code test
nsim = 1000
y = rep(0,nsim)
for( i in 1:nsim){
	x = sample(1:0, replace = TRUE, prob = c(.4755,.5245))
	y[i] = x
}
y



	
	for row in firstHalf.find_all('tr'):
		gamedata =  a.find('td' , {'class' : 'text-right hide-on-medium-down'})
		print(gamedata)"""
