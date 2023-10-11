import setuptools
from distutils.core import setup


setup(
    name='ytw',
    version='0.0.0',
    description='Youtube to wav',
    author='You',
    author_email='',
    packages=['ytw'],
    entry_points={
        'console_scripts': ['ytw=ytw.entry:cli_entry_point'],
    },
    install_requires=[
        'requests',
    ],
)