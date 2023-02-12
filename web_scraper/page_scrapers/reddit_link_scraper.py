from bs4 import BeautifulSoup

from urllib.parse import urlsplit, urlunsplit


from web_scraper.page_scrapers.scraper_base import ScraperBase
from web_scraper.page_scrapers.http_reader import HTTPReader



class RedditLinkScraper(ScraperBase, HTTPReader):
	'''
	
	HTML Scraper for a Reddit subreddit page. 

	scrapes the link to all posts and the link to the next subreddit page.

	'''


	def __init__(self, url):
		'''


		'''

		self.url = url



	def scrape(self):
		'''

		'''

		self.read_html(url=self.url)


		soup = BeautifulSoup(self.html, 'html.parser')

		# find the url for each post.
		# each post is contained in a <div class='thing ...' ...></div>:

		data_urls = list()
		for post in soup.find_all(name='div', attrs={'class': 'thing'}):
			a_title_tag = post.find(name='a', attrs={'title'})

			data_url = self.post_url(post_url=a_title_tag.attrs['href'])
			data_urls.append(data_url)


		# find the next page url if it exits:
		next_nav_tag = soup.find(name='span', attrs={'class': 'next-button'})


		if next_nav_tag:
			next_page_url = next_nav_tag.find(name='a').attrs['href']

		else:
			next_page_url = None


		self.success = True


		return (next_page_url, data_urls)


	def post_url(self, post_url):
		'''
		
		The post url is a relative url. Adding the net location to the relative url

		'''
	
		# using the scheme and the net location from the link page url and
		# adding the post path
		url_tuple = urlsplit(self.url)
		url_tuple = url_tuple._replace(path=post_url)

		full_post_path = urlunsplit(url_tuple)


		return full_post_path









