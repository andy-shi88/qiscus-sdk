import uuid # noqa
import random # noqa
from unittest import TestCase
from voluptuous import Schema, Required

from .constants import TEST_APP
from ..qiscus_builder import QiscusBuilder


class TestApi(TestCase):
	"""Test on qiscus api call."""

	def setUp(self):
		"""Setup call.
		setup: create qiscuss instance
		"""
		self.qiscus = QiscusBuilder().set_app_id(TEST_APP['APP_ID']).set_app_secret(
			TEST_APP['APP_SECRET']).build()
		self.qiscus_fail = QiscusBuilder().set_app_id(
			str(uuid.uuid4())).set_app_secret(str(uuid.uuid4())).build()
		"""Setup: payload """
		self.login_register_payload = {
			'email': 'testmail@mail.com',
			'username': 'testusername',
			'password': 'testpassword'
		}
		"""Setup: expected response schema"""
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
		self.room_success_schema = Schema({
			Required('results'): {
				Required('meta'): {
					Required('current_page'): int,
					Required('total_room'): int
				},
				Required('rooms_info'): [
					{
						'is_removed': bool,
						'last_comment_id': int,
						'last_comment_id_str': str,
						'last_comment_message': str,
						'last_comment_sender_email': str,
						'last_comment_sender_id': int,
						'last_comment_sender_id_str': str,
						'last_comment_sender_username': str,
						'last_comment_timestamp': str,
						'last_comment_timestamp_unix': int,
						'raw_room_name': str,
						'room_avatar_url': str,
						'room_unique_id': str,
						'room_id': int,
						'room_id_str': str,
						'room_options': str,
						'room_name': str,
						'room_type': str,
						'unread_count': int
					}
				]
			},
			Required('status'): int
		})
		self.room_created_schema = Schema({
			Required('results'): {
				Required('creator'): str,
				Required('participants'): list,
				Required('room_id'): int,
				Required('room_name'): str,
				Required('room_type'): str
			},
			Required('status'): int
		})

	def test_login_register(self):
		"""Test login and register method call."""
		result = self.qiscus.login_register(
			email=self.login_register_payload['email'],
			password=self.login_register_payload['password'],
			username=self.login_register_payload['username'])
		self.assertTrue(isinstance(result, dict))
		self.assertEqual(result['status'], 200)
		self.assertEqual(self.login_register_success_schema(result), result)
		"""Remove password some required payload here and there"""
		result = self.qiscus.login_register(
			email=self.login_register_payload['email'],
			password=self.login_register_payload['password'],
			username=None)
		self.assertTrue(isinstance(result, dict))
		self.assertEqual(result['status'], 400)
		self.assertEqual(self.invalid_payload_schema(result), result)

	def test_login_register_fail_app(self):
		"""Test login and register failure call."""
		result = self.qiscus_fail.login_register(
			email=self.login_register_payload['email'],
			password=self.login_register_payload['password'],
			username=self.login_register_payload['username'])
		self.assertTrue(isinstance(result, dict))
		self.assertEqual(result['status'], 400)
		self.assertEqual(self.login_register_fail_schema(result), result)

	def test_get_user_profile(self):
		"""Get user profile will return the same structure as login_register."""
		result = self.qiscus.get_user_profile(self.login_register_payload['email'])
		self.assertTrue(isinstance(result, dict))
		self.assertEqual(result['status'], 200)
		self.assertEqual(self.login_register_success_schema(result), result)
		"""Not registered email test."""
		notfound_result = self.qiscus.get_user_profile('damn@it.com')
		self.assertTrue(isinstance(notfound_result, dict))
		self.assertEqual(notfound_result['status'], 404)
		self.assertEqual(self.login_register_fail_schema(
			notfound_result), notfound_result)
		"""Invalid payload test"""
		invalidpayload_result = self.qiscus.get_user_profile(None)
		self.assertTrue(isinstance(invalidpayload_result, dict))
		self.assertEqual(invalidpayload_result['status'], 400)
		self.assertEqual(self.invalid_payload_schema(
			invalidpayload_result), invalidpayload_result)

	def test_reset_user_token(self):
		"""Reset user token test."""
		result = self.qiscus.reset_user_token(self.login_register_payload['email'])
		self.assertTrue(isinstance(result, dict))
		self.assertEqual(result['status'], 200)
		self.assertEqual(self.login_register_success_schema(result), result)
		"""Not registered email test."""
		notfound_result = self.qiscus.reset_user_token('damn@it.com')
		self.assertTrue(isinstance(notfound_result, dict))
		self.assertEqual(notfound_result['status'], 400)
		self.assertEqual(self.invalid_payload_schema(
			notfound_result), notfound_result)
		"""Invalid payload test"""
		invalidpayload_result = self.qiscus.reset_user_token(None)
		self.assertTrue(isinstance(invalidpayload_result, dict))
		self.assertEqual(invalidpayload_result['status'], 400)
		self.assertEqual(self.invalid_payload_schema(
			invalidpayload_result), invalidpayload_result)

	def test_get_rooms(self):
		"""Get user rooms tests."""
		result = self.qiscus.get_user_rooms(
			user_email=self.login_register_payload['email'])
		self.assertTrue(isinstance(result, dict))
		self.assertEqual(result['status'], 200)
		self.assertEqual(self.room_success_schema(result), result)
		"""Not registered email test."""
		notfound_result = self.qiscus.get_user_rooms('damn@it.com')
		self.assertTrue(isinstance(notfound_result, dict))
		self.assertEqual(notfound_result['status'], 400)
		self.assertEqual(self.invalid_payload_schema(
			notfound_result), notfound_result)
		"""Invalid payload test"""
		invalidpayload_result = self.qiscus.get_user_rooms(None)
		self.assertTrue(isinstance(invalidpayload_result, dict))
		self.assertEqual(invalidpayload_result['status'], 400)
		self.assertEqual(self.invalid_payload_schema(
			invalidpayload_result), invalidpayload_result)

	def create_rooms(self):
		"""Create room tests."""
		result = self.qiscus.create_room(
			name=str(uuid.uuid4()),
			participants=[self.login_register_payload['email']],
			creator='andy.developmode@gmail.com')
		self.assertTrue(isinstance(result, dict))
		self.assertEqual(result['status'], 200)
		self.assertEqual(self.room_created_schema(result), result)
		"""Not registered email test."""
		notfound_result = self.qiscus.create_room(
			name='thiswillfail',
			participants=['damn@it.com'],
			creator='darn@it.com')
		self.assertTrue(isinstance(notfound_result, dict))
		self.assertEqual(notfound_result['status'], 400)
		self.assertEqual(self.invalid_payload_schema(
			notfound_result), notfound_result)
		"""Invalid payload test"""
		invalidpayload_result = self.qiscus.create_room(
			name=None,
			participants=[],
			creator=None)
		self.assertTrue(isinstance(invalidpayload_result, dict))
		self.assertEqual(invalidpayload_result['status'], 400)
		self.assertEqual(self.invalid_payload_schema(
			invalidpayload_result), invalidpayload_result)

	def tearDown(self):
		"""Teardown call."""
		pass
