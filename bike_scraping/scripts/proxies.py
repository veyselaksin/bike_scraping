from ast import Param
import requests
import json
from lxml.html import fromstring
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent
PROXY_LIST = Path.joinpath(BASE_DIR, "output/proxy_list.txt")

def get_proxies():
    url = "https://www.free-proxy-list.net/"

    response = requests.get(url)
    parser = fromstring(response.text)
    proxies = set()

    for item in parser.xpath("//tbody/tr"):
        if item.xpath(".//td[7][contains(text(), 'yes')]"):
            proxy = ":".join([item.xpath(".//td[1]/text()")[0], item.xpath(".//td[2]/text()")[0]])
            proxies.add(proxy)

    return proxies

def set_to_list(data:set):
    proxies = []

    for item in data:
        proxies.append(item)
    return proxies

if __name__ == "__main__":
    proxies = get_proxies()
    proxy_list = set_to_list(proxies)
    
    with open(PROXY_LIST, "w") as plist:

       plist.write("\n".join(proxy_list)) 