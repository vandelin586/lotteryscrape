#! C:\Users\vande\AppData\Local\Programs\Python\Python38
#ouput_lst = This is a list of the element(Table body) found on the website that contains the line with lottery numbers listed on it.
#allnum = All Mega Millions lottery number from start of year
#powerfile = The Powerball number since beginning of year
#Element2 = the search for the lottery numbers posted on Website
#there are five whiteballs; there are one mega ball

import re 
from typing import Type
from selenium import webdriver

output_lst = []
allnum = open("allnums.txt", "a")
whiteball = open("fivelist.txt", "a")
megaball = open("powerlist.txt", "a")
url = 'https://lottery.com/previous-results/mi/megamillions/2021/','https://lottery.com/previous-results/mi/megamillions/2020/','https://lottery.com/previous-results/mi/megamillions/2019/','https://lottery.com/previous-results/mi/megamillions/2018/','https://lottery.com/previous-results/mi/megamillions/2017/'


def urlfunc (echurl):     
    for x in echurl:
        print(x)      
        browser = webdriver.Chrome()
        browser.get(x)
        for tr in browser.find_elements("by.xpath",'/html/body/main/section/div/div/table/tbody'):
            tds = tr.driver.find_elements("by.tag_name",'tr')
            output_lst = [tr.text for tr in tds]
            browser.quit

            for element in output_lst:
                element2 = re.search("((\d*)-(\d*)-(\d*)-(\d*)-(\d*)-(\d*))",element) 
                allnum.write(element2.group() + "\n")
                megaball.write(element2.group (7) + "\n")
                whiteball.write(element2.group(2) + "\n" + element2.group(3) + "\n" + element2.group(4) + "\n" + element2.group(5) + "\n" + element2.group(6) + "\n")
    
urlfunc (url)