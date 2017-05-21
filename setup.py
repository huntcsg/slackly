from setuptools import setup, find_packages

setup(
    name='slackly',
    version='1.0.0',
    install_requires=[
        'requests',
        'websocket-client',
    ],
    zip_safe=True,
    package_dir={
        '': 'src',
    },
    packages=find_packages('src'),
)