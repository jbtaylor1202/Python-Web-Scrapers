#!/usr/bin/env python3

from urllib.request import urlopen, Request
from bs4 import BeautifulSoup

req = Request("http://www.bbcgoodfood.com/recipes/falafel-wraps-spinach-pesto-pickled-red-cabbage", headers={'User-Agent': 'Mozilla/5.0'})
webpage = urlopen(req).read()

bsObj = BeautifulSoup(webpage, "html.parser")


ingredientList=bsObj.select("#recipe-ingredients")
#ingredientList = bsObj.findAll("li",{"class":"ingredients-list__item"})

for ingredient in ingredientList:
    print(ingredient.get_text())

#ingredientGroupTitles = bsObj.findAll("h3",{"class":"ingredients-list__group-title"})

#for titles in ingredientGroupTitles:
 #   print(titles.get_text())
