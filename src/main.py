#!/usr/bin/python

import tor_handler
import sherdog_scraper
import ufc_scraper
from google import search
import json

def get_sherdog_url(fighter):
  search_results = search(fighter + ' sherdog', stop=5)
  for result in search_results:
      if 'sherdog.com/fighter/' in result and 'm.sherdog' not in result:
        return result

  return ''

def get_ufc_url(fighter):
  search_results = search(fighter + ' ufc', stop=5)
  for result in search_results:
      if 'ufc.com/fighter/' in result and 'm.ufc' not in result:
        return result

  return ''

def scrape_fighter(fighter_name):
  fighter = {}

  ufc_url = get_ufc_url(fighter_name)
  sherdog_url = get_sherdog_url(fighter_name)

  sherdog_scraper.scrape_url(sherdog_url, SOCKS_PORT, fighter)
  ufc_scraper.scrape_url(ufc_url, SOCKS_PORT, fighter)

  return fighter

def read_fighter_names():
  with open("fighter_names.txt") as f:
    fighters_list = f.readlines()
  return [x.strip() for x in fighters_list]

def write_fighter_dict():
  json = json.dumps(fighters_dict)
  f = open("fighters.json","w")
  f.write(json)
  f.close() 


SOCKS_PORT = 7000
fighters_dict = {}
fighters_list = read_fighter_names()

tor_process = tor_handler.connect_to_tor(SOCKS_PORT)


for fighter_name in fighters_list:
  
  try:
    fighters_dict[fighter_name] = scrape_fighter(fighter_name)
    print (fighter_name + ' - Success')
  except (AttributeError, IndexError, ValueError):
    print (fighter_name + ' - Error')
  
#tor_handler.disconnect_from_tor(tor_process)