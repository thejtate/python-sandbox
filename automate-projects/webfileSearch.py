import bs4, lxml
exampleFile = open('index.html')
exampleSoup = bs4.BeautifulSoup(exampleFile, "lxml")
elems = exampleSoup.select('div')
print(type(elems)) 
print(len(elems))