from .api.api_base import ApiBase
from .configs.constants import API_BASE_URI, ENDPOINTS


class Qiscus(ApiBase):
	"""Main qiscus class for api call.
	methods:
	- login_register(email, password, username, avatar_url, device_token,
		device_platform [optional])
	this will log user in or register them if not exist.
	"""

	def __init__(self, base_url, app_secret):
		"""Default constructor method.
		build api base url and default headers with app_secret params
		"""
		self.base_url = 'https://' + base_url + API_BASE_URI
		self.headers = {
			'Accept': 'application/json',
			'Content-Type': 'application/json',
			'qiscus_sdk_secret': app_secret
		}

	def login_register(self, payloads):
		"""Login and register method.
		login_register(payloads [required])
			- payloads consists of
				+ email
				+ password
				+ username
				+ avatar_url, optional
				+ device_token, optional
				+ device_platform, optional
		"""
		return self.post(endpoint=ENDPOINTS['login_register'], payloads=payloads)

	def get_user_profile(self, user_email):
		"""Get user profile information by email.
		get_user_profile(user_email [required])
			- get user profile info by email
				+ user_email, required.
		"""
		query = {
			'user_email': user_email
		}
		return self.get(endpoint=ENDPOINTS['user_profile'], query=query)
