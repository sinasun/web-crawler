from bs4 import BeautifulSoup


def parse_html(html):

	soup = BeautifulSoup(html, 'html.parser');


	data = extract_data(soup)


	return data



def extract_data(html):

	links = [link.get('href') for link in soup.find_all('a')]

	headings = soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6'])

	paragraphs = soup.find_all('p')
	
	data = []

	for element in headings + paragraphs:
		if element.name.startswith('h'):
			data.append(('title', element.get_text(strip=True)))
		elif element.name == 'p':
			data.append(('content', element.get_text(strip=True)))

	return {
		'data': data,
		'links': links
	}


