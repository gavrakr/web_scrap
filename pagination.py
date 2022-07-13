# pagination test

from typing import ParamSpecArgs
import requests
from bs4 import BeautifulSoup
import os

os.system("clear")

request = requests.get("http://hosigi.alba.co.kr/job/brand/")
soup = BeautifulSoup(request.text, "html.parser")
#pagination = soup.find("span", {"class":"pag"})


pages = soup.find("div")



print(pages)
#pages = pagination.find_all("a")

# for page in pages:
#     page = page.find("span")
#     print(page)#