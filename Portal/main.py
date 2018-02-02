import selenium
from selenium import webdriver
import os
import time
import csv
import tkinter as tk
from tkinter import *
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from tabula import read_pdf
import pandas as pd
from itertools import islice
from pathlib import Path
import pyautogui

class Login(tk.Tk):
    def __init__(self):
        global id
        global loginPass
        loginFile = Path('loginFile.txt')
        if loginFile.is_file() == False:
            f = open('loginFile.txt', "w")

        with open('loginFile.txt', "r") as file:
            id = file.readline(6)
            loginPass = ""
            for line in islice(file, 1, 2):
                loginPass = line
        tk.Tk.__init__(self)
        self.label = tk.Label(self, text="Enter Student Portal Login Details", height=5, font=("Yu Gothic Light", 16), background="#6f6f6f")
        self.entry = tk.Entry(self, background="#AFAFAF", font=("Yu Gothic Light", 12))
        self.entry.insert(0, id)
        self.entry2 = tk.Entry(self, show="#", background="#AFAFAF", font=("Yu Gothic Light", 12))
        self.entry2.insert(0, loginPass)
        self.button = tk.Button(self, text="Login", command=self.on_button, pady=0, padx=15, background="#AFAFAF", font=("Yu Gothic Light", 12))
        self.loginElements = []
        self.bind('<Return>', self.on_button)
        self.var = BooleanVar()
        self.saveSettings = tk.Checkbutton(self, text="Save Settings", variable=self.var, background="#6f6f6f", font=("Yu Gothic Light", 12), highlightcolor="#6f6f6f")
        # self.label.pack()
        # self.entry.pack()
        # self.entry2.pack()
        # self.button.pack()
        # self.saveSettings.pack()
        self.label.grid(row=0, column=0)
        self.entry.grid(row=1, column=0, pady=10)
        self.entry2.grid(row=2, column=0)
        self.button.grid(row=3, column=0, pady=10)
        self.saveSettings.grid(row=4, column=0)

    def on_button(self, event=None):
        global id
        global loginPass
        id = self.entry.get()
        loginPass = self.entry2.get()
        if self.var.get():
            loginFile = open("loginFile.txt", 'w')
            loginFile.write(id)
            loginFile.write("\n")
            loginFile.write(loginPass)
            loginFile.write("")
            loginFile.close()
        login.destroy()

    def enter_key(self):
        self.on_button()


login = Login()
login.title("Student Portal")
x = Frame(height=100, width=300, background='#6f6f6f')
# x.pack()
x.grid()
login.configure(background='#6f6f6f')
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

if browser.find_element_by_xpath('//*[@id="Assignments"]/td[2]').is_enabled() == True:
    browser.find_element_by_xpath('//*[@id="Assignments"]/td[2]').click()

time.sleep(1)

# if(browser.find_element_by_xpath("//*[@id='chk_Assignments']").is_enabled()){
# print(browser.find_element_by_xpath("//*[@id='chk_Assignments']").is_selected())
if browser.find_element_by_xpath("//*[@id='chk_Assignments']").is_selected() == False:
    browser.find_element_by_xpath("//*[@id='chk_Assignments']").click()

time.sleep(1)

printer = browser.find_element_by_xpath("//*[@id='tblassign_1']/thead/tr[2]/td/a/img")
printer.click()

time.sleep(1)

report = browser.find_element_by_xpath("//*[@id='tbltermlist']/tbody/tr[4]/td[5]")
report.click()

time.sleep(1)

for handle in browser.window_handles:
    browser.switch_to.window(handle)
print(browser.current_url)

time.sleep(1)

saveas = ActionChains(browser).key_down(Keys.CONTROL)\
         .send_keys('s').key_up(Keys.CONTROL)
saveas.perform()

time.sleep(1)

pyautogui.typewrite('period1')
time.sleep(1)
pyautogui.hotkey('f4')
pyautogui.hotkey('ctrl', 'a')
pyautogui.typewrite('Documents')
pyautogui.hotkey('return')
time.sleep(1)
pyautogui.hotkey('alt', 's')
time.sleep(1)
pyautogui.hotkey('alt', 'y')
time.sleep(3)
pyautogui.hotkey('ctrl', 'w')
pyautogui.hotkey('ctrl', 'w')
os.system('taskkill /F /IM chromedriver.exe')

# # Table 1
#
# period1 = browser.find_element_by_xpath("//*[@id='tblassign_1']/tbody")
# # for tr in period1.find_elements_by_tag_name('tr'):
# #     with open("output.csv", "wb") as csvFile:
# #         w = csv.writer(csvFile, dialect='excel')
# #         w
# periodOneElements = []
#
# for tr in period1.find_elements_by_tag_name('td'):
#     periodOneElements.append(tr.text)
#
# # no you
# with open("period_1.csv", 'w') as resultFile:
#     writer = csv.writer(resultFile, dialect='excel', delimiter=' ')
#     writer.writerows(periodOneElements)
#
# time.sleep(5)
#
# # Table 2
#
# period2 = browser.find_element_by_xpath("//*[@id='tblassign_2']/tbody")
# periodTwoElements = []
#
# for tr in period2.find_elements_by_tag_name('td'):
#     periodTwoElements.append(tr.text)
#
# with open("period_2.csv", "w") as resultFile:
#     writer = csv.writer(resultFile, dialect='excel', delimiter=' ')
#     writer.writerows(periodTwoElements)
#
# time.sleep(5)
#
# # Table 3
#
# period3 = browser.find_element_by_xpath("//*[@id='tblassign_3']/tbody")
# periodThreeElements = []
#
# for tr in period3.find_elements_by_tag_name('td'):
#     periodTwoElements.append(tr.text)
#
# with open("period_3.csv", "w") as resultFile:
#     writer = csv.writer(resultFile, dialect='excel', delimiter=' ')
#     writer.writerows(periodThreeElements)
#
# time.sleep(5)
#
# # Table 5
#
# period5 = browser.find_element_by_xpath("//*[@id='tblassign_4']/tbody")
# periodFiveElements = []
#
# for tr in period5.find_elements_by_tag_name('td'):
#     periodFiveElements.append(tr.text)
#
# with open("period_5.csv", "w") as resultFile:
#     writer = csv.writer(resultFile, dialect='excel', delimiter=' ')
#     writer.writerows(periodFiveElements)






