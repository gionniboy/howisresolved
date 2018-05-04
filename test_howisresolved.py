#!/usr/bin/env python

import os
#from unittest.mock import patch
import pytest
import howisresolved


def test_setup_logging():
    """ test logging.json configuration """
    assert howisresolved.setup_logging() is True


def test_setup_logging_missing():
    """ test missing logging.json configuration """
    with pytest.raises(SystemExit) as err:
        howisresolved.setup_logging(filepath="logging.test")
    assert 'Create logging.json config file and restart.' in str(err.value)


def test_download_publicdns():
    """ test download publicdns list """
    dnsfile = './dnslist.test'
    assert howisresolved.download_publicdns(dnsfile) is None
    os.remove(dnsfile)


# def test_download_publicdns_mocked():
#     """ test download publicdns list """
#     dnsfile = './dnslist.test'
#     with patch('requests.get') as mocked_get:
#         print(mocked_get)
#         mocked_get.return_value.ok = True
#         mocked_get.return_value.text = 'Success'

#         data = 'https://public-dns.info/nameservers.txt'
#         mocked_get.assert_called_with(data)
#         assert (data == 'https://public-dns.info/nameservers.txt') is True

#         mocked_get.return_value.ok = False

#         data = dnsfile
#         mocked_get.assert_called_with(
#             'https://public-dns.info/nameservers.txt')
#         assert (data) == 'Connnection Error'

#     #os.remove(dnsfile)


if __name__ == '__main__':
    pytest.main()
