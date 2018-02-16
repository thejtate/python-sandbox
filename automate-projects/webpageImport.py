import requests, bs4, urllib

pullHTMlfile = urllib.urlretrieve("https://weather.com/weather/today/l/USDC0001:1:US","index.html")
exampleFile = open('index.html')
exampleSoup = bs4.BeautifulSoup(exampleFile)
type(exampleSoup)

print(exampleSoup.select('div.today_nowcard-temp'))