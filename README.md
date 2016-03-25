# sourcemon

[![Build Status](https://travis-ci.org/michaelimfeld/sourcemon.svg?branch=master)](https://travis-ci.org/michaelimfeld/sourcemon)

Sourcemon is a web-based monitoring tool for valve source servers (like CS:GO or Garry's Mod). It uses the [valve-python](https://github.com/Holiverh/python-valve) module to query any source server for data.

## Installation

    git clone https://github.com/michaelimfeld/sourcemon.git
    bower install
    debuild -us -uc
    dpkg -i ../sourcemon_1.0_amd64.deb

## Usage

    sudo service sourcemon start

Navigate your browser to localhost:5000 and start adding your servers!

## Debugging

For debugging you can start sourcemon manually:

    sudo su www-data -s /bin/bash
    sourcemon
