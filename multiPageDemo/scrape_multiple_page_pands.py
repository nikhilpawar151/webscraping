# In this program I have used pandas to export the book data. We have used multi page scraping in this program.
import requests
from bs4 import BeautifulSoup
import pandas as pd

baseurl = "https://books.toscrape.com"
url = baseurl

books = []

while (True):
    print(url)
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    section = soup.find("section")
    lists = section.find('ol').find_all('li')
    for list in lists:
        article = list.find("article", class_="product_pod")
        title = article.find("div", class_="image_container").find(
            'img').attrs['alt']
        ratings = article.find('p', class_="star-rating")['class'][1]
        price = article.find('p', class_="price_color").text[1:]
        row = [title, ratings, price]
        books.append(row)
    next = section.find('ul', class_="pager").find(
        'li', class_="next")
    if next == None:
        break
    next = next.find('a').attrs['href']
    if url == baseurl:
        url = url + "/" + next
    else:
        url = url[0:url.rfind('/') + 1] + next

df = pd.DataFrame(books, columns=['Title', 'Rating', "Price"])
df.to_csv('pandas_books_exports.csv')
