import uuid, random
from unittest import TestCase
from voluptuous import Schema, Required, Length, Url, MultipleInvalid, Invalid

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
		self.qiscus_fail = QiscusBuilder().set_app_id(str(uuid.uuid4())).set_app_secret(str(uuid.uuid4())).build()
		'''
		setup: payload
		'''
		self.login_register_payload = {
			'email': 'testmail@mail.com',
			'username': 'testusername',
			'password': 'testpassword'
		}
		'''
		setup: expected response schema
		'''
		self.login_register_fail_schema = Schema({
			Required('status'): int,
			Required('error'): {
				Required('message'): str
			}
		})
		self.invalid_payload_schema = Schema({
			Required('status'): int,
			Required('error'): {
				Required('detailed_messages'): list,
				Required('errors'): dict,
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
		self.assertEqual(result['status'], 200)
		self.assertEqual(self.login_register_success_schema(result), result)
		'''
		remove password some required payload here and there
		'''
		invalid_payload = self.login_register_payload.copy()
		tobe_removed_key = random.choice(list(invalid_payload.keys())) 
		del invalid_payload[tobe_removed_key]
		result = self.qiscus.login_register(invalid_payload)
		self.assertTrue(isinstance(result, dict))
		self.assertEqual(result['status'], 400)
		self.assertEqual(self.invalid_payload_schema(result), result)

	def test_login_register_fail_app(self):
		result = self.qiscus_fail.login_register(self.login_register_payload)
		self.assertTrue(isinstance(result, dict))
		self.assertEqual(result['status'], 400)
		self.assertEqual(self.login_register_fail_schema(result), result)

	def test_get_user_profile(self):
		'''
		get user profile will return the same structure as login_register
		'''
		result = self.qiscus.get_user_profile(self.login_register_payload['email'])
		self.assertTrue(isinstance(result, dict))
		self.assertEqual(result['status'], 200)
		self.assertEqual(self.login_register_success_schema(result), result)
		'''
		not registered email test
		'''
		notfound_result = self.qiscus.get_user_profile('damn@it.com')
		self.assertTrue(isinstance(notfound_result, dict))
		self.assertEqual(notfound_result['status'], 404)
		self.assertEqual(self.login_register_fail_schema(notfound_result), notfound_result) 
		'''
		invalid payload test
		'''
		invalidpayload_result = self.qiscus.get_user_profile(None)
		self.assertTrue(isinstance(invalidpayload_result, dict))
		self.assertEqual(invalidpayload_result['status'], 400)
		self.assertEqual(self.invalid_payload_schema(invalidpayload_result), invalidpayload_result) 
		
	def tearDown(self):
		pass
