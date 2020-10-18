import re
import sys
from typing import List


class IPExtractor:
    def __init__(self):
        self.ip_regex = re.compile(r"^(\d{1,3}\.){3}\d{1,3}$")
        self.valid_ip_regex = re.compile(r"^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$")

    def extract(self, data: str) -> List:
        result = []
        data_items = re.split('[;, \n/\\\\#!"$%&(@)=<>:{}~`_*+-]', data)
        for d in data_items:
            d = d.rstrip(".")
            if len(d):
                result.append(self.ip_regex.match(d))
        result = [x for x in [x.group(0) for x in result if x] if self.validate(x)]
        return result

    def validate(self, data: str) -> bool:
        result = False
        if self.valid_ip_regex.match(data):
            result = True
        return result


if __name__ == '__main__':
    input_str = sys.argv[1]
    ip_extractor = IPExtractor()
    # Extract valid IPv4 from a string
    extracted_ips = ip_extractor.extract(input_str)

    print("Extracted IPs: {}".format(extracted_ips))

