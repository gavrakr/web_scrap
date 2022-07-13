import requests
from bs4 import BeautifulSoup
import os

os.system("clear")

alba_url = "http://www.alba.co.kr"

check = requests.get(alba_url)
soup = BeautifulSoup(check.text, "html.parser")
results = soup.find("div", {"id":"MainSuperBrand"})

def b_company():
    a = []
    b = []
    c = {}

    c_result = results.find_all("span", {"class":"company"})
    for company in c_result:
        company = company.string
        if company is not None:
            company
        else:
            continue
        a.append(company)

    l_result = results.find_all("a", {"class":"goodsBox-info"})
    #print(l_result)
    for link in l_result:
        link = link.get("href")
        b.append(link)

    for i in range(len(a)):
        c[a[i]] = b[i]

    return c

