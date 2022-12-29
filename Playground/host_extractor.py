#!/usr/bin/python3

# This simple short code snippet is extracting the 
# host from a given URL via RegEx regardless the
# extension, how many subdomain it has or whether
# it starts with "http(s)://www.", or pointing to
# specific path or not.

import re

URL = "https://www.subdomain.example.com/"
host = re.findall(r"(https?:\/\/)?(www\.)?(.*\.)?([^\/]*)\.", URL)[-1][-1]
print(host) # Output: "example"