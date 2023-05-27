
from crawler.parser import parse_link
from crawler.storage import *
from crawler.utils import *

def crawl_link(domain_path, link, domain):
	append_to_file(domain_path + "/scraped.txt", link + "\n")
	
	data = parse_link(link, domain)

	append_to_file(domain_path + "/" + link_to_filename(link), data['content'])

	for url in data['links']:
		if not check_line_exists(domain_path + "/scraped.txt", url):
			crawl_link(domain_path, url, domain)


def crawl_website(url):
	normalized_url = normalize_link(url)
	domain = get_domain_from_link(url)	
	domain_folder = "data/" + domain
	create_folder(domain_folder)
	
	crawl_link(domain_folder, url, domain)
	
if __name__ == '__main__':
	
	create_folder("data")
	website_url = 'https://speedyjanitorial.ca/'

	crawl_website(website_url)


