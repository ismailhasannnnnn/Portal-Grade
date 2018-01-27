import selenium
from selenium import webdriver
import os
import time
import csv
import tkinter as tk
from tkinter import *
from selenium.webdriver.common.keys import Keys
from tabula import read_pdf
import pandas as pd

# top = Tk()
# L1 = Label(top, text="ID Number")
# L1.pack( side = LEFT)
# E1 = Entry(top, bd =5)
# E1.pack(side = RIGHT)
#
# top.mainloop()

class Login(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.entry = tk.Entry(self)
        self.entry2 = tk.Entry(self)
        self.button = tk.Button(self, text="Get", command=self.on_button)
        self.button.pack()
        self.entry.pack()
        self.entry2.pack()

    def on_button(self):
        global id
        global loginPass
        id = self.entry.get()
        loginPass = self.entry2.get()


login = Login()
login.mainloop()

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

time.sleep(1)

td = browser.find_element_by_class_name('sturow')
td.click()

time.sleep(1)

# if(browser.find_element_by_xpath("//*[@id='chk_Assignments']").is_enabled()){
# print(browser.find_element_by_xpath("//*[@id='chk_Assignments']").is_selected())
if browser.find_element_by_xpath("//*[@id='chk_Assignments']").is_selected() == False:
    browser.find_element_by_xpath("//*[@id='chk_Assignments']").click()

time.sleep(1)

# Table 1

period1 = browser.find_element_by_xpath("//*[@id='tblassign_1']/tbody")
# for tr in period1.find_elements_by_tag_name('tr'):
#     with open("output.csv", "wb") as csvFile:
#         w = csv.writer(csvFile, dialect='excel')
#         w
periodOneElements = []

for tr in period1.find_elements_by_tag_name('td'):
    periodOneElements.append(tr.text)


with open("period 1.csv", 'w') as resultFile:
    writer = csv.writer(resultFile, dialect='excel', delimiter=' ')
    writer.writerows(periodOneElements)

time.sleep(5)

# Table 2

period2 = browser.find_element_by_xpath("//*[@id='tblassign_2']/tbody")
periodTwoElements = []

for tr in period2.find_elements_by_tag_name('td'):
    periodTwoElements.append(tr.text)

with open("period_2.csv", "w") as resultFile:
    writer = csv.writer(resultFile, dialect='excel', delimiter=' ')
    writer.writerows(periodTwoElements)

time.sleep(5)

# Table 3

period3 = browser.find_element_by_xpath("//*[@id='tblassign_3']/tbody")
periodThreeElements = []

for tr in period3.find_elements_by_tag_name('td'):
    periodTwoElements.append(tr.text)

with open("period_3.csv", "w") as resultFile:
    writer = csv.writer(resultFile, dialect='excel', delimiter=' ')
    writer.writerows(periodThreeElements)

time.sleep(5)

# Table 5

period5 = browser.find_element_by_xpath("//*[@id='tblassign_4']/tbody")
periodFiveElements = []

for tr in period5.find_elements_by_tag_name('td'):
    periodFiveElements.append(tr.text)

with open("period_5.csv", "w") as resultFile:
    writer = csv.writer(resultFile, dialect='excel', delimiter=' ')
    writer.writerows(periodFiveElements)






