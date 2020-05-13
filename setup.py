from distutils.core import setup
setup(
  name = 'jpntextgen',
  packages = ['jpntextgen'],
  version = '0.1',
  license='MIT',
  description = 'The Japanese Text Generator Library use to generate the japanese general text such as name, address',
  author = 'Nero Phung',
  author_email = 'nerophung.io@gmail.com',
  url = 'https://github.com/nerophung/jpn-text-gen',
  download_url = 'https://github.com/nerophung/jpn-text-gen/archive/dev_0.1.tar.gz',    # I explain this later on
  keywords = ['Japanese', 'Generator', 'OCR'],   # Keywords that define your package best
  install_requires=[            # I get to this in a second
          'pickle',
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3.6',
  ],
)