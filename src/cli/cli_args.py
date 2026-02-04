import argparse
import os
import subprocess

parser = argparse.ArgumentParser(
    prog="v2ray-scraper",
    description="A simple program to extract v2ray and mtproto proxies from "
    "multiple telegram channels",
)

parser.add_argument("-v", "--v2ray", action="store_true", help="Extract v2ray proxies")

parser.add_argument(
    "-m", "--mtproto", action="store_true", help="Extract mtproto proxies"
)

parser.add_argument(
    "-s",
    "--session",
    help="The name of the session file (default: session_name.session)",
    metavar="<file_name>",
    default="session_name.session",
)

parser.add_argument(
    "-n",
    "--no-save-messages",
    action="store_true",
    help="Do not save the full messages of proxy channels to a file",
)

parser.add_argument(
    "-f",
    "--messages-file",
    help="The name of the file to save channels messages (default: channels_messages.txt)",
    default="channels_messages.txt",
    metavar="<file_name>",
)

parser.add_argument(
    "-c",
    "--auto-copy",
    action="store_true",
    help="Automatically copy extracted proxies to clipboard",
)

parser.add_argument(
    "-e",
    "--save-extracted",
    help="Save the extracted proxies in a file",
    metavar="<file_name>",
)

parser.add_argument(
    "-p",
    "--print-proxies",
    help="Print the extracted proxy configurations to the console",
    action="store_true",
)

parser.add_argument(
    "-d",
    "--disable-delay",
    action="store_true",
    help="disables the random delays between connections to different telegram channels (not recommended!)",
)

parser.add_argument(
    "-r",
    "--retries",
    type=int,
    default=None,
    metavar="<retries>",
    help="Set the number of retries when the connection to the telegram server is lost. (default: infinite).",
)

parser.add_argument(
    "--proxy",
    metavar="<proxy>",
    help="Specify a proxy in the form: scheme://host:port. Supported: HTTP, SOCKS4 and SOCKS5",
)

parser.add_argument(
    "--delay",
    metavar="<interval>",
    help="Specify the random delay interval in seconds in the format <min>-<max>. (default: 1.0-1.6)",
    default="1.0-1.6",
)

args = parser.parse_args()

# --- termux support ---


def is_termux():
    is_android = subprocess.check_output(["uname", "-o"]).decode().strip() == "Android"
    termux_path_exists = os.path.isdir("/data/data/com.termux/files/usr/bin")

    return is_android and termux_path_exists


def termux_copy(proxies: str):
    subprocess.run("termux-clipboard-set", input=proxies.encode())


def set_delay_interval(interval: str):
    try:
        index = interval.find("-")
        interval_list = [float(interval[:index]), float(interval[index + 1 :])]
        if interval_list[0] < 0 or interval_list[1] < 0:
            raise ValueError
        return interval_list

    except Exception:
        parser.error("The entered interval is not valid.")
