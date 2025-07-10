import argparse

parser = argparse.ArgumentParser(prog='v2ray',
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

args = parser.parse_args()