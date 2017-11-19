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
		@params:
			- base_url, string - required
			- app_secret, string - required
		@return -
		"""
		self.base_url = 'https://' + base_url + API_BASE_URI
		self.headers = {
			'Accept': 'application/json',
			'Content-Type': 'application/json',
			'qiscus_sdk_secret': app_secret
		}

	def login_register(self, payloads):
		"""Login and register method.
		@params:
			- payloads, dict - required
				+ email, string - required
				+ password, string - required
				+ username, string - required
				+ avatar_url, string - optional
				+ device_token, string - optional
				+ device_platform, string - optional
		@return user profile information, dict
		"""
		return self.post(endpoint=ENDPOINTS['login_register'], payloads=payloads)

	def get_user_profile(self, user_email):
		"""Get user profile information by email.
		@params:
			- user_email, string - required
		@return user_profile information, dict
		"""
		query = {
			'user_email': user_email
		}
		return self.get(endpoint=ENDPOINTS['user_profile'], query=query)

	def reset_user_token(self, user_email):
		"""Reset user token.
		@params:
			- user_email, string - required
		@return user profile information, dict
		"""
		payloads = {
			'user_email': user_email
		}
		return self.post(endpoint=ENDPOINTS['reset_user_token'], payloads=payloads)
