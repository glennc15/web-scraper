import unittest

import rlcompleter
import pdb 
pdb.Pdb.complete = rlcompleter.Completer(locals()).complete



from web_scraper.web_scraper import WebScraper 

class WebScraperTests(unittest.TestCase):


	def test_reddit_scraper_01(self):
		'''


		'''

		from web_scraper.page_scrapers.reddit_link_scraper import RedditLinkScraper
		from web_scraper.page_scrapers.reddit_page_scraper import RedditPageScraper
		from web_scraper.output_classes.json_formatter import JSONFormatter


		my_scraper = WebScraper(
			base_url='',
			link_scraper=RedditLinkScraper,
			data_scraper=RedditPageScraper,
			output_format=JSONFormatter,
			depth=2
		)


		self.assertEquals(len(my_scraper.link_urls), 2)
		self.assertTrue(len(my_scraper.data_urls) >= 2)



