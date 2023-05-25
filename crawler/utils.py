import requests
from urllib.parse import urlparse

def check_link_availabality(link):

	reponse = requests.get(link)

	if response.status.code == 200:
		return True
	else:
		return False


def normalize_link(link):
	parsed_url = urlparse(link)

	scheme = parsed_url.scheme.lower()

	netloc = parsed_url.netloc.lower()

	normalized_url = scheme + "://" + netloc

	return normalized_url
def get_domain_from_link(link):
	parsed_url = urlparse(link)

	domain = parsed_url.netloc


	if domain.startswith('www.'):
		domain = domain[4:]

	return domain

def link_to_filename(link):
	
	filename = re.sub(r'^https?://(www\.)?', '', link)

	filename = re.sub(r'[/\\?%*:|"<>]', '_', filename)

	return filename

