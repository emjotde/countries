import requests
from bs4 import BeautifulSoup
import time
import sys

i = 0
cont = True
while cont:

  URL = f"https://scholar.google.com/scholar?start={i}&hl=en&as_sdt=5,48&cites={sys.argv[1]}&scipsc="
  headers = {
      'User-Agent': 'Mozilla/5.0 (Android 4.4; Mobile; rv:41.0) Gecko/41.0 Firefox/41.0',
  }

  page = requests.get(URL, headers=headers)
  soup = BeautifulSoup(page.content, "html.parser")

  print(soup.get_text(), file=sys.stderr)

  author_fields = soup.find_all('div', class_='gs_a')

  found = False
  for af in author_fields:
    authors = af.find_all('a')
    for a in authors:
      if a.has_attr('href'):
        found = True;
        print(f"{a.get_text()}\t{a['href']}")
        print(f"{a.get_text()}\t{a['href']}", file=sys.stderr)
  
  cont = found
  i += 10
  time.sleep(10)
