from abc import ABC, abstractmethod

class ScraperBase(ABC):
	'''
	
	provides and interface for all scrapers classes.

	'''


	@property
	def url(self):
		return self._url 

	@url.setter
	def url(self, value):
		self._url = value 

	@property
	def success(self):
		return self._success
	
	@success.setter
	def success(self, value):
		self._success = value 


	@abstractmethod
	def scrape(self):
		pass 