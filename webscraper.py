from os import write
import re
reg = re.compile("\d*-\d*-\d*-\d*-\d*")
output_lst = []
matches = []
textfile = open("lotterylist.txt", "w")
fivedigits=open("fivelist.txt", "w")
from selenium import webdriver
url = 'https://lottery.com/previous-results/mi/megamillions/2021/'
browser = webdriver.Chrome()
browser.get(url)
for tr in browser.find_elements_by_xpath('/html/body/main/section/div/div/table/tbody') :
    tds = tr.find_elements_by_tag_name('tr')
output_lst = [tr.text for tr in tds]

for element in output_lst:    
    textfile.write(element + "\n")
textfile.close
textfile = open("lotterylist.txt",'r')
for line in textfile:
  reg.findall(line).
  fivedigits.write(s + "\n")

