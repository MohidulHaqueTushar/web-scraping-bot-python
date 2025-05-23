import requests
from bs4 import BeautifulSoup

url = "https://finance.yahoo.com/quote/GOOGL?p=GOOGL&.tsrc=fin-srch"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36"
}

html_page = requests.get(url, headers=headers)

soup = BeautifulSoup(html_page.content, "lxml")


header_info = soup.find_all("div", id="quote-header-info")[0]
stock_title = header_info.find("h1").get_text()
current_price = header_info.find("div", class_="My(6px) Pos(r) smartphone_Mt(6px)")

print(stock_title)
print(current_price)
