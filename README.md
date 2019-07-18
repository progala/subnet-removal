# subnet_removal: Subnet filtering for IPv4 and IPv6 prefixes

subnet_removal - Filters out child prefixes read from a file, or passed from standard input.

Can be used as a module or as a standalone shell utility.

More details @ http://ttl255.com/subnet-removal-with-python/

## Import as a module

```python
>>> from subnet_removal import filter_out_subnets
>>> pfxs = ["10.0.1.0/24", "10.0.1.128/25", "10.0.1.192/28"]
>>> pfxs_filt = filter_out_subnets(pfxs)
>>> print(pfxs_filt)
['10.0.1.0/24']

>>> ipv6pfxs = ["2001:db8::/48", "2001:db8:0:a::/64", "2001:db8:0:b::/64", "2001:db8:1:a::/64"]
>>> ipv6pfxs_filt = filter_out_subnets(ipv6pfxs, ipv6=True)
>>> print(ipv6pfxs_filt)
['2001:db8::/48', '2001:db8:1:a::/64']
```


## Shell usage:

- Filter out prefixes read from a file

$ subn_rm pfxs_ex_01.txt [-ipv6]

```ipv6``` flag enables processing of IPv6 prefixes
