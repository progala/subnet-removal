import ipaddress
from itertools import islice
from random import randint
from time import process_time

from subnet_removal import filter_out_subnets


def random_pfx():
    """
    Caveman style random pfx generation
    :return:
    """
    while True:
        rp = "{0}.{1}.{2}.{3}/{4}".format(
            randint(1, 223),
            randint(0, 255),
            randint(0, 255),
            randint(0, 254),
            randint(8, 31),
        )
        pfx = str(ipaddress.IPv4Interface(rp).network.with_prefixlen)
        yield pfx


if __name__ == "__main__":
    for pow in range(3, 7):
        pfxs = list(islice(random_pfx(), 0, 10 ** pow))

        start = process_time()

        filter_out_subnets(pfxs)

        end = process_time()

        print(
            "It took {0:05.5f}s to process {1:,} random prefixes.".format(
                end - start, 10 ** pow
            )
        )

    with open("test_input/inet-pfxs.txt") as f:
        pfxs = list(l.strip() for l in f)

    inet_sz = len(pfxs)

    start = process_time()

    inet_flt = filter_out_subnets(pfxs)

    end = process_time()

    print("\n\nNow something more fun. Full Internet table!")
    print(
        "It took {0:05.5f}s to process {1:,} Internet prefixes.\n"
        "After filtering out subnets we are left with {2:,} prefixes.".format(
            end - start, inet_sz, len(inet_flt)
        )
    )
