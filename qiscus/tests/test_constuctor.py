import uuid
from unittest import TestCase

from ..qiscus_builder import QiscusBuilder
from ..qiscus import Qiscus

class TestConstructor(TestCase):
	'''
	test on qiscus object constuction
	'''

	def test_qiscus_builder(self):
		'''
		test for qiscus builder
		'''
		qiscus = QiscusBuilder().set_app_id(str(uuid.uuid4())).set_app_secret(str(uuid.uuid4())).build()
		self.assertTrue(isinstance(qiscus, Qiscus))
