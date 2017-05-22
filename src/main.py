#!/usr/bin/python

import tor_handler
import sherdog_scraper

url = "http://www.sherdog.com/fighter/Matt-Riddle-34072"
SOCKS_PORT = 7000

tor_process = tor_handler.connect_to_tor(SOCKS_PORT)

sherdog_scraper.scrape_url(url, SOCKS_PORT)

tor_handler.disconnect_from_tor(tor_process)