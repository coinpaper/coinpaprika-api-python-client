from distutils.core import setup
setup(
  name = 'coinpaprika-api',         # How you named your package folder (MyLib)
  packages = ['coinpaprika-api'],   # Chose the same as "name"
  version = '1.0.0',      # Start with a small number and increase it with every change you make
  license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'Free API Wrapper for api.coinpaprika.com, provided by https://coinpaper.io',   # Give a short description about your library
  author = 'coinpaper.io',                   # Type in your name
  author_email = 'contact@coinpaper.io',      # Type in your E-Mail
  url = 'https://coinpaper.io',   # Provide either the link to your github or to your website
  download_url = 'https://github.com/coinpaper/coinpaprika-api-python-client/archive/v_1.tar.gz',    # I explain this later on
  keywords = ['coinpaprika', 'api', 'wrapper'],   # Keywords that define your package best
  install_requires=[            # I get to this in a second
          'requests',
      ],
  classifiers=[
      'Programming Language :: Python :: 3',
      'License :: OSI Approved :: MIT License',
      'Operating System :: OS Independent',
      'Intended Audience :: Developers',
      'Topic :: Software Development :: Libraries :: Python Modules',
  ],
)