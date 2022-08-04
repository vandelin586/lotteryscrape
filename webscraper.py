
# Python program to demonstrate
# selenium
# # import webdriver
from selenium import webdriver
 
# create webdriver object
driver = webdriver.Chrome()
 
# enter keyword to search
keyword = "lottery"
 
# get geeksforgeeks.org
driver.get("https://www.lotteryusa.com/michigan/mega-millions/year")
 
# get element
element = driver.find_elements("by.xpath" '/html/body/main/div[3]/form/div[2]/div/div/div/table/tbody/tr[2]/th/time')
 
# print complete element
print(element)