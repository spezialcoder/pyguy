from distutils.core import setup
setup(
  name = 'pyguy',
  packages = ['pyguy'],
  version = '0.1',
  license='unlicense',
  description = 'Python libary for handle Person data',
  author = 'Lewin Sorg',
  author_email = 'developermind405@gmail.com',
  url = 'https://github.com/Spezialcoder/pyguy',
  download_url = 'https://github.com/spezialcoder/pyguy/archive/master.zip',
  keywords = ['Person data'],
  install_requires=[
          'datetime'
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',

    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',

    'License :: OSI Approved :: unlicense',

    'Programming Language :: Python :: 2.7',
  ],
)
