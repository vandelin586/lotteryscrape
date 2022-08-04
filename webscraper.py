# Python program to demonstrate
# selenium
 
# import webdriver
from selenium import webdriver
 
# create webdriver object
driver = webdriver.Firefox()
 
# enter keyword to search
keyword = "geeksforgeeks"
 
# get geeksforgeeks.org
driver.get("https://www.geeksforgeeks.org/")
 
# get element
element = driver.find_element_by_xpath("//form[input/@name ='search']")
 
# print complete element
print(element)