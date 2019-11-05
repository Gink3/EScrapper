import requests
import urllib.request
import time
from bs4 import BeautifulSoup

url = "http://kunalsdatabase.com/ebooks/2016/"
response = requests.get(url)

