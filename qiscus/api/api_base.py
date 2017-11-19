import requests
from .contracts.api_base_interface import ApiBaseInterface


class ApiBase(ApiBaseInterface):

	def __init__(self):
		pass

	def get(self, endpoint, query={}):
		return self.request(
			requests.get(
				self.base_url + endpoint, 
		    	params=query, 
		    	headers=self.headers
			)
		)

	def post(self, endpoint, payloads):
		return self.request(
			requests.post(
				self.base_url + endpoint,
				headers=self.headers,
				json=payloads
			)
		)

	def request(self, request_call):
		'''
		request(request_call [callback])
		request call to self.endpoint
		'''
		try:
			result = request_call
			return result.json()
		except requests.exceptions.Timeout as e:
			raise Exception(e)
		except requests.exceptions.TooManyRedirects as e:
			raise Exception(e)
		except requests.exceptions.RequestException as e:
			raise Exception(e)
