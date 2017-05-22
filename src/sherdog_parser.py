
from bs4 import BeautifulSoup

def parse_sherdog_page(html):
	parse_name(html)

	#print(soup.prettify())

def parse_name(html):
	soup = BeautifulSoup(html, 'html.parser')
	arr = soup.find(itemprop='name').find_all('span')
	return arr[0].get_text()

def parse_nickname(html):
	soup = BeautifulSoup(html, 'html.parser')
	arr = soup.find(itemprop='name').find_all('span')
	return arr[1].get_text()