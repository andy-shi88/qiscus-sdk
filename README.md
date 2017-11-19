# README

### Python Qiscus SDK

#### How to:
clone the repo and install with `pip install .` as it's not on pypi yet.

import the `QiscusBuilder` by `from qiscus import QiscusBuilder`
`QiscusBuilder` will return on `Qiscus` object for you to work with

you can do `Qiscus` api call by using the `Qiscus` object
example:
```
qiscus = QiscusBuilder().set_app_id('your app id').set_app_secret('your app secret').build()
payload = {
	'email': 'your@email.com',
	'username': 'your user name',
	'password': 'password',
}
result = qiscus.login_register(payload)
``` 

The above call will come with something like this:
```
{
	'results': {
		'user': {
			'app': {
				'code': 'code', 
				'id': 1243, 
				'id_str': '1243', 
				'name': 'app name'
			}, 
			'avatar': {
				'avatar': {
					'url': 'https://d1edrlpyc25xu0.cloudfront.net/kiwari-prod/image/upload/75r6s_jOHa/1507541871-avatar-mine.png'
					}
			}, 
			'avatar_url': 'https://d1edrlpyc25xu0.cloudfront.net/kiwari-prod/image/upload/75r6s_jOHa/1507541871-avatar-mine.png', 
			'email': 'your@email.com', 
			'id': 323507, 'id_str': '323507', 
			'last_comment_id': 0, 
			'last_comment_id_str': '0', 
			'pn_android_configured': False, 
			'pn_ios_configured': False, 
			'rtKey': 'somestring', 
			'token': 'KEACQzAR8SXfDznAmqEB', 
			'username': 'your username'
		}
	}, 
	'status': 200}

```

# This is still Work in Progress
## finished functionalities and tests
- [x] login register
- [x] get user info
- [x] reset user token

## Tests
- first activate the virtual environment `. env/bin/activate`
- install the test tools requirements by running `pip install -r dev-requirements`
- run unit tests with `python setup.py test` 
- run linter test with `flake8` 