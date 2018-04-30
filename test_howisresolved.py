#!/usr/bin/env python

import os
#from unittest.mock import patch
import pytest
import howisresolved

def test_validate_domain_ok():
    """ test domain validation ok"""
    domain = 'python.org'
    assert howisresolved.validate_domain(domain) is None


def test_validate_domain_exit():
    """ test domain validation exit """
    domain = 'python.org@it'
    with pytest.raises(SystemExit) as err:
        howisresolved.validate_domain(domain)
    assert 'Invalid domain specified.' in str(err.value)

def test_validate_ip_ok():
    """ test ip validation ok"""
    ip = '1.1.1.1'
    assert howisresolved.validate_ip(ip) is None

def test_validate_ip_exit():
    """ test ip validation exit """
    ip = '1.1'
    with pytest.raises(SystemExit) as err:
        howisresolved.validate_ip(ip)
    assert 'Invalid ip specified.' in str(err.value)


def test_download_publicdns():
    """ test download publicdns list """
    dnsfile = './dnslist.test'
    assert howisresolved.download_publicdns(dnsfile) is None
    os.remove(dnsfile)


# def test_download_publicdns_mocked():
#     """ test download publicdns list """
#     dnsfile = './dnslist.test'
#     with patch('howisresolved.requests.get') as mocked_get:
#         print(mocked_get)
#         mocked_get.return_value.ok = True
#         mocked_get.return_value.text = 'Success'

#         data = dnsfile
#         mocked_get.assert_called_with(
#             'https://public-dns.info/nameservers.txt')
#         assert (data) == 'Success'

#         mocked_get.return_value.ok = False

#         data = dnsfile
#         mocked_get.assert_called_with(
#             'https://public-dns.info/nameservers.txt')
#         assert (data) == 'Connnection Error'

#     #os.remove(dnsfile)


if __name__ == '__main__':
    pytest.main()
