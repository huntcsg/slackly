import os
from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
try:
    with open(os.path.join(here, 'README.rst')) as f:
        readme = f.read()
    with open(os.path.join(here, 'CHANGES.txt')) as f:
        CHANGES = f.read()
except IOError:
    readme = changes = ''



install_requires = [
    'requests',
    'websocket-client',
]

docs_require = [
    'sphinx',
    'rtd_theme',
]

testing_requires = [
    'pytest',
    'pytest-cov',
    'mock',
]

setup(
    name='slackly',
    version='1.0.0',
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
)