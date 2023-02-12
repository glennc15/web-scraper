from bs4 import BeautifulSoup

from urllib.parse import urlsplit

from web_scraper.page_scrapers.scraper_base import ScraperBase
from web_scraper.page_scrapers.http_reader import HTTPReader


class RedditPageScraper(ScraperBase, HTTPReader):
	'''
	
	HTML scraper for a Reddit post.


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


		# parse the title, author, time, and post:
		a_title_tag = soup.find(name='a', attrs={'class': 'title'})
		a_author_tag = soup.find(name='a', attrs={'class': 'author'})
		time_tag = soup.find(name='time')

		# post strings are contained in <p> tags:
		# only need the path from the url

		url_parts = urlsplit(self.url)

		post_body = soup.find(
			name='div', 
			attrs={'class': 'thing', 'data-url': url_parts.path}
		)

		post_str = ""

		# if the post body is empty this tag will not exists
		if post_body:
			post_data = post_body.find(name='div', attrs={'class': 'md'})

			if post_data:
				# add all the <p> tags
				for this_p_tag in post_data.find_all(name='p'):
					post_str += ' '.join([x.lower() for x in this_p_tag.contents if isinstance(x, str)])

   

		subreddit_data = {
			'submission date': time_tag.attrs['datetime'],
			'submitter username': a_author_tag.contents[0],
			'title': a_title_tag.contents[0],
			'post': post_str,
			'url': self.url
		}


		self.success = True


		return subreddit_data


	# ***********************************************************************************************
	# START: Internal methods:


	# End: Internal methods:
	# ***********************************************************************************************	