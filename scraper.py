from selenium import webdriver
from bs4 import BeautifulSoup
import time
import csv
import requests
import pandas as pd

url = "https://en.wikipedia.org/wiki/List_of_brown_dwarfs#Field_brown_dwarfs"
page = requests.get(url)

soup = BeautifulSoup(page.text, 'html.parser')

brown_dwarf_table = soup.find_all('table')
table_rows = brown_dwarf_table[7].find_all('tr')

brown_dwarf_stars = []
temp_list = []
for tr_tag in soup.find_all("tr", attrs={"class": "fact_row"}):
    td_tags = tr_tag.find_all("td")
    for td_tag in td_tags:
        try:
            temp_list.append(td_tag.find_all(
            "div", attrs={"class": "value"})[0].contents[0])
        except:
            temp_list.append("")
    brown_dwarf_stars.append(temp_list)

headers = ["Brown dwarf", "Constellation", "Right ascension", "Declination", "App.mag.", "Distance", "Spectral type", "Mass", "Radius", "Discovery year"]

with open("final.csv", "w") as f:
        csvwriter = csv.writer(f)
        csvwriter.writerow(headers)
        csvwriter.writerows(brown_dwarf_stars)