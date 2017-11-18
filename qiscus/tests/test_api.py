import uuid
from voluptuous import Schema, Required, Length, Url, MultipleInvalid, Invalid
from unittest import TestCase

from .constants import TEST_APP
from ..qiscus_builder import QiscusBuilder
from ..qiscus import Qiscus

class TestApi(TestCase):
	'''
	test on qiscus api call
	'''

	def setUp(self):
		'''
		setup: create qiscuss instance
		'''
		self.qiscus = QiscusBuilder().set_app_id(TEST_APP['APP_ID']).set_app_secret(TEST_APP['APP_SECRET']).build()
		self.login_register_payload = {
			'email': 'testmail@mail.com',
			'username': 'testusername',
			'password': 'testpassword'
		}
		self.login_register_fail_schema = Schema({
			Required('status'): int,
			Required('error'): {
				Required('message'): str
			}
		})
		self.login_register_success_schema = Schema({
			Required('status'): int,
			Required('results'): {
				Required('user'): {
					Required('app'): {
						Required('code'): str,
						Required('id'): int,
						Required('id_str'): str,
						Required('name'): str
					},
					Required('avatar'): {
						Required('avatar'): {
							Required('url'): str,
						}
					},
					Required('avatar_url'): str,
					Required('email'): str,
					Required('id'): int,
					Required('id_str'): str,
					Required('last_comment_id'): int,
					Required('last_comment_id_str'): str,
					Required('pn_android_configured'): bool,
					Required('pn_ios_configured'): bool,
					Required('rtKey'): str,
					Required('token'): str,
					Required('username'): str
				},
			}
		})

	def test_login_register(self):
		result = self.qiscus.login_register(self.login_register_payload)
		self.assertTrue(isinstance(result, dict))
		self.assertEquals(self.login_register_success_schema(result), result)

	def tearDown(self):
		pass
