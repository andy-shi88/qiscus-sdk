import requests # noqa
from .contracts.api_base_interface import ApiBaseInterface


class ApiBase(ApiBaseInterface):
	"""API call base class.
	storing base methods for requesting to api
	"""

	def __init__(self):
		"""Default API base class constructor."""
		pass

	def get(self, endpoint, query={}):
		"""Default get method doc in the interface."""
		return self.request(
			requests.get(
				self.base_url + endpoint,
				params=query,
				headers=self.headers
			)
		)

	def post(self, endpoint, payloads):
		"""Default post method doc in the interface."""
		return self.request(
			requests.post(
				self.base_url + endpoint,
				headers=self.headers,
				json=payloads
			)
		)

	def request(self, request_call):
		"""Request call to self.endpoint.
		@params:
			- request_call, callback - required
		"""
		try:
			result = request_call
			return result.json()
		except requests.exceptions.Timeout as e:
			raise Exception(e)
		except requests.exceptions.TooManyRedirects as e:
			raise Exception(e)
		except requests.exceptions.RequestException as e:
			raise Exception(e)
