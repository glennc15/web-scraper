

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

		#  initializations:
		self.link_urls = list()
		self.data_urls = list()
		self.data =list()
		
		self.crawl(base_url=base_url, 
			link_scraper=link_scraper, 
			data_scraper=data_scraper, 
			output_format=output_format, 
			depth=depth
		)




	@property
	def link_urls(self):
		return self._link_urls
	
	@link_urls.setter
	def link_urls(self, value):
		self._link_urls = value 

	@property
	def data_urls(self):
		return self._data_urls
	
	@data_urls.setter
	def data_urls(self, value):
		self._data_urls = value 

	@property
	def data(self):
		return self._data
	
	@data.setter
	def data(self, value):
		self._data = value


	# ***********************************************************************************************
	# START: Internal methods:

	def crawl(self, base_url, link_scraper, data_scraper, output_format, depth):
		'''

		'''

		self.link_urls.append(base_url)
		this_base_url = base_url

		safety_ctr = 0
		max_safety_ctr = 10

		# crawls link pages for data page urls
		while this_base_url:


			this_base_url, data_page_urls = link_scraper(url=this_base_url).scrape()

			if this_base_url is not None:
				self.link_urls.append(this_base_url)

			self.data_urls = self.data_urls + data_page_urls


			if isinstance(depth, int):
				if len(self.link_urls) >= depth:
					break


			safety_ctr += 1

			if safety_ctr >= max_safety_ctr:
				break


		# scrape the data page urls:
		for data_page_url in self.data_urls:
			this_data_scraper = data_scraper(url=data_page_url)
			scrape_data = this_data_scraper.scrape()
			
			if this_data_scraper.success:
				self.data.append(scrape_data)



	# End: Internal methods:
	# ***********************************************************************************************


