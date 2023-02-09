

class WebCrawler(object):
	'''
	
	This is a generic web crawler class for data scraping projects.

	This class assumes two kinds of pages will be scraped:

	a link page - such as a search result from Amazon.
	a data page - such as an Amazon project page.

	The link page has links to the data pages and possible a link to the next
	link page (example: next button on a Google seach result page.)

	A data page contains the data of interest.


	Parameters
	__________

	base_url: this is the url to start the crawl. It's usuall the first link page.

	link_scraper: site specific class and used to scape a link page. It returns
	urls to data pages. And it returns a url to the next link page.

	data_scraper: site specific class used to scrape a data page. It
	returns a dictionary of the data of interest.

	output_formatter: a formatter class to convert the dictionary data to
	another format. A common format is JSON or CSV.

	depth: limits the number of link pages visited.


	Attributes:

	link_urls: list of link page urls that were crawled

	data_urls: list of data page urls that were scraped

	data: list of data page dictionaries.



	'''


	def __init__(self, base_url, link_scraper, data_scraper, output_format=None, depth=None):
		'''



		'''
		pass 