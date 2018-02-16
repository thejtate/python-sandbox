import bs4, requests, sys
from selenium import webdriver
from lxml import html

from PyQt4.QtGui import *  
from PyQt4.QtCore import *  
from PyQt4.QtWebKit import *  

# URL layout: http://readcomiconline.to/Comic/Saga/Issue-1?&readType=1
headerAgent = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36'}

comicSeries = 'Saga'
issueNum = 1
listingURL = 'http://readcomiconline.to/Comic/'+comicSeries
comicURL = 'http://readcomiconline.to/Comic/'+str(comicSeries)+'/Issue-'+str(issueNum)+'?readType=1'

res = requests.get(listingURL,headers=headerAgent)
res.raise_for_status()

soup = bs4.BeautifulSoup(res.text, "lxml")
comicElement = soup.find('table', {'class':'listing'})
