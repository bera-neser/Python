#!/usr/bin/python3

# This simple short code snippet is extracting the
# host from a given URL via RegEx regardless the
# extension, how many subdomain it has or whether
# it starts with "http(s)://www.", or pointing to
# specific path or not.

import re
from tld import get_tld, get_fld

HOST_REGEX = r"(?:https?:\/\/)?(?:www\.)?(?:.*\.)?([^\/]*)\."


def host_extractor(url):
    Match = re.match(HOST_REGEX, url)
    return Match.group(1)


if __name__ == "__main__":
    URL = (
        "https://www.subdomain.example.com/path1?query1=value1&query2=value2#fragment1"
    )
    print(host_extractor(URL))  # Output: "example"
    print(get_tld(URL).domain)  # Output: "example"
    print(get_fld(URL))  # Output: "example.com"
