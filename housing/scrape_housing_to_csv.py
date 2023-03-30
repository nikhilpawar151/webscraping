from bs4 import BeautifulSoup
import requests
from csv import writer

url = "https://housing.com/rent/search-Plqq7bm2s53fechd"
page = requests.get(url)

# print(page)  # To print response code must be 200
soup = BeautifulSoup(page.content, 'html.parser')
lists = soup.find_all("article", class_="css-10x9k9b")
# print(len(lists))

with open('housing_data.csv', 'w', encoding='utf-8-sig', newline='') as f:
    thewriter = writer(f)
    header = ['Sr. No.', 'Broker', 'Price', 'Size', 'Details']
    i = 1
    thewriter.writerow(header)
    for l in lists:
        # .find("span", class_="css-0").text
        broker = l.find("div", class_="css-a17j20").find("a",
                                                         class_="css-0").contents[0]
        price = l.find("div", class_="css-132rfk5").text
        size = l.find("div", class_="css-11nfaq3").text
        details = l.find("div", class_="css-79elbk").find("span",
                                                          class_="css-14g5neq").text.replace('\n', ' ')
        data = [i, broker, price, size, details]
        thewriter.writerow(data)
        # print(data)
        i += 1
""" 

data = urllib.request.urlopen(url).read()
print(data)
 """
