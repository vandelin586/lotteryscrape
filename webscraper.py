#ouput_lst = This is a list of the element(Table body) found on the website that contains the line with lottery numbers listed on it.
#allnum = All Mega Millions lottery number from start of year
#powerfile = The Powerball number since beginning of year
#Element2 = the search for the lottery numbers posted on Website
#test

import re
output_lst = []
textfile = open("lotterylist.txt", "w")
fivefile = open("fivelist.txt", "w")
powerfile = open("powerlist.txt", "w")
allnum = open("allnums.txt", "w")
class extractall:
    
    from typing import Type
from selenium import webdriver
url = 'https://lottery.com/previous-results/mi/megamillions/2021/'
browser = webdriver.Chrome()
browser.get(url)
for tr in browser.find_elements_by_xpath('/html/body/main/section/div/div/table/tbody') :
    tds = tr.find_elements_by_tag_name('tr')
output_lst = [tr.text for tr in tds] 

for element in output_lst:
    element2 = re.search("((\d*-\d*-\d*-\d*-\d*)-(\d*))",element) 
    allnum.write(element2.group() + "\n")
    powerfile.write(element2.group(3) + "\n")

    for elementfive in element:        
        fivefile.write(element2.group(2) + "\n")