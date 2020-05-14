from distutils.core import setup
from setuptools import find_packages
setup(
  name = 'jpntextgen',
  version = '2.0',
  license='MIT',
  description = 'The Japanese Text Generator Library use to generate the japanese general text such as name, address',
  author = 'Nero Phung',
  author_email = 'nerophung.io@gmail.com',
  url = 'https://github.com/nerophung/jpn-text-gen',
  download_url = 'https://github.com/nerophung/jpn-text-gen/archive/dev-2.0.tar.gz',
  keywords = ['Japanese', 'Generator', 'OCR'],
  packages = ['jpntextgen', 'jpntextgen.utils'],
  pakage_data={
    'data': ['address.pkl', 'email.txt', 'first_name.txt', 'last_name.txt'],
  },
  include_package_data=True,
  install_requires=[
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3.6',
  ],
)