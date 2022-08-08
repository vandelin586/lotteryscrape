

# importing the HTMLSession class
from requests_html import HTMLSession
# create the object of the session
session = HTMLSession()
# url of the page
web_page = 'https://webscraper.io/'
# making get request to the webpage
respone = session.get(web_page)
# getting the html of the page
page_html = respone.html
# finding all divs which have h2 child using xpath
divs_parent_to_h2= page_html.xpath('//div//h2')
# printing the elements list
print(divs_parent_to_h2)Copy Code