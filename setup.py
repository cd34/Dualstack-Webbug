import os

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.txt')).read()
CHANGES = open(os.path.join(here, 'CHANGES.txt')).read()

requires = [
    'tornado',
    'ipaddr',
    'fabric',
    ]

setup(name='dualstack',
      version='0.0',
      description='tube',
      long_description=README + '\n\n' + CHANGES,
      classifiers=[
        "Programming Language :: Python",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
        ],
      author='',
      author_email='',
      url='',
      keywords='web wsgi ipv4 ipv6',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      test_suite='dualstack',
      install_requires=requires,
      entry_points="""\
      [paste.app_factory]
      main = dualstack:main
      """,
      )
