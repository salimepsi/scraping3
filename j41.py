import requests
from bs4 import BeautifulSoup
import re

url = "https://www.papo-france.com/fr/les-dinosaures/566-t-rex.html"
response = requests.get(url)
content = response.content
soup = BeautifulSoup(content, "html.parser")
div = soup.find("div", class_="rte align_justify")
print(div)