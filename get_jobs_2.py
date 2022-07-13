import requests
from bs4 import BeautifulSoup
import os

os.system('clear')

def jobs():
    jobs_check = requests.get("http://ypyp.alba.co.kr/job/brand/")
    jobs_page = BeautifulSoup(jobs_check.text, "html.parser")
    results = jobs_page.find("tbody")
    information = []
    for result in results:
        company = result.find("span", {"class":"company"})
        if company is not None:
            company = result.find("span", {"class":"company"}).string
        else:
            continue
        
        location = result.find("td", {"class":"local first"}).text
        location = location.replace("\xa0", " ")
        
        data = result.find("td", {"class":"data"}).find("span")
        for time in data:
            if "time" in time:
                time = data.find("span", {"class":"time"}).string
            elif "console" in time:
                time = data.find("span", {"class":"consult"}).text

        pay_t = result.find("span", {"class":"payIcon"}).string
        pay_m = result.find("span", {"class":"number"}).string

        u_time = result.find("td", {"class":"regDate"}).find("strong").string

        information.append({"location":location, "company":company, "time":time, "pay":pay_t+pay_m, "update":u_time})
    return information
