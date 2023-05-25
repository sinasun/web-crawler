import re

from crawler.parser import parse_html
from crawler.storage import *
from crawler.utils import *

def crawl_link(domain_path, link):

	


def crawl_website(url):
	normalized_url = normalize_link(url)
	
	domain_folder = "data/" + get_domain_from_link(url)
	create_folder(domain_folder)
	
	
if __name__ == '__main__':
	
	create_folder("data")
	website_url = 'https://speedyjanitorial.ca/'

	crawl_website(website_url)


