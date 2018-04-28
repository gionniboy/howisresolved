# howisresolved
how is resolved is a little python script to resolve a domain from differents nameservers.

DNS list is passed with a simple txt file.
If not present the script download a list of valid nameservers from [public-dns.info](https://public-dns.info/).

An output on logfile is generated.
On cli too if debug is active. [check logging.json]

**Python3 required**.

Install requirements.txt for dependencies [dnspython, requests].

Use requirements-dev.txt if you want to contribute to [really appreciate].

For a bit of info
```console
$ python howisresolved.py --help
```

## Example
```console
$ python howisresolved.py --domain python.org --dnsfile dnslist.txt --dnsrand 3
$ python howisresolved.py --domain python.org
$ python howisresolved.py --domain python.org --dnsrand 3

random nameserver: ['123.202.155.89', '83.19.215.58', '78.193.175.96']

python.org IP 23.253.135.79 resolved by 123.202.155.89
python.org IP 23.253.135.79 resolved by 83.19.215.58
python.org IP 23.253.135.79 resolved by 78.193.175.96
```

issue&&PR || GTFO

enjoy.

## Authors

* **GB 'firegarden' Pullarà** - [firegarden](https://firegarden.co)

See also the list of [contributors](https://github.com/gionniboy/howisresolved/contributors) who participated in this project.

## License
This project is licensed under the BSD 3-Clause License - see the [LICENSE](LICENSE) file for details
