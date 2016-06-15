#!/usr/bin/env python3

#Script from Chapter 1 (Page 11) of Webscraping with Python

from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup

def getTitle(url):
    try:
        html=urlopen(url)
    except HTTPError as e:
        return None
    try:
        bsObj = BeautifulSoup(html.read(), "html.parser")
        title = bsObj.h1
    except AttributeError as e:
        return None
    return title


def getHtml(url):
    try:
        html=urlopen(url)
    except HTTPError as e:
        return None
    try:
        bsObj = BeautifulSoup(html.read(), "html.parser")
        fullHtml = bsObj.prettify()
    except AttributeError as e:
        return None
    return fullHtml

title = getTitle("http://www.bbcgoodfood.com/recipes/falafel-wraps-spinach-pesto-pickled-red-cabbage")
if title == None:
    print("Title could not be found")
else:
    print(title)
    print("------END TITLE-------")


fullHtml = getHtml("http://www.bbcgoodfood.com/recipes/falafel-wraps-spinach-pesto-pickled-red-cabbage")
if fullHtml == None:
    print("HTML could not be found")
else:
    print(fullHtml)
    print("------END HTML-------")
   
