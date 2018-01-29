# howisresolved
how is resolved is a little python script to resolve a domain from differents nameservers.

DNS list is passed with a simple txt file.
If not present the script download a list of valid nameservers from [public-dns.info](https://public-dns.info/).

An output on cli is generated.

Python3 required.

Install requirements.txt for dependency.

Use requirements-dev.txt if you want contribute to.

## Example

`python3 howisresolved.py python.org name.txt 3`

```
random nameserver: ['123.202.155.89', '83.19.215.58', '78.193.175.96']

python.org IP 23.253.135.79 resolved by 123.202.155.89
python.org IP 23.253.135.79 resolved by 83.19.215.58
python.org IP 23.253.135.79 resolved by 78.193.175.96
```


enjoy.
