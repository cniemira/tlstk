import os

from distutils.core import setup
from setuptools import find_packages

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.md')).read()
CHANGES = open(os.path.join(here, 'CHANGES.md')).read()

requirements = [
    "click >= 6.7",
    "x509 >= 0.1",
    ]

setup(
    name='tlstk',
    version='0.0',
    description='TLS ToolKit for Python and CLI',
    url='https://github.com/cniemira/tlstk',
    author='CJ Niemira',
    author_email='siege@siege.org',
    license='MIT',
    long_description=README + '\n\n' + CHANGES,
    packages=find_packages(),
    install_requires=requirements,
    entry_points={
        'console_scripts': [
            'tls = tlstk.cli:tls'
        ]
    },
    classifiers=[
        "Development Status :: 1 - Planning",
        "Environment :: Console",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: C",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3 :: Only",
        "Topic :: Security :: Cryptography"
    ],
    test_requires=requirements,
    test_suite='tlstk.test',
    zip_safe=False,
)
