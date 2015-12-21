# sourcemon
Sourcemon is a web-based monitoring tool for valve source servers. It uses the [valve-python](https://github.com/Holiverh/python-valve) module to query any source server for data.
## Installation

    git clone https://github.com/michaelimfeld/sourcemon.git
    bower install
    debuild -us -uc
    dpkg -i ../sourcemon_1.0_amd64.deb

## Usage

    sudo su www-data -s /bin/bash
    cd /var/www/sourcemon
    python main.py
