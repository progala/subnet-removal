#!/usr/bin/env python3
"""
subnet_removal - Filters out child prefixes read from a file, or passed from standard input.

Usage:

- Filter out prefixes read from a file

$ subn_rm random_ips.txt

- Filter out prefixes piped from other program

$ cat ex_pfx_lengths_ipv4.txt | xargs -L 1 ./subn_rm [-ipv6]
"""
import argparse
import sys
from typing import Iterable, List

import pytricia


__author__ = "Przemek Rogala"


def filter_out_subnets(prefixes: Iterable[str], ipv6=False) -> List[str]:
    """
    Goes through prefixes and filters out any prefix that is a subnet of any other

    Uses Patricia Tree for efficient prefix lookups

    :param prefixes: iterable with prefixes
    :param ipv6: set to True for IPv6 prefixes
    :return: list of filtered out prefixes
    """
    if ipv6:
        pyt = pytricia.PyTricia(128)
    else:
        pyt = pytricia.PyTricia()
    for p in prefixes:
        pyt.insert(p, p)
        if pyt.parent(p):
            del pyt[p]
        elif pyt.children(p):
            for child in pyt.children(p):
                del pyt[child]

    return [pyt[p] for p in pyt]


if __name__ == "__main__":
    try:
        parser = argparse.ArgumentParser()
        parser.add_argument("input_file")
        parser.add_argument(
            "-ipv6",
            "--ipv6",
            action="store_true",
        )
        args = parser.parse_args()
        try:
            with open(args.input_file, mode="r", newline="") as fp:
                result = filter_out_subnets(fp, ipv6=args.ipv6)
        except IOError:
            print("Error. Unable to read file: {}.".format(args.input_file))
            raise SystemExit(1)
        for r in result:
            print(r, end="")
    except ValueError as e:
        print(e)
        sys.exit(1)
