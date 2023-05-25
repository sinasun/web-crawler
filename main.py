from urlib.parse import urlparse

from crawler.parser import parse_html
from crawler.storage import *



def normalize_link(link):
	parsed_url = urlparse(link)

	scheme = parsed_url.scheme.lower()

	netloc = parsed_url.netloc.lower()

	normalized_url = f"{scheme://{netloc}"

	return normalized_url

def get_domain_from_link(link):
	domain = urlparse(link)

	domain = parsed_url.netloc


	if domain.startswith('www.'):
		domain = domain[4:]

	return domain

def link_to_filename(link):
	
	filename = re.sub(r'^https?://(www\.)?', '', link)

	filename = re.sub(r'[/\\?%*:|"<>]', '_', filename)

	return filename

def crawl_website(url):
	normalized_url = normalize_link(url)
	
	create_folder(link_to_filename())	


	



if __name__ == '__main__':

	website_url = 'https://speedyjanitorial.ca/'

	crawl_website(website_url)


