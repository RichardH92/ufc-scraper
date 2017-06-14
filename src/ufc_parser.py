from bs4 import BeautifulSoup

def parse_ufc_page(html, fighter):

	fighter['strikes'] = parse_striking_metrics(html)
	fighter['takedowns'] = parse_grappling_metrics(html)

	print(fighter)

	return

def parse_striking_metrics(html):
	strikes = {}
	soup = BeautifulSoup(html, 'html.parser')

	str_attempted = soup.find_all('div', class_='graph')[0]
	strikes['attempted'] = int(str_attempted.find('div', class_='max-number').get_text())

	str_succ = soup.find('div', class_='graph', id='types-of-successful-strikes-graph')
	strikes['successful'] = int(str_succ.find('div', class_='max-number').get_text())

	strikes['standing'] = int(str_succ.find_all('div', class_='text-bar')[0].get_text())
	strikes['clinch'] = int(str_succ.find_all('div', class_='text-bar')[1].get_text())
	strikes['ground'] = int(str_succ.find_all('div', class_='text-bar')[2].get_text())

	return strikes

def parse_grappling_metrics(html):
	takedowns = {}
	soup = BeautifulSoup(html, 'html.parser')

	td_attempted = soup.find_all('div', class_='graph')[2]
	takedowns['attempted'] = int(td_attempted.find('div', class_='max-number').get_text())

	td_succ = soup.find_all('div', class_='graph')[2]
	takedowns['successful'] = int(td_succ.find('div', id='total-takedowns-number').get_text())

	td_types = soup.find('div', class_='graph', id='grappling-totals-by-type-graph')
	takedowns['submissions'] = int(td_types.find_all('div', class_='text-bar')[0].get_text())
	takedowns['passes'] = int(td_types.find_all('div', class_='text-bar')[1].get_text())
	takedowns['sweeps'] = int(td_types.find_all('div', class_='text-bar')[2].get_text())

	return takedowns