from abc import ABCMeta, abstractmethod # noqa


class ApiBaseInterface(metaclass=ABCMeta):
	"""Contract on qiscus api call.
	methods:
		+ request(endpoint [required])
	"""

	@abstractmethod
	def get(self, endpoint, query={}):
		"""Send GET request to qiscus_base_url + $endpoint.
		@params:
			- endpoint, will be the endpoint for the request.
			- query, will be the parameter query key-value dictionary.
		"""
		pass

	@abstractmethod
	def post(self, endpoint, payloads):
		"""Send POST request to qiscus_base_url + $endpoint.
		@params:
			- endpoint, will be the endpoint for the request.
			- payloads, will be the json payload for the request.
		"""
		pass
