import os
from setuptools import setup, find_packages
import sys

PY2 = sys.version_info.major == 2

here = os.path.abspath(os.path.dirname(__file__))
try:
    with open(os.path.join(here, 'README.rst')) as f:
        README = f.read()
    with open(os.path.join(here, 'CHANGES.txt')) as f:
        CHANGES = f.read()
    with open(os.path.join(here, 'AUTHORS.rst')) as f:
        AUTHORS = f.read()
except IOError:
    README = CHANGES = AUTHORS = ''


install_requires = [
    'requests',
    'websocket-client',
    'six',
]


docs_require = [
    'sphinx',
    'sphinx_rtd_theme',
]


testing_requires = [
    'pytest',
    'pytest-cov',
]

if PY2:
    install_requires.extend([
        'backports.functools_lru_cache',
    ])

    testing_requires.extend([
        'mock',
    ])


setup(
    name='slackly',
    version='1.0.1',
    description='A full featured python Slack API SDK',
    long_description="\n".join([README, CHANGES, AUTHORS]),
    author='Hunter Senft-Grupp',
    author_email='huntcsg@gmail.com',
    url='https://slackly.io',
    python_requires='>=2.7,!=3.0.*,!=3.1.*,!=3.2.*,!=3.3.*',
    install_requires=install_requires,
    extras_require={
        'docs': docs_require,
        'testing': testing_requires,
    },
    zip_safe=True,
    package_dir={
        '': 'src',
    },
    packages=find_packages('src'),
    keywords="slack slackly api sdk realtime",
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Topic :: Communications :: Chat',
        'Topic :: Office/Business',
        'Topic :: Software Development :: Libraries'
    ],
)
