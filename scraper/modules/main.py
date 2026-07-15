from modules.fetcher import fetch
from modules.parser import parse

url = input("URL: ")

html = fetch(url)

soup = parse(html)

print(soup.title.text)
