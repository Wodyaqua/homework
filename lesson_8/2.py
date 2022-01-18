import re
import requests

raw = requests. \
    get('https://raw.githubusercontent.com/elastic/examples/master/Common%20Data%20Formats/nginx_logs/nginx_logs').text

pattern = re.compile(r'((?:[0-9]{,3}[.]){3}[0-9]{,3}) - - (.[0-9]{,2}/\w+/[0-9]{4}:(?:[0-9]{2}:){2}[0-9]{2} '
                     r'\+[0-9]{4}]) .(\w+) ([/\w+]{0,}) (?:[^\"]*)\" ([0-9]+) ([0-9]+)')

for parsed_raw in pattern.findall(raw):
    address, date, request_type, product, arg, next_arg = parsed_raw
    print(address, date, request_type, product, arg, next_arg)
