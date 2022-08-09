
# Python program to demonstrate
# selenium
# # import webdriver
from asyncio.constants import SENDFILE_FALLBACK_READBUFFER_SIZE
from datetime import date
import datetime
from hashlib import new
from importlib.resources import path
from re import I
from tkinter import N
from typing_extensions import Self
from webbrowser import get
from xml.dom.minidom import Identified
from selenium import webdriver
from selenium.webdriver.common.by import By
 
# create webdriver object
driver = webdriver.Chrome()
 
# enter keyword to search
keyword = "datetime"
 
# get geeksforgeeks.org
driver.get("https://www.lotteryusa.com/michigan/mega-millions/year")
driver.implicitly_wait(20)
 
# get element
#element = driver.find_element(By.XPATH, '//*[@id="main"]/div[3]/form/div[2]/div/div/div/table/tbody/tr[2]/th/time').text
ldate=[]
ldate = driver.find_elements(By.XPATH, '//*[@id="main"]/div[3]/form/div[2]/div/div/div/table/tbody/tr[*]')


for i in ldate:

    #print("location" + i.location.__str__().lower)
    #print(i)
   # print(i.tag_name)
   # print(i.text)
   # print(i.__module)

    #print(i.get_attribute('innerHTML'))  
    

#elementlilist=[]
#elementlilist = driver.find_elements(By.XPATH, '//*[@class="c-result-card__header"]')
#print(elementlilist.__doc__.title)

    #print(i.get_dom_attribute)
   # print





#print(element.text)
#elementidtext = driver.find_elements(By.CLASS_NAME)
#elementid = driver.find_elements(By.XPATH, element)
##for n in elementid :
#print (elementidtext)
#print (elementid)
#element = driver.find_element(By.XPATH, '//*[@id="main"]/div[3]/form/div[2]/div/div/div/table/tbody/tr[]/th/time')
#driver.find_element(By.XPATH, '//button[text()="Some text"]')


#get this text //*[@id="main"]/div[3]/form/div[2]/div/div/div/table/tbody/tr[4]...
#.../(By.xpath(".//*.getText();
##driver.findElement(By.xpath("/html/body/div[1]/div[2]/div/div[2]/article/div/table/tbody/tr["+sRow+"]/td["+sCol+"]")).getText();