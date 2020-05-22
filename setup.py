#!/usr/bin/env python

from setuptools import setup
from djangocms_twitter import __version__


CLASSIFIERS = [
    'Development Status :: 4 - Beta',
    'Environment :: Web Environment',
    'Framework :: Django',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: BSD License',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Topic :: Communications',
    'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    'Topic :: Internet :: WWW/HTTP :: Dynamic Content :: Message Boards',
    'Framework :: Django',
    'Framework :: Django :: 1.11',
    'Framework :: Django :: 2.2',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
]

setup(
    name='djangocms-twitter',
    version=__version__,
    description='Twitter plugin for django CMS',
    author='Nephila s.a.s.',
    author_email='web@nephila.it',
    url='https://github.com/nephila/djangocms_twitter',
    packages=['djangocms_twitter', 'djangocms_twitter.migrations'],
    install_requires=[
        'django-cms>=3.0',
        'django-colorfield',
    ],
    license='LICENSE.txt',
    platforms=['OS Independent'],
    classifiers=CLASSIFIERS,
    long_description=open('README.rst').read(),
    include_package_data=True,
    zip_safe=False
)
