import re

V2RAY_PATTERN = r'^(vmess|vless|ss|trojan)://.+(?=\n)?'
MTPROTO_PATTERN = r'^https://t\.me/proxy\?server=.+(?=\n)?'

def extract_v2ray_proxies(result_text):
    proxies_list = [match.group() for match in re.finditer(V2RAY_PATTERN,result_text,re.M)]
    proxies_string = '\n'.join(proxies_list)

    return proxies_string

def extract_mtproto_proxies(result_text):
    proxies_list = re.findall(MTPROTO_PATTERN,result_text,re.M)
    proxies_string = '\n'.join(proxies_list)

    return proxies_string