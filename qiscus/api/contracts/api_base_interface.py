from abc import ABCMeta, abstractmethod


class ApiBaseInterface(metaclass=ABCMeta):

	'''
	contract on qiscus api call
		methods:
			+ request(endpoint [required])
	'''
	@abstractmethod
	def get(self, endpoint, query=[]):
		'''
		send GET request to qiscus_base_url + $endpoint
		'''
		pass

	@abstractmethod
	def post(self, endpoint, payloads):
		'''
		send POST request to qiscus_base_url + $endpoint
		'''
		pass
