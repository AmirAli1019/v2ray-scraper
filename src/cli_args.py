import argparse, subprocess, os
from urllib.parse import urlparse

parser = argparse.ArgumentParser(prog='v2ray-scraper',
                                 description='A simple program to extract v2ray and mtproto proxies from ' \
                                 'multiple telegram channels')

parser.add_argument('-v','--v2ray', action='store_true', help='Extract v2ray proxies')

parser.add_argument('-m','--mtproto', action='store_true', help='Extract mtproto proxies')

parser.add_argument('-s','--session',help='The name of the session file (default: session_name.session)',
                     metavar='<file_name>', default='session_name.session')

parser.add_argument('-n','--no-save-messages',action='store_true',
                    help='Do not save the full messages of proxy channels to a file')

parser.add_argument('-f','--messages-file',
                    help='The name of the file to save channels messages (default: channels_messages.txt)',
                    default='channels_messages.txt',metavar='<file_name>')

parser.add_argument('-c','--auto-copy',action='store_true',
                    help='Automatically copy extracted proxies to clipboard')

parser.add_argument('-e','--save-extracted',help='Save the extracted proxies in a file', metavar='<file_name>')

parser.add_argument('-p','--print-proxies',
                    help='Print the extracted proxy configurations to the console', action='store_true')

parser.add_argument('-d', '--disable-delay', action='store_true',
                    help = 'disables the random delays between connections to different telegram channels (not recommended!)')

parser.add_argument('-r', '--retries', type=int, default=None, metavar='<retries>',
                    help='Set the number of retries when the connection to the telegram server is lost. (default: infinite).')

parser.add_argument('--proxy', metavar='<proxy>', 
                    help='Specify a proxy in the form: scheme://host:port. Supported: HTTP, SOCKS4 and SOCKS5')

args = parser.parse_args()

if args.proxy:
    from socks import HTTP, SOCKS4, SOCKS5

# --- termux support ---

def is_termux():
    is_android = subprocess.check_output(["uname", "-o"]).decode().strip() == "Android"
    termux_path_exists = os.path.isdir("/data/data/com.termux/files/usr/bin")

    return is_android and termux_path_exists

def termux_copy(proxies : str):
    subprocess.run("termux-clipboard-set", input=proxies.encode())

def invalid_proxy():
    print('Invalid proxy.')
    exit(1)

def specify_proxy(proxy : str):
    try:
        if args.proxy:
            data_list = [None, None, None]
            parsed_url = urlparse(proxy)

            # ----- specifying scheme -----

            if parsed_url.scheme == 'socks' or parsed_url.scheme == 'socks5':
                data_list[0] = SOCKS5

            elif parsed_url.scheme == 'socks4':
                data_list[0] = SOCKS4

            elif parsed_url.scheme == 'http':
                data_list[0] = HTTP

            else:
                invalid_proxy()

            # ----- specifying host and port -----
            
            splited_address = parsed_url.netloc.split(':')
            if len(splited_address) == 2:
                data_list[1], data_list[2] = splited_address[0], int(splited_address[1])
            else:
                invalid_proxy()

            return data_list

        else: # this executes when no proxy is entered
            return None

    except ValueError:
        invalid_proxy()
