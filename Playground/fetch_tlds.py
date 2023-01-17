import requests

# from itertools import islice

r = requests.get("https://data.iana.org/TLD/tlds-alpha-by-domain.txt")

tlds = "|".join(
    [
        line.decode().lower()
        for line in r.iter_lines()
        if (" " in line.decode()) == False
    ]
)  # - 0.20s
# tlds = "|".join([line.decode().lower() for i, line in enumerate(r.iter_lines()) if i != 0])  # - Alternative way, using enumerate() = 0.20s
# tlds = "|".join([line.decode().lower() for line in islice(r.iter_lines(), 1, None)]) # - Alternative way, using itertools - 0.20s

print(tlds)
