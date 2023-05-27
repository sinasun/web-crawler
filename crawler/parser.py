import requests
import json
from bs4 import BeautifulSoup
from urllib.parse import urlparse, urljoin


def parse_link(link, domain):

	print("Parsing: " + link)
	response = requests.get(link)

	if response.status_code == 200:

		soup = BeautifulSoup(response.text, 'html.parser');

		data = extract_data(soup, domain)

	else:
		data = {'content': '', 'links': []}
	return data


def extract_data(soup, domain):

	links = [link.get('href') for link in soup.find_all('a')]

	filtered_links = []
	for link in links:
		parsed_link = urlparse(link)
		if not parsed_link.netloc:
			full_link = urljoin(f"https://{domain}", parsed_link.path)
			filtered_links.append(full_link)
		elif parsed_link.netloc == domain:
			filtered_links.append(link)

	filtered_links = list(set(filtered_links))


	headings = soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6'])

	paragraphs = soup.find_all('p')
	
	data = []

	for element in headings + paragraphs:
		if element.name.startswith('h'):
			data.append(('title', element.get_text(strip=True)))
		elif element.name == 'p':
			data.append(('content', element.get_text(strip=True)))


	data_json = json.dumps(data)
	return {
		'content': data_json,
		'links': filtered_links
	}


