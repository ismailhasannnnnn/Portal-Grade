import selenium
from selenium import webdriver
import os
import time
import csv
from selenium.webdriver.common.keys import Keys
from tabula import read_pdf


id = input('Please input your ID number: ')
loginPass = input("And your password: ")
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

period1 = browser.find_element_by_xpath("//*[@id='tblassign_1']/tbody")
# for tr in period1.find_elements_by_tag_name('tr'):
#     with open("output.csv", "wb") as csvFile:
#         w = csv.writer(csvFile, dialect='excel')
#         w
periodOneElements = []

for tr in period1.find_elements_by_tag_name('tr'):
    periodOneElements.append(tr.text)


with open("output.csv", 'w') as resultFile:
    writer = csv.writer(resultFile, dialect='excel', delimiter=' ')
    writer.writerows(periodOneElements)




