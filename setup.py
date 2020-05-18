from distutils.core import setup
from setuptools import find_packages
setup(
  name = 'jpntextgen',
  version = '2.2',
  license='MIT',
  description = 'The Japanese Text Generator Library use to generate the japanese general text such as name, address',
  author = 'Nero Phung',
  author_email = 'nerophung.io@gmail.com',
  url = 'https://github.com/nerophung/jpn-text-gen',
  download_url = 'https://github.com/nerophung/jpn-text-gen/archive/dev-2.2.tar.gz',
  keywords = ['Japanese', 'Generator', 'OCR'],
  packages = ['jpntextgen', 'jpntextgen.utils'],
  package_data={
    'data': ['address.pkl', 'email.txt', 'first_name.txt', 'last_name.txt'],
  },
  include_package_data=True,
  install_requires=[
      ],
  classifiers=[
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3.6',
  ],
)