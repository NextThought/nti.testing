from setuptools import setup, find_packages
import codecs

VERSION = '0.0.0'

entry_points = {
}

setup(
    name = 'nti.testing',
    version = VERSION,
    author = 'Jason Madden',
    author_email = 'jason@nextthought.com',
    description = "Support for testing code",
    long_description = codecs.open('README.rst', encoding='utf-8').read(),
    license = 'Proprietary',
    keywords = 'nose testing',
    url = 'https://github.com/NextThought/nti.testing',
    classifiers = [
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Operating System :: OS Independent',
		'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Topic :: Software Development :: Testing'
        ],
	packages=find_packages('src'),
	package_dir={'': 'src'},
	namespace_packages=['nti'],
	install_requires=[
		'setuptools',
		'nose',
		'pyhamcrest',
		'fudge',
		'zope.testing',
		'transaction',
		'persistent',
		'zope.interface',
		'zope.schema',
		'zope.annotation',
		'zope.component',
		'zope.configuration',
		'zope.dottedname',
		'zope.site',
	],
	entry_points=entry_points
)
