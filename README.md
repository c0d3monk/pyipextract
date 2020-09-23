# pyipextract
Python utility to extract or validate IPv4 addresses

## IPv4 Extraction 
* It can extract valid IPv4 addresses from a given string
* Returns a list of all valid IPv4 addresses extracted from a given string

## IPv4 Validation
* Can also be used just to validate an IPv4address

## Installation
`pip install pyipextract`

## How to use

Here's an example of calling `IPExtractor` constructor and using the extraction or just validation 
mechanisms

### Extraction
```
from pyipextract import IPExtractor

input_str = "This is a string which contains valid IPs 192.168.1.1, 1.1.1.1 and an invalid IP 256.444.22.22"
ip_extractor = IPExtractor()
extracted_ips = ip_extractor.extract(input_str)
print(extracted_ips) 

```

Output:

```
['192.168.1.1', '1.1.1.1']
```

### Validation

```
from pyipextract import IPExtractor

ips = ["192.168.1.1", "256.444.22.22", "1.1.1.1111"]
ip_extractor = IPExtractor()
for value in ips:
    if ip_extractor.validate(value):
        print("Valid IP: {}".format(value))
    else:
        print("Invalid IP: {}".format(value))
```

Output
```
Valid IP: 192.168.1.1
Invalid IP: 256.444.22.22
Invalid IP: 1.1.1.1111
```

