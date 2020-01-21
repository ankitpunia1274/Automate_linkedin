from selenium import webdriver

browser = webdriver.Chrome('/home/ankit/This PC/python/Automate Linkedin/chromedriver')
browser.get('https://in.linkedin.com/')
browser.maximize_window()  # maximize the browser window

browser.find_element_by_class_name("nav__button-secondary").click()

browser.find_element_by_id("username").send_keys('Username@')  # sends Username
browser.find_element_by_id("password").send_keys('Password')  # sends password
browser.find_element_by_class_name("btn__primary--large").click()  # click on login button
browser.implicitly_wait(10)  # it waits until elemant not found
browser.find_element_by_class_name("share-box__open").click()
browser.find_element_by_class_name("mentions-texteditor__content").send_keys("Any content you wants")  # send contents
browser.find_element_by_class_name("share-actions__primary-action").click()  # click on post button

browser.close()

# we have 3 type of waits implicit,Explicit and Fluent Wait
