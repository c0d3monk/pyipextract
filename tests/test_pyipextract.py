import pytest
from pyipextract import IPExtractor


@pytest.mark.parametrize("data", ['string with IP 192.168.1.1',
                                  'this is a ip surrounded by special chars #!"$%&(@)=<>:{}~`_*+-192.168.1.1/24!"\n$%&(@)=<>:{}~`_*+-/24 ',
                                  'random string with ip 1.1.1.1.'
                                  ])
def test_valid_ip_extraction(data):
    obj = IPExtractor()
    assert len(obj.extract(data)) > 0


@pytest.mark.parametrize("data", ["invalid ip 256.256.265.566", "1111.1.1.1"])
def test_invalid_ips_string(data):
    obj = IPExtractor()
    assert not len(obj.extract(data))


@pytest.mark.parametrize("data", ["256.135.223.333"])
def test_ip_validation_with_invalid_ips(data):
    obj = IPExtractor()
    assert not obj.validate(data)


@pytest.mark.parametrize("data", ["8.8.8.8", "255.255.255.255", "1.0.0.0"])
def test_ip_validation_with_valid_ips(data):
    obj = IPExtractor()
    assert obj.validate(data)