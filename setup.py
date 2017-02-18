#!/usr/bin/env python

import os
from setuptools import setup

import apds9960

README = open(os.path.join(os.path.dirname(__file__), 'README.rst')).read()

setup(
    name="RPi.apds9960",
    version=apds9960.__version__,
    author="Richard Hull",
    author_email="richard.hull@destructuring-bind.org",
    description="A library to drive an Avago APDS9960 gesture, proximity, ambient light and RGB color sensor over I2C",
    long_description=README,
    license="MIT",
    keywords=["raspberry pi", "orange pi", "banana pi", "rpi", "avago", "apds9960", "i2c", "gesture", "proximity", "ambient light", "RGB"],
    url="https://github.com/rm-hull/apds9960",
    download_url="https://github.com/rm-hull/apds9960/tarball/" + apds9960.__version__,
    packages=['apds9960'],
    install_requires=["smbus2"],
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Development Status :: 4 - Beta",
        "Intended Audience :: Education",
        "Intended Audience :: Developers",
        "Topic :: Education",
        "Topic :: System :: Hardware",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3"
    ]
)
