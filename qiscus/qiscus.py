from .api.api_base import ApiBase
from .configs.constants import API_BASE_URI, ENDPOINTS


class Qiscus(ApiBase):
	'''
	main qiscus class for api call
		methods:
			- login_register(email, password, username, avatar_url, device_token, device_platform [optional]) 
				this will log user in or register them if not exist
	'''

	def __init__(self, base_url, app_secret):
		'''
		__init__(base_url, app_secret)
		build api base url and default headers
		'''
		self.base_url = 'https://' + base_url + API_BASE_URI
		self.headers = {
			'Accept': 'application/json',
			'Content-Type': 'application/json',
			'qiscus_sdk_secret': app_secret
		}

	def login_register(self, payloads):
		'''
		login_register(payloads [required])
		 - payloads consists of
		 	+ email
		 	+ password
		 	+ username
		 	+ avatar_url, optional
		 	+ device_token, optional
		 	+ device_platform, optional
		'''
		return super().post(ENDPOINTS['login_register'], payloads)