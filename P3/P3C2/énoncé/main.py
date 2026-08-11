from math import prod

import requests
from bs4 import BeautifulSoup
with open("index.html", "r") as file:
  soup = BeautifulSoup(file.read(), 'html.parser')

title = soup.title
h1_node = soup.find(id="titre")
h1 = h1_node.string if h1_node else ""

all_products = dict()

products = soup.find_all("li", class_="product")

for product in products:
  name_node = product.h2
  name = name_node.string if name_node else ""

  price_node = product.find("p", class_="price")
  price_str = price_node.string if price_node else ""
  price_list = price_str.split(" ") if price_str else []
  price = price_list[1]

  all_products[name] = {"prix": price}

  description_node = product.find_all("p")[-1]
  description = description_node.string if description_node else ""

  all_products[name]["description"] = description

print(f"Liste des produits : {all_products}")

for name in all_products.keys():
  price_str = all_products[name]["prix"]
  price = price_str.strip("€")
  price = float(price)
  price_dollar = price * 1.2
  all_products[name]["prix_dollar"] = f"{price_dollar}$"

print(f"Dollar : {all_products}")

