from .qiscus import Qiscus

class QiscusBuilder(object):
	'''
	Qiscus builder class
		- __init__(app_id=None, app_secret=None)
		- set_app_id(app_id)
		- set_app_secret(app_secret)
		- build() @return qiscus object
	support chaining call such as qis = Qiscus().set_app_id(x).set_app_secret(y).build()
	'''

	def __init__(self, app_id=None, app_secret=None):
		'''
		__init__ 
		initialize qiscus object sdk to work with the api
			params:
				+ app_id (optional, default=None) app id retrieved from qiscus when creating app
				+ app_secret (optional, default=None) app_secret retrieved from qiscus when creating app
		'''
		self.app_id = app_id
		self.app_secret = app_secret

	def set_app_id(self, app_id):
		'''
		set_app_id(app_id, required)
		return qiscus object 
		'''
		self.app_id = app_id
		return self

	def set_app_secret(self, app_secret):
		'''
		set_app_secret(app_secret, required)
		return qiscus object 
		'''
		self.app_secret = app_secret
		return self

	def build(self):
		'''
		build()
		@return qiscus object to work with
		'''
		if None in [self.app_id, self.app_secret]:
			raise ValueError('app_id or app_secret not set')
		self.base_url = str(self.app_id) + '.qiscus.com'
		return Qiscus(self.base_url, self.app_secret)
