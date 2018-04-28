#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# resolve a domain from different nameservers

__author__ = "GB Pullarà"
__copyright__ = "Copyright 2018"
__credits__ = ["joeyrs"]
__license__ = "BSD-3clause"
__version__ = "0.2.3"
__maintainer__ = "gionniboy"
__email__ = "giovbat@gmail.com"
__status__ = "Development"


import os
import sys
import re
import time
import random
import argparse

import json
import logging
import logging.config

import dns.resolver
import requests


# istanziate logger
LOGGER = logging.getLogger(__name__)


def setup_logging(filepath="logging.json", log_level=logging.INFO):
    """ setup logging based on json dict

    :param filepath: filename
    :param type: string

    """
    if not os.path.exists(filepath):
        LOGGER.error('no logging config file founded.')
        sys.exit('Create logging.json config file and restart.')

    with open(filepath, 'r') as fileconfig:
        config = json.load(fileconfig)
    logging.config.dictConfig(config)
    LOGGER.info('LOGGING SETUP from JSON %s', filepath)

    LOGGER.debug('LOGGING OK - path %s - level %s', filepath, log_level)


def validate_domain(domain):
    """Check if the argument is a syntax-valid domain.

    :param domain: domain string from positional arg
    :param type: string

    :return: validate or exit
    """
    domain_regex = re.compile(
        r'^(?=.{4,255}$)([a-zA-Z0-9][a-zA-Z0-9-]{,61}[a-zA-Z0-9]\.)+[a-zA-Z0-9]{2,5}$')
    if not domain_regex.match(domain):
        sys.exit("Invalid domain specified.")


def download_publicdns(dnsfile):
    """Download valid nameservers list from public-dns.info

    :param dnsfile: filename
    :param type: string from position arg

    :return: a list of nameservers and a file on disk
    :rtype: list
    """
    try:
        url = 'https://public-dns.info/nameservers.txt'
        data = requests.get(url)
        open(dnsfile, 'wb').write(data.content)
        LOGGER.debug("file saved on disk %s", dnsfile)
    except requests.exceptions.ConnectionError as err:
        LOGGER.error(err)
        sys.exit('connection error')
    except PermissionError as err:
        LOGGER.error(err)
        sys.exit('permission error')
    except IOError as err:
        LOGGER.error(err)
        sys.exit('IO error')


def generate_dns(dnsfile):
    """Generate dns list
    by default it download a valid nameserver list from https://public-dns.info/
    and write it on file
    or you can pass a dns list throught a txt file to it

    :param dnsfile: txt file with dns list
    :type dnsfile: string

    :return: a list of nameservers
    :rtype: list
    """
    try:
        if not os.path.exists(dnsfile):
            download_publicdns(dnsfile)

        filestat = os.stat(dnsfile)
        file_age = time.time() - filestat.st_mtime
        if file_age > (86400 * 3):
            LOGGER.info("dns list older than 3 days: delete it if you want update it automatically")

        with open(dnsfile, 'r') as nameserver:
            dnslist = [line.rstrip() for line in nameserver]
            return dnslist

    except PermissionError as err:
        LOGGER.error(err)
        sys.exit('permission error')
    except IOError as err:
        LOGGER.error(err)
        sys.exit('IO error')


def resolve(domain, dnsfile, dnsrand):
    """Resolve domain

    :param domain: domain.tld to be resolved
    :type domain: string from positional args

    :param dnsfile: filename.txt
    :type dnsfile: list from positional args

    :param dnsrand: number of dns to use
    :type dnsrand: int

    :return: domain resolved with specified nameserver
    :rtype: string
    """
    validate_domain(domain)
    my_resolver = dns.resolver.Resolver(configure=False)
    my_resolver.nameservers = generate_dns(dnsfile)
    # use random.sample to mantain the type [list]
    secure_random = random.SystemRandom()
    my_resolver.nameservers = secure_random.sample(my_resolver.nameservers, dnsrand)
    LOGGER.info("random nameserver: %s", str(my_resolver.nameservers))
    try:
        for nameserver in my_resolver.nameservers:
            my_answers = my_resolver.query(domain)
            for rdata in my_answers:
                LOGGER.info("%s IP %s resolved by %s", domain, rdata, nameserver)
                # return rdata
    except dns.exception.DNSException as err:
        LOGGER.error("DNSException %s", err)
        sys.exit(42)


def main():
    """ main """
    parser = argparse.ArgumentParser(
        description='Check domain with different nameservers.',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('--domain', type=str, help="Domain to check.")
    parser.add_argument('--dnsfile', default="./dnslist.txt", type=str, help='Dnsfile text to read nameservers from.')
    parser.add_argument('--dnsrand', default=6, type=int, help='how many ns pick from list and test.')
    args = parser.parse_args()

    DOMAIN = args.domain
    DNSFILE = args.dnsfile
    DNSRAND = args.dnsrand

    try:
        resolve(DOMAIN, DNSFILE, DNSRAND)
    except KeyboardInterrupt:
        print("interrupted, stopping ...")
        sys.exit(42)


if __name__ == '__main__':
    setup_logging()
    main()
