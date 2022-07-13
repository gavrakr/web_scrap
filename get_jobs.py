import requests
from bs4 import BeautifulSoup
import os

os.system('clear')

def jobs(url=""):
    jobs_check = requests.get(url)
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
        location = location.replace("\xa0", "_")
        
        data = result.find("td", {"class":"data"}).find("span")
        for time in data:
            if "time" in time:
                time = data.find("span", {"class":"time"}).string
            elif "console" in time:
                time = data.find("span", {"class":"consult"}).text

        pay_t = result.find("span", {"class":"payIcon"}).string
        pay_m = result.find("span", {"class":"number"}).string

        u_time = result.find("td", {"class":"regDate"}).find("strong")
        if u_time is not None:
            u_time = u_time.string
        else:
            continue

        information.append(f"{location}, {company}, {time}, {pay_t+pay_m}, {u_time}")
    return information
