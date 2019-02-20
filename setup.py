import setuptools

with open('README.md', 'r', encoding='utf-8') as fh:
    long_description = fh.read()

setuptools.setup(
    name='coinpaprika-client',
    author='coinpaper.io',
    version = '1.1.2',
    author_email='contact@coinpaper.io',
    description='Coinpaprika API client written in Python',
    keywords='coinpaprika, api, wrapper, client, python',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://coinpaper.io',
    project_urls={
        'Coinpaprika API': 'https://api.coinpaprika.com',
        'Coinpaper.io': 'https://coinpaper.io',
        'Source Code': 'https://github.com/coinpaper/coinpaprika-api-python-client',
    },
    package_dir={'': 'src'},
    packages=setuptools.find_packages(where='src'),
    classifiers=[
        'Development Status :: 5 - Production/Stable',

        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',

        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3 :: Only',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
    install_requires=[
        'requests'
    ],
)