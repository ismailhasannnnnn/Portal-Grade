import selenium
from selenium import webdriver
import os
import time
from selenium.webdriver.common.keys import Keys


id = raw_input('Please input your ID number: ')
loginPass = raw_input("And your password: ")
clear = lambda: os.system('cls')
os.system("cls")
print("Please wait....")

chromedriver = 'C:\\chromedriver.exe'
browser = webdriver.Chrome(chromedriver)
browser.get("https://q.gusd.net/production/studentportal")


username = browser.find_element_by_id('Pin')
username.send_keys(id)

password = browser.find_element_by_id('Password')
password.send_keys(loginPass)

login = browser.find_element_by_id('LoginButton')
login.click()

time.sleep(2)

td = browser.find_element_by_class_name('sturow')
td.click()

time.sleep(2)

period1 = browser.find_element_by_id('tblassign_1')