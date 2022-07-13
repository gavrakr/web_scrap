import requests
from bs4 import BeautifulSoup
import os

a_goods =[]
b_company = []
b_links = []


os.system('clear')

html_check = requests.get("https://www.alba.co.kr")
html = BeautifulSoup(html_check.text, "html.parser")
s_brand = html.find("div", {"id" : "MainSuperBrand"})

def super_brand():
    company = s_brand.find_all("span",{"class":"company"})
    links = s_brand.find_all("a", {"clase":"brandHover"})["href"]
    for name in company:
        b_company.append(name)
    for link in links:
        if link is not None:
            b_links.append(link)
        else:
            continue
    return {"company" : b_company, "link" : b_links}

super_brand()

# def b_link():
#     for link in alba_brand.find_all('a'):
#         links.append(link.get('href'))
#         for link in links:
#             if "http:" in link:
#                 a_goods.append(link)
#             else:
#                 continue
#     for good in a_goods:
#         print(good)
