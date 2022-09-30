import requests
from bs4 import BeautifulSoup
import time
import sys

for line in sys.stdin:
  line = line.rstrip("\n")
  author, url = line.split("\t")
  
  url = f"https://scholar.google.com/{url}"
  headers = {
      'User-Agent': 'Mozilla/5.0 (Android 4.4; Mobile; rv:41.0) Gecko/41.0 Firefox/41.0',
  }

  page = requests.get(url, headers=headers)
  soup = BeautifulSoup(page.content, "html.parser")

  author_affil = soup.find_all('div', class_='gsc_prf_il')
  for af in author_affil:
    aft = af.get_text()
    print(f"{author}\t{aft}")
    break

    time.sleep(5)



  