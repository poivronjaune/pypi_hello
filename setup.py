# setup.py

from setuptools import setup, find_packages

setup(
    name='hellopj',
    version='0.1',
    packages=find_packages(),
    description='A simple pj package that says Hello Package',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='PoivronJaune',
    author_email='poivronjaune+pypi@gmail.com',
    url='https://github.com/poivronjaune/pypi_hello',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
