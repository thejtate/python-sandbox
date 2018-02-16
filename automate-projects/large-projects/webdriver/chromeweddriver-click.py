from selenium import webdriver
browser = webdriver.Firefox()
browser.get('http://stackoverflow.com/questions/31064528/webdriver-how-to-find-elements-when-class-name-contains-space')
linkElem = browser.find_element_by_link_text('add a comment')

#type(linkElen)
linkElem.click()