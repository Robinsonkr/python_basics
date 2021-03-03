from selenium import webdriver
import time

browser = webdriver.Chrome(executable_path='C:/chromedriver/chromedriver')
browser.get('https://www.google.com/')
time.sleep(2)

search_input= browser.find_element_by_name('q')
search_input.send_keys('hello world')
time.sleep(2)

search_button = browser.find_element_by_css_selector('input[type="submit"]')
search_button.click()