import requests
import urllib.request
import time
from bs4 import BeautifulSoup

url = "http://kunalsdatabase.com/ebooks/2016/"
response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

#soup.findAll('a') #finds all anchor tags
#starts the search from line 51


# http://kunalsdatabase.com/ebooks/2016/1001%20People%20Who%20Made%20America%20-%20Alan%20Axelrod.epub
# 1001%20People%20Who%20Made%20America%20-%20Alan%20Axelrod.epub


for i in range(6,len(soup.findAll('a'))+1): #'a' tags are for links
    one_a_tag = soup.findAll('a')[i]
    link = one_a_tag['href']
    name = link.replace("%20","")
    #name = name.replace("-","")
    print(name)
    download_url = 'http://kunalsdatabase.com/ebooks/2016/'+ link
    urllib.request.urlretrieve(download_url,name) 
    time.sleep(1) #pause the code for a sec