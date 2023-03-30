# Here in this code I have scrape just single page and exported to csv using writer package.
import requests
from bs4 import BeautifulSoup
from csv import writer

url = "https://books.toscrape.com/catalogue/page-1.html"
response = requests.get(url)
data = response.content
# print(data)

soup = BeautifulSoup(data, 'html.parser')
ol = soup.find("ol", class_="row")
li = ol.find_all('li')
# print(len(li))

with open('books_data.csv', 'w', encoding="utf8", newline='') as f:
    thewriter = writer(f)
    headerrow = ['Title', 'Rating', 'Price']
    thewriter.writerow(headerrow)
    for i in li:
        article = i.find('article')

        title = article.find('div', class_="image_container").find('img').attrs['alt']  # Find ALT tag in image
        # used to find class name
        rating = article.find('p', class_="star-rating")['class'][1]
        price = article.find("p", class_="price_color").text[1:]
        op = [title, rating, price]
        # print(op)
        thewriter.writerow(op)
