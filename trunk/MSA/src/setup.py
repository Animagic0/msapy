__author__="Jorge Rodr�guez Ara�jo"
__date__ ="$24-jul-2009 1:20:23$"

from setuptools import setup,find_packages

setup (
  name = 'MSA',
  version = '0.1',
  packages = find_packages(),

  # Declare your packages' dependencies here, for eg:
  install_requires=['foo>=3'],

  # Fill in these to make your Egg ready for upload to
  # PyPI
  author = 'Jorge Rodr�guez Ara�jo',
  author_email = '',

  summary = 'Just another Python package for the cheese shop',
  url = '',
  license = '',
  long_description= 'Long description of the package',

  # could also include long_description, download_url, classifiers, etc.

  
)