import requests
import csv
from bs4 import BeautifulSoup

url = "https://books.toscrape.com/"

response = requests.get(url, timeout=15)
response.raise_for_status()

soup = BeautifulSoup(response.text, "html.parser")

with open("products.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Product Name", "Price"])

    products = soup.find_all("article", class_="product_pod")

    for p in products:
        name = p.h3.a["title"]
        price = p.find("p", class_="price_color").get_text(strip=True)

        writer.writerow([name, price])
        print(name, price)

print("Data saved to products.csv")