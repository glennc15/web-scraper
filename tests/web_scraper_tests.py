import unittest

import rlcompleter
import pdb 
pdb.Pdb.complete = rlcompleter.Completer(locals()).complete




class WebScraperTests(unittest.TestCase):


	def test_reddit_scraper_01(self):
		'''


		'''


		from web_scraper.web_crawler import WebCrawler 
		from web_scraper.page_scrapers.reddit_link_scraper import RedditLinkScraper
		from web_scraper.page_scrapers.reddit_page_scraper import RedditPageScraper
		from web_scraper.output_classes.json_formatter import JSONFormatter


		my_crawler = WebCrawler(
			base_url='https://old.reddit.com/r/islam/new/',
			link_scraper=RedditLinkScraper,
			data_scraper=RedditPageScraper,
			output_format=JSONFormatter,
			depth=2
		)


		self.assertEqual(len(my_crawler.link_urls), 2)
		self.assertTrue(len(my_crawler.data_urls) >= 2)


		self.assertEqual(len(my_crawler.data_urls), len(my_crawler.data))




