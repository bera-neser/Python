import tld
import requests
from bs4 import BeautifulSoup

url = "https://stackoverflow.com/"

print(
    *[
        link.get("href")
        for link in BeautifulSoup(
            requests.Session().get(url).content, "html.parser"
        ).find_all("a")
        if link.get("href") is not None
        and link.get("href") != ""
        and not any(
            x in link.get("href")
            for x in [
                "#",
                "?",
                "../",
                "data:",
                "about:",
                "mailto:",
                "callto:",
                "javascript:",
                ".webmanifest",
                "ios-app://",
                "android-app://",
            ]
        )
        and tld.get_fld(url, fail_silently=True)
        == tld.get_fld(link.get("href"), fail_silently=True)
    ],
    sep="\n"
)
