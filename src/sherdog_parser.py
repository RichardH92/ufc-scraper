
from bs4 import BeautifulSoup

def parse_sherdog_page(html):
	fighter = {}

	fighter = parse_bio(html, fighter)
	fighter = parse_win_stats(html, fighter)

	print(fighter)

def parse_bio(html, fighter):
	soup = BeautifulSoup(html, 'html.parser')

	fighter['name'] = soup.find(itemprop='name').find_all('span')[0].get_text()
	fighter['nickname'] = soup.find(itemprop='name').find_all('span')[1].get_text()
	fighter['birthday'] = soup.find('span', itemprop='birthDate').get_text()
	fighter['locality'] = soup.find('span', itemprop='addressLocality').get_text()
	fighter['nationality'] = soup.find('strong', itemprop='nationality').get_text()
	fighter['association'] = soup.find('h5', class_='item association').find('strong').get_text()
	fighter['height'] = soup.find('span', class_='item height').find('strong').get_text()
	fighter['weight'] = soup.find('span', class_='item weight').find('strong').get_text()
	fighter['weight_class'] = soup.find('h6', class_='item wclass').find('strong').get_text()

	#TODO: Substr this
	fighter['age'] = soup.find('span', class_='item birthday').find('strong').get_text()

	return fighter

def parse_fight_stats(html, fighter):

	fighter = parse_win_stats(html, fighter)
	fighter = parse_loss_stats(html, fighter)

	return fighter

def parse_win_stats(html, fighter):

	return fighter


def parse_loss_stats(html, fighter):

	return fighter