import requests


class HTTPReader(object):
	'''

	Class for reading an web page.

	
	'''

	def __init__(self):
		'''

		
		'''

		self.html = None


	@property
	def html(self):
		return self._html
	
	@html.setter
	def html(self, value):
		self._html = value 


	@property
	def status_code(self):
		return self._status_code
	
	@status_code.setter
	def status_code(self, value):
		self._status_code = value 



	def read_html(self, url):
		'''

		'''

		r = requests.get(
			url=url,
			headers={
				'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.1 Safari/605.1.15'
			}
		)

		if r.status_code == 200:
			self.html = r.text
			self.status_code = r.status_code
	
		else:
			raise ValueError("url={} returned a status code: {}".format(url, r.status_code))





