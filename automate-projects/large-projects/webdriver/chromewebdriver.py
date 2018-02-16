from selenium import webdriver
browser = webdriver.Chrome()
browser.get('http://inventwithpython.com')

try: 
	elem = browser.find_element_by_css_name('bookcover')
	print('Found <%s> element with that class name: '%s(elem.tag_name))
except: 
	print('Was not able to find anything.')