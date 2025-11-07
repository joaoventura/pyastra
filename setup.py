"""
Author: João Ventura <joaojonesventura@gmail.com>

"""

from setuptools import setup
from setuptools import find_packages

setup(
    # Project
    name='pyastra',
    version='0.3.0',

    # Sources
    packages=find_packages(),
    package_data={
        'pyastra': [
            'resources/README.md',
            'resources/swefiles/*'
        ],
    },

    # Dependencies
    install_requires=['pyswisseph==2.10.3.2'],

    # Metadata
    description='Python library for Traditional Astrology',
    url='https://github.com/joaoventura/pyastra',
    keywords=['Astrology', 'Traditional Astrology'],
    license='MIT',

    # Authoring
    author='João Ventura',
    author_email='joaojonesventura@gmail.com',

    # Classifiers
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Development Status :: 4 - Beta',
        'Environment :: Other Environment',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
