#ouput_lst = This is a list of the element(Table body) found on the website that contains the line with lottery numbers listed on it.
#allnum = All Mega Millions lottery number from start of year
#powerfile = The Powerball number since beginning of year
#Element2 = the search for the lottery numbers posted on Website
#test

import re 
from typing import Type
from selenium import webdriver

output_lst = []
textfile = open("lotterylist.txt", "a")
fivefile = open("fivelist.txt", "a")
powerfile = open("powerlist.txt", "a")
allnum = open("allnums.txt", "a")   

def urlfunc (echurl):     
    for x in echurl:       
        browser = webdriver.Chrome()
    browser.get(x)
    for tr in browser.find_elements_by_xpath('/html/body/main/section/div/div/table/tbody') :
        tds = tr.find_elements_by_tag_name('tr')
    output_lst = [tr.text for tr in tds]

for element in output_lst:
    element2 = re.search("((\d*)-(\d*)-(\d*)-(\d*)-(\d*)-(\d*))",element) 
    allnum.write(element2.group() + "\n")
    powerfile.write(element2.group (7) + "\n")
    fivefile.write(element2.group(2) + "\n" + element2.group(3) + "\n" + element2.group(4) + "\n" + element2.group(5) + "\n" + element2.group(6) + "\n")
    url = ['https://lottery.com/previous-results/mi/megamillions/2021/','https://lottery.com/previous-results/mi/megamillions/2020/']

    urlfunc(url)