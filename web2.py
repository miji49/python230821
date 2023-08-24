# web2.py

#웹서버에 통신
import requests

#크롤링
from bs4 import BeautifulSoup

url = "https://www.daangn.com/"
response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

#f = open("c:\\work\\daangn.txt", "wt", encoding="utf-8")
#기존 파일에 첨부(a+)
f = open("c:\\work\\daangn.txt", "a+", encoding="utf-8")
posts = soup.find_all("div", attrs={"class":"card-desc"})
for post in posts:
    titleElem = post.find("h2", attrs={"class":"card-title"})
    priceElem = post.find("div", attrs={"class":"card-price"})
    addrElem = post.find("div", attrs={"class":"card-region-name"})
    #print(f"{title.text}, {price.text}, {addr.text}")
    title = titleElem.text.replace("\n","")
    price = priceElem.text.replace("\n","")
    addr = addrElem.text.replace("\n","")
    print(f"{title}, {price}, {addr}")
    f.write(f"{title}, {price}, {addr}\n")

f.close()


# <div class="card-desc">
#       <h2 class="card-title">인터프로 미사일자전거 판매</h2>
#       <div class="card-price ">
#         100,000원
#       </div>
#       <div class="card-region-name">
#         경남 김해시 삼계동
#       </div>