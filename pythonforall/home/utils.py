import requests
from bs4 import BeautifulSoup

def scrape():
    page = requests.get('https://medium.com/search?q=python')
    soup = BeautifulSoup(page.text, 'html.parser')
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
