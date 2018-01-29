#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# resolve a domain from different nameservers

__author__ = "GB Pullarà"
__copyright__ = "Copyright 2018"
__credits__ = ["joeyrs"]
__license__ = "BSD-3clause"
__version__ = "0.1.0"
__maintainer__ = "gionniboy"
__email__ = "giovbat@gmail.com"
__status__ = "Development"

#
# TODO: argparse instead sys.argv
# TODO: choose 10 random dns and check with all them
# TODO: option to choose how many dns pick from list
# TODO: multithreading
#

import os
import re
import sys
import time
import random
import dns.resolver
import requests


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
        print("file saved on disk {}".format(dnsfile))
    except requests.exceptions.ConnectionError as err:
        print(err)
        sys.exit('connection error')
    except PermissionError as err:
        print(err)
        sys.exit('permission error')
    except IOError as err:
        print(err)
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
        if file_age > (86400 * 2):
            print("dns list older than 2 days: updating from public-dns.info")
            download_publicdns(dnsfile)

        with open(dnsfile, 'r') as ns:
            dnslist = [line.rstrip() for line in ns]
            return dnslist

    except PermissionError as err:
        print(err)
        sys.exit('permission error')
    except IOError as err:
        print(err)
        sys.exit('IO error')


def resolve(domain, dnsfile):
    """Resolve domain

    :param domain: domain.tld to be resolved
    :type domain: string from positional args

    :param dnsfile: filename.txt
    :type dnsfile: list from positional args

    :return: domain resolved with specified nameserver
    :rtype: string
    """

    validate_domain(DOMAIN)
    my_resolver = dns.resolver.Resolver(configure=False)
    my_resolver.nameservers = generate_dns(dnsfile)
    # use random.sample to mantain the type [list]
    secure_random = random.SystemRandom()
    my_resolver.nameservers = secure_random.sample(my_resolver.nameservers, 1)
    try:
        print("random nameserver: {}".format(str(my_resolver.nameservers)))
        my_answers = my_resolver.query(domain)
        for rdata in my_answers:
            print("{} IP: {}".format(domain, rdata))
            # return rdata
    except dns.exception.DNSException as err:
        print(err)
        sys.exit(42)


if __name__ == '__main__':
    if len(sys.argv) > 2:
        DOMAIN = sys.argv[1]
        DNSFILE = sys.argv[2]
    else:
        sys.exit("Specify domain to resolve and dns file")

    resolve(DOMAIN, DNSFILE)
