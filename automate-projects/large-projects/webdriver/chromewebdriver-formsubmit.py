from selenium import webdriver
browser = webdriver.Firefox()

loginURL = 'https://funneleyes.com'
dashboardURL = 'https://funneleyes.com/dashboard'
projectURL = 'https://funneleyes.com/projects?status=active'

browser.get(loginURL)
loginChecker = browser.find_element_by_css_selector('.front.not-logged-in')

if loginChecker != '':

	emailElem = browser.find_element_by_id('edit-name')
	emailElem.send_keys('Josh')
	passwordElem = browser.find_element_by_id('edit-pass')
	passwordElem.send_keys('prime') 
	passwordElem.submit()

	browser.get(projectURL)
	browser.find_element_by_id('select2-drop')