import requests
import bs4
result=requests.get("https://www.trustpilot.com/categories/clothing_store")
result.text #It returns the web source as Python String
soup=bs4.BeautifulSoup(result.text,'lxml') #parsing the text to html
# print(soup)
for i in range(10):
    title=(soup.select(".styles_displayName__1LIcI")[i].getText())
    stars=(soup.select(".styles_desktop__3N0-b")[i].getText())
    review3=((soup.select(".styles_ratingText__nheL7")[i].getText().split(' '))[1].split('|'))[1]
    print(title)
    print(stars)
    print(review3)
    print("***********************")
