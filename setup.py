from setuptools import setup, find_packages

setup(
    name = 'django-vellum',
    version = '0.1',
    description = 'A web log for Django.',
    long_description = open('README.md').read(),
    url = 'https://github.com/pigmonkey/django-vellum',
    author = 'Pig Monkey',
    author_email = 'pm@pig-monkey.com',

    packages = find_packages(),
    zip_safe=False,
)
