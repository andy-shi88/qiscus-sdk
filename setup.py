from setuptools import setup

setup(name='qiscus-sdk',
	version='0.1.0',
	description='qiscus sdk for easily interact with qiscus api',
	keywords='python qiscus sdk',
	url='',
	author='andy-shi88',
	author_email='shi88.andy@gmail.com',
	license='',
	packages=['qiscus'],
	install_requires=[
          'requests'
    ],
    test_suite='nose.collector',
    test_requires=['nose'],
	zip_safe=False)
