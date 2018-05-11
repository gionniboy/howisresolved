[![Build Status](https://travis-ci.org/gionniboy/howisresolved.svg?branch=master)](https://travis-ci.org/gionniboy/howisresolved)

[![Maintainability](https://api.codeclimate.com/v1/badges/80fe92c3529f911b676b/maintainability)](https://codeclimate.com/github/gionniboy/howisresolved/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/80fe92c3529f911b676b/test_coverage)](https://codeclimate.com/github/gionniboy/howisresolved/test_coverage)

[![Updates](https://pyup.io/repos/github/gionniboy/howisresolved/shield.svg)](https://pyup.io/repos/github/gionniboy/howisresolved/)
[![Python 3](https://pyup.io/repos/github/gionniboy/howisresolved/python-3-shield.svg)](https://pyup.io/repos/github/gionniboy/howisresolved/)


# **howisresolved**
how is resolved is a little python script to resolve a domain from differents nameservers.


### **how it works**

DNS list is passed with a simple txt file.

By default it is dnslist.txt and contain six major dns.

- 1.1.1.1 - CloudFlare
- 4.2.2.1 - Level3
- 8.8.8.8 - Google
- 9.9.9.9 - Quad9
- 64.6.64.6 - Verisign
- 208.67.222.222 - OpenDNS

If the dnsfile.txt is not present the script download a list of valid nameservers from [public-dns.info](https://public-dns.info/).

An output on logfile is generated.
On cli too if debug is active. [check logging.json]

**Python3 required**.

### To the Users
Install dependencies using Pipenv.
```console
$ pipenv --three install
```

For a bit of info
```console
$ pipenv run python howisresolved.py --help
```

#### Example
```console
$ pipenv run python howisresolved.py --domain python.org --expect 23.253.135.79
$ pipenv run python howisresolved.py --domain python.org --dnsfile dnslist.txt --dnsrand 6 --expect 23.253.135.79
$ pipenv run python howisresolved.py --domain python.org --dnsrand 6 --expect 23.253.135.79

random nameserver: ['4.2.2.1', '8.8.8.8', '9.9.9.9', '1.1.1.1', '208.67.222.222', '64.6.64.6']

python.org IP 23.253.135.79 resolved by 4.2.2.1
python.org IP 23.253.135.79 resolved by 8.8.8.8
python.org IP 23.253.135.79 resolved by 9.9.9.9
python.org IP 23.253.135.79 resolved by 1.1.1.1
python.org IP 23.253.135.79 resolved by 208.67.222.222
python.org IP 23.253.135.79 resolved by 64.6.64.6
```

## To Contributors
Install dev dipendencies to avoid useless issues.

```console
$ pipenv --three install -d
```

To launch tests with coverage
```console
$ pipenv run pytest -v --cov=./
```

or use pipenv shortcut
```console
$ pipenv run tests
```

issue&&PR || GTFO

enjoy.

## **Authors**

* **GB 'firegarden' Pullarà** - [firegarden](https://firegarden.co)

See also the list of [contributors](https://github.com/gionniboy/howisresolved/contributors) who participated in this project.


### **License**
This project is licensed under the BSD 3-Clause License - see the [LICENSE](LICENSE) file for details
