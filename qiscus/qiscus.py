from .api.api_base import ApiBase # noqa
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

	def login_register(
		self, email, password, username,
		avatar_url=None,
		device_token=None,
		device_platform=None):
		"""Login and register method.
		@params:
			- email, string - required
			- password, string - required
			- username, string - required
			- avatar_url, string - optional
			- device_token, string - optional
			- device_platform, string - optional
		@return user profile information, dict
		"""
		payloads = {
			'email': email,
			'password': password,
			'username': username,
			'avatar_url': avatar_url,
			'device_token': device_token,
			'device_platform': device_platform
		}
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

	def get_user_rooms(
		self, user_email, page=1,
		show_participants=False, room_type=None):
		"""Get user room list.
		@params:
			- user_email, string - required
			- page, int - optional {default=0} [page number for the list,
				20 rows per page]
			- show_participants, bool - optional {default=False}
			- room_type, string - optional {default=None}, opt=[single, group]
		@return list of rooms depends on what information is included by params
		"""
		query = {
			'user_email': user_email,
			'page': page,
			'show_participants': show_participants,
			'room_type': room_type
		}
		return self.get(endpoint=ENDPOINTS['get_user_rooms'], query=query)

	def create_room(
		self, name, participants,
		creator, avatar_url=None):
		"""Create user room and put participants into it.
		@params:
			- name: string - required.
			- participants: list - required.
			- creator: string - required.
			- avatar_url: string - optional.
		@return dict, created room information and its participants.
		"""
		payloads = {
			'name': name,
			'participants': participants,
			'creator': creator,
			'avatar_url': avatar_url
		}
		return self.post(endpoint=ENDPOINTS['create_room'], payloads=payloads)

	def update_room(
		self, user_email, room_id, room_name=None,
		room_avatar_url=None, options=None):
		"""Update room information.
		@params:
			- user_email: string - required
			- room_id: string - required
			- room_name: string - optional
			- room_avatar_url: string - optional
			- options: string - optional
		"""
		payloads = {
			'user_email': user_email,
			'room_id': room_id,
			'room_name': room_name,
			'room_avatar_url': room_avatar_url,
			'options': options
		}
		return self.post(endpoint=ENDPOINTS['update_room'], payloads=payloads)
