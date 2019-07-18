import pytest

from subnet_removal.subn_rm import filter_out_subnets


@pytest.mark.parametrize(
    "prefixes,result",
    [
        (["10.0.1.0/24", "10.0.1.128/25", "10.0.1.192/28"], ["10.0.1.0/24"]),
        (["10.1.0.0/16", "10.0.0.0/15", "10.2.0.0/16"], ["10.0.0.0/15", "10.2.0.0/16"]),
        (
            [
                "10.0.0.0/25",
                "10.0.0.0/29",
                "10.0.0.8/29",
                "10.0.0.16/29",
                "10.0.0.128/26",
                "10.0.0.160/27",
                "10.0.0.192/26",
                "10.0.0.248/30",
            ],
            ["10.0.0.0/25", "10.0.0.128/26", "10.0.0.192/26"],
        ),
        (
            ["10.0.0.0/8", "172.16.0.0/12", "192.168.0.0/16"],
            ["10.0.0.0/8", "172.16.0.0/12", "192.168.0.0/16"],
        ),
    ],
)
def test_subn_rm(prefixes, result):
    assert filter_out_subnets(prefixes) == result


@pytest.mark.parametrize(
    "prefixes,result",
    [
        (
            [
                "2001:db8::/48",
                "2001:db8:0:a::/64",
                "2001:db8:0:b::/64",
                "2001:db8:0:c::/64",
                "2001:db8:0:d::/64",
                "2001:db8:0:e::/64",
                "2001:db8:1:a::/64",
            ],
            ["2001:db8::/48", "2001:db8:1:a::/64"],
        ),
    ],
)
def test_subn_rm_ipv6(prefixes, result):
    assert filter_out_subnets(prefixes, ipv6=True) == result
