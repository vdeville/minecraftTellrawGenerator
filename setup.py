from setuptools import setup
from os import path

with open(path.join(path.abspath(path.dirname(__file__)), 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='minecraftTellrawGenerator',
    version='1.0.2',
    description='Easily create minecraft tellraw command',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/MyTheValentinus/minecraftTellrawGenerator',
    author='Valentin DEVILLE',
    author_email='contact@valentin-deville.eu',
    keywords='minecraft tellraw command',
    python_requires='~=3.3',
    packages=['minecraftTellrawGenerator'],
    project_urls={
        'Bug Reports': 'https://github.com/MyTheValentinus/minecraftTellrawGenerator/issues',
        'Donation': 'https://www.paypal.me/ValentinDeville',
        'Source': 'https://github.com/MyTheValentinus/minecraftTellrawGenerator',
    },
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Topic :: Software Development :: Build Tools',
        'Natural Language :: French',
        'Programming Language :: Python :: 3 :: Only',
        'Topic :: Utilities'
    ],
)
