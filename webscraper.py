
# Python program to demonstrate
# selenium
# # import webdriver
from importlib.resources import path
from selenium import webdriver
from selenium.webdriver.common.by import By
 
# create webdriver object
driver = webdriver.Chrome()
 
# enter keyword to search
keyword = "datetime"
 
# get geeksforgeeks.org
driver.get("https://www.lotteryusa.com/michigan/mega-millions/year")
 
# get element
#element = driver.find_element(By.XPATH, '//*[@id="main"]/div[3]/form/div[2]/div/div/div/table/tbody/tr[2]/th/time').text
element = driver.find_element(By.XPATH, '/html/body/main/div[3]/form/div[2]/div/div/div/table/tbody/tr[5]/th').accessible_name
#element = driver.find_element(By.XPATH, '//*[@id="main"]/div[3]/form/div[2]/div/div/div/table/tbody/tr[]/th/time')
#driver.find_element(By.XPATH, '//button[text()="Some text"]')
# print complete element
print(element)

#get this text //*[@id="main"]/div[3]/form/div[2]/div/div/div/table/tbody/tr[4]...
#.../(By.xpath(".//*.getText();

#driver.findElement(By.xpath("/html/body/div[1]/div[2]/div/div[2]/article/div/table/tbody/tr["+sRow+"]/td["+sCol+"]")).getText();

#/html/body/main/div[3]/form/div[2]/div/div/div/table/tbody/tr[2]/th/time

#//*[@id="main"]/div[3]/form/div[2]/div/div/div/table/tbody/tr[2]/th/time