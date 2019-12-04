""" 
@Author Sachi Adikaram 
Created on December 03rd 2019
"""
import requests
import pandas as pd
from bs4 import BeautifulSoup


# Items to be searched on ebay
items = ['Canon Mirrorless camera', 'Sony Mirrorless camera', 'Nikon Mirrorless camera', 'Panasonic Mirrorless camera']

# A function to return the urls of the items that'll be serached
def create_url(items):
  #url for ebay's search page
  url = 'https://www.ebay.com/sch/i.html?_from=R40&_trksid=p2380057.m570.l1312.R1.TR11.TRC2.A0.H0.XIp.TRS1&_nkw='
  url_lst = []

  for item in items:
    url_lst.append(url + item.replace(' ', '+'))

  return url_lst  

# Scrapes and prints the url, name, and price of the first item result listed on eBay
def scrape_ebay(url_lst):
  item_names = []  
  item_prices = []
  for url in url_lst:
    #Downloads the ebay page for processing
    webpage = requests.get(url)
    # Raises an exception error if there's an error downloading the website
    webpage.raise_for_status()
    # Creates a BeautifulSoup object for HTML parsing
    soup = BeautifulSoup(webpage.text, 'html.parser')
    #Scrapes the first listed item's name
    item_name = soup.find('h3', {'class': 's-item__title'}).get_text()
    #Scraped the first listed item's price
    item_price = soup.find('span', {'class': 's-item__price'}).get_text()
    
    #Append the names and the prices of the items to two separate lists
    item_names.append(item_name)
    item_prices.append(item_price)
    

  #Use pandas to represent the data in a table
  data = {
          'Camera': item_names,
          'Price': item_prices
         }
  data_pandas = pd.DataFrame(data)  
  print(data_pandas)  
    


    

scrape_ebay(create_url(items))


      



    
 






















