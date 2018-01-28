#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# resolve a domain from different nameservers


#
# TODO: argparse instead sys.argv
# TODO: choose 10 random dns and check with all them
# TODO: option to choose how many dns pick from list
# TODO: multithreading
#

import os
import sys
import time
import random
import dns.resolver
import requests

if len(sys.argv) > 2:
    DOMAIN = sys.argv[1]
    DNSFILE = sys.argv[2]
else:
    sys.exit("Specify domain to resolve and dns file")


def download_publicdns(dnsfile):
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
    try:
        if not os.path.exists(dnsfile):
            download_publicdns(dnsfile)

        filestat = os.stat(dnsfile)
        file_age = time.time() - filestat.st_mtime
        if file_age > (86400 * 2):
            print("dns list older than 2 days: updating from public-dns")
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

    my_resolver = dns.resolver.Resolver(configure=False)
    my_resolver.nameservers = generate_dns(dnsfile)
    # use random.sample to mantain the type [list]
    secure_random = random.SystemRandom()
    my_resolver.nameservers = secure_random.sample(my_resolver.nameservers, 1)
    print("random nameserver: {}".format(str(my_resolver.nameservers)))
    try:
        my_answers = my_resolver.query(domain)
        for rdata in my_answers:
            print("{} IP: {}".format(domain, rdata))
            # return rdata
    except dns.exception.DNSException as err:
        print(err)
        sys.exit(42)


if __name__ == '__main__':
    resolve(DOMAIN, DNSFILE)
