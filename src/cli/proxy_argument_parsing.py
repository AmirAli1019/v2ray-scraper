from urllib.parse import urlparse

import re


def invalid_proxy():
    print("Invalid proxy.")
    exit(1)


def is_mtproto(proxy_string: str):
    return proxy_string.startswith("https://t.me/proxy?server")


def parse_mtproto_proxy(proxy_string: str):
    url_queries = urlparse(proxy_string).query.split("&")

    if len(url_queries) != 3:
        invalid_proxy()

    data_list = [0, "", 0]

    for i, pattern in enumerate([r"server=(.+)", r"port=(.+)", r"secret=(.+)"]):
        data = re.search(pattern, url_queries[i])

        if data:
            data_list[i] = data.group(1)
        else:
            invalid_proxy()

    data_list[1] = int(data_list[1])

    return data_list


def parse_normal_proxy(proxy_string: str):
    from socks import HTTP, SOCKS4, SOCKS5

    data_list = [0, "", 0]
    parsed_url = urlparse(proxy_string)

    # ----- specifying scheme -----

    if parsed_url.scheme == "socks" or parsed_url.scheme == "socks5":
        data_list[0] = SOCKS5

    elif parsed_url.scheme == "socks4":
        data_list[0] = SOCKS4

    elif parsed_url.scheme == "http":
        data_list[0] = HTTP

    else:
        invalid_proxy()

    # ----- specifying host and port -----

    splited_address = parsed_url.netloc.split(":")
    if len(splited_address) == 2:
        data_list[1], data_list[2] = splited_address[0], int(splited_address[1])
    else:
        invalid_proxy()

    return data_list


def get_proxy_components(proxy_string: str):
    try:
        if proxy_string:
            if is_mtproto(proxy_string):
                return parse_mtproto_proxy(proxy_string)
            else:
                return parse_normal_proxy(proxy_string)

        else:  # this executes when no proxy is entered
            return None

    except ValueError:
        invalid_proxy()
