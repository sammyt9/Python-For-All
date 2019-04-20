import requests
import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def scrape():
    # browser = webdriver.Firefox()
    browser = webdriver.Chrome('C:\\Users\\stien\\Downloads\\chromedriver_win32\\chromedriver.exe')
    browser.get('https://medium.com/search?q=python')
    time.sleep(1)

    elem = browser.find_element_by_tag_name("body")

    num_Pagedowns = 50

    while num_Pagedowns:
        elem.send_keys(Keys.PAGE_DOWN)
        time.sleep(0.3)
        num_Pagedowns -= 1

    page = browser.page_source
    soup = BeautifulSoup(browser.page_source)
    body = soup.find(class_='col u-size9of12 u-sm-size12of12')

    articles = soup.findAll("div", {"class": "postArticle-content"})
    data_list = []
    for x in articles:
        data = dict()
        if x.img is not None:
            data['image'] = x.img['src']
        else:
            data['image'] = ""

        if x.h3 is not None:
            data['title'] = x.h3.string.replace("\xa0", " ")
        else: 
            data['title'] = ""
        
        if x.a is not None:
            data['link'] = x.a['href']
        else:
            data['link'] = ""
        
        data_list.append(data)
    return data_list
