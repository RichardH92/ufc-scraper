
from bs4 import BeautifulSoup

def parse_sherdog_page(html):
	fighter = {}

	fighter = parse_bio(html, fighter)
	fighter = parse_fight_stats(html, fighter)

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
	fighter['age'] = soup.find('span', class_='item birthday').find('strong').get_text()[5:]

	return fighter

def parse_fight_stats(html, fighter):

	fighter['wins'] = parse_win_stats(html)
	fighter['losses'] = parse_loss_stats(html)

	return fighter

def parse_win_stats(html):
	soup = BeautifulSoup(html, 'html.parser')
	wins = {}

	wins['total'] = soup.find('div', class_='left_side').find('span', class_='counter').get_text()
	
	wins_ko = soup.find('div', class_='left_side').find_all('span', class_='graph_tag')[0].get_text()
	wins['knockouts'] = wins_ko[:wins_ko.find(' ')]

	wins_sub = soup.find('div', class_='left_side').find_all('span', class_='graph_tag')[1].get_text()
	wins['submissions'] = wins_sub[:wins_sub.find(' ')]

	wins_dec = soup.find('div', class_='left_side').find_all('span', class_='graph_tag')[2].get_text()
	wins['decisions'] = wins_dec[:wins_dec.find(' ')]

	wins_oth = soup.find('div', class_='left_side').find_all('span', class_='graph_tag')[3].get_text()
	wins['others'] = wins_oth[:wins_oth.find(' ')]

	return wins


def parse_loss_stats(html):

	return fighter