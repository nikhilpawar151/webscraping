#In this code we have scrap multiple pages from the website and store book's data in CSV. We have used writer library to export data to CSV
import requests
from bs4 import BeautifulSoup
from csv import writer

baseurl = "https://books.toscrape.com"
url = baseurl
counter = 1
with open('multi_page_writers.csv', 'w', encoding='utf8', newline='') as f:
    thewriter = writer(f)
    headerrow = ["Title", "Rating", "Price"]
    thewriter.writerow(headerrow)
    while (True):
        print(url)
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')

        section = soup.find("section")
        lists = section.find('ol').find_all('li')
        for list in lists:
            article = list.find("article", class_="product_pod")
            title = article.find("div", class_="image_container").find('img').attrs['alt']
            ratings = article.find('p', class_="star-rating")['class'][1]
            price = article.find('p', class_="price_color").text[1:]
            row = [title, ratings, price]
            thewriter.writerow(row)
        next = section.find('ul', class_="pager").find(
            'li', class_="next")
        if next == None:
            break
        next = next.find('a').attrs['href']
        if url == baseurl:
            url = url + "/" + next
        else:
            url = url[0:url.rfind('/') + 1] + next
