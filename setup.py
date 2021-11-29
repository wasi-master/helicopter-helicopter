from setuptools import setup, find_packages
import pathlib

here = pathlib.Path(__file__).parent.resolve()

# Get the long description from the README file
long_description = (here / 'README.md').read_text(encoding='utf-8')

setup(
    name='helikopter',
    version='1.0.3',
    description='A simple script to print a helicopter to the terminal',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/wasi-master/helicopter-helicopter',
    author='Wasi Master',
    author_email='arianmollik323@gmail.com',

    # For a list of valid classifiers, see https://pypi.org/classifiers/
    classifiers=[  # Optional
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Topic :: Games/Entertainment',
        'Topic :: Terminals',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.0',
        'Programming Language :: Python :: 3.1',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3 :: Only',
    ],
    keywords='helicopter, meme, helikopter, helicopter-helicopter, helikopter-helikopter',
    packages=['helikopter'],
    python_requires='>=3.0, <4',
    project_urls={
        'Bug Reports': 'https://github.com/wasi-master/helicopter-helicopter/issues',
        'Say Thanks!': 'https://saythanks.io/to/wasi-master',
        'Source': 'https://github.com/wasi-master/helicopter-helicopter',
    },
    package_data={
        'helikopter': ['heli_animation.txt'],
    },
)
