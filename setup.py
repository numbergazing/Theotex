from distutils.core import setup

import setuptools

with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='theotex',
    version='1.0.0',
    url='https://github.com/numbergazing/Theotex',
    project_urls={
        'Bug Tracker': 'https://github.com/numbergazing/Theotex/issues',
    },
    license='MIT',
    author='numbergazing',
    author_email='hello@numbergazing.com',
    description='A python package to get Bible verses from https://theotex.org',
    long_description=long_description,
    long_description_content_type='text/markdown',
    packages=setuptools.find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3.10',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Natural Language :: English',
        'Natural Language :: French'
    ],
    python_requires='>=3.10.4',
    py_modules=['theotex'],
    package_dir={'':'src/theothex'},
    install_requires=[]
)
