import requests
from bs4 import BeautifulSoup

url = "https://www.bbc.com/news"

response = requests.get(url, timeout=15)
response.raise_for_status()

soup = BeautifulSoup(response.text, "html.parser")

headlines = soup.find_all(["h1", "h2", "h3"])

for h in headlines:
    title = h.get_text(strip=True)
    link = h.find("a")

    if link and link.get("href"):
        href = link["href"]
        if href.startswith("/"):
            href = requests.compat.urljoin(url, href)
        print("Headline:", title)
        print("Link:", href)
        print()
    else:
        print("Headline:", title)
        print("Link: Not available\n")