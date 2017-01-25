import requests
import sys
import time
from bs4 import BeautifulSoup

url = "http://www.bom.gov.au/vic/forecasts/melbourne.shtml"
r = requests.get(url)
isEve = bool(False)
currentDate = (time.strftime("%d/%m/%Y"))
currentDay = (currentDate[0] + currentDate[1])
currentMonth = (currentDate[3] + currentDate[4])

soup = BeautifulSoup(r.content, "html.parser")

links = soup.find_all("a")

# for link in links:
#     print (link.text)

data_eve = soup.find_all("div", {"class": "day eve"})
data_main = soup.find_all("div", {"class": "day main"})
data_tomorrow = soup.find_all("div", {"<h2>"})  #don't know why this works but it does

try:
    for item in data_eve:
        print(item.text)
        isEve = True
except RuntimeError:
    print("Eve not found")

if isEve is True:
    print("\n-----------------------------------------------\n")

for item in data_main:
    print(item.text)
    sys.stdout.flush()

if isEve is False:
    print("\n-----------------------------------------------\n")

for item in data_tomorrow:
    print(item.text)
    sys.stdout.flush()

input()
