import argparse

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

def crawl_website(url, output_folder):
	domain = get_domain_from_link(url)	
	domain_folder = output_folder + domain
	create_folder(domain_folder)
	crawl_link(domain_folder, url, domain)
	
if __name__ == '__main__':
	parser = argparse.ArgumentParser(prog="WebCrawler", description="Python Web Crawler", epilog="python3 main.py -w https://example.com -o data/")

	parser.add_argument('-w', '--website', help="The website url to crawl")
	parser.add_argument('-o', '--output', default="data/", help="Output folder")

	args = parser.parse_args()

	output_folder = args.output
	website_url = args.website
	
	create_folder(output_folder)
	crawl_website(website_url, output_folder)

