from bs4 import BeautifulSoup as soup
import bs4
from urllib.request import Request, urlopen
from instabot import Bot 

username = input("Kindly Enter Your Username : ")
password = input("Kindly Enter Your Password : ")
path_image = input("kindly Enter The Path Of The Image : ")
hash_idea = input("Kindly Enter One hashtag Related to your Post : ")
cap = input("Enter If you want any other text in caption : ")


url = ("https://www.best-hashtags.com/hashtag/" + hash_idea)
req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
page = urlopen(req,timeout=10)
page_html = page.read()
page.close()
page_soup = soup(page_html, "html.parser")
result = page_soup.find("div",{"class":"tag-box tag-box-v3 margin-bottom-40"})
tags = result.decode()
start_index = tags.find("#")
end_index = tags.find("</p1>")
tags = tags[start_index:end_index]
tags = tags + '\n' +cap



bot = Bot()
bot.login(username=username,password=password)
bot.upload_photo(path_image,caption=tags)

