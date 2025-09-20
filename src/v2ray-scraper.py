__version__ = '1.3.1'

from cli_args import args

import asyncio, subprocess
from telethon.sync import TelegramClient
from telethon.tl.functions.messages import GetHistoryRequest
from telethon.errors import ChannelPrivateError, PeerIdInvalidError
import random, json, os, extractors

# --- termux support ---

def is_termux():
    is_android = subprocess.check_output(["uname", "-o"]).decode().strip() == "Android"
    termux_path_exists = os.path.isdir("/data/data/com.termux/files/usr/bin")

    return is_android and termux_path_exists

def termux_copy(proxies : str):
    subprocess.run("termux-clipboard-set", input=proxies.encode())

# --- checking for auto copy option enabled and the platform working on ---

copy_function = None

def set_copy_function():
    global copy_function

    if os.name == 'posix':
        if is_termux():
            copy_function = termux_copy
            return

    copy_function = __import__('pyperclip').copy

if args.auto_copy:
    set_copy_function()

session_name = args.session

# --- loads channels list and API keys ---

channels_path = os.path.join(os.path.dirname(__file__), 'channels.json')
with open(channels_path) as f:
    channels,api = json.load(f)

# --- shuffles the channels list randomly ---

channels = list(channels.items())
random.shuffle(channels)
channels = dict(channels)

# ----------------------------

def handle_proxies_output(result_text):
    if not args.no_save_messages:
        with open(args.messages_file, "w", encoding="utf-8") as f:
            f.write(result_text)

        print(f'\nAll messages have been saved to {args.messages_file!r}.')

    proxies = ''
    if args.v2ray:
        proxies += extractors.extract_v2ray_proxies(result_text) + '\n\n'

    if args.mtproto:
        proxies += extractors.extract_mtproto_proxies(result_text)

    if args.auto_copy:
        copy_function(proxies)

        print('All extracted proxy configs have been copied to clipboard')

    if args.save_extracted:
        with open(args.save_extracted,'w',encoding='utf-8') as f:
            f.write(proxies)
        
        print(f'All extracted proxy configs have been save to {args.save_extracted!r}')

    if args.print_proxies:
        print(proxies)

# --- the main program ---

async def main():
    result_text = ""
    for channel_identifier in channels:
        try:
            print(f"Attempting to connect to channel: {channel_identifier} ...")
            channel = await client.get_entity(channel_identifier)

            if not args.disable_delay:
                await asyncio.sleep(random.uniform(1,1.6))

            history = await client(GetHistoryRequest(
                peer=channel,
                limit=channels[channel_identifier],
                offset_date=None,
                offset_id=0,
                max_id=0,
                min_id=0,
                add_offset=0,
                hash=0
            ))

            messages = history.messages
            
            result_text += f"\n\n--- Channel: {channel.title} ({channel_identifier}) ---\n"
            print(f"Reading messages from '{channel.title}'...")
            
            message_count = 0
            for msg in messages:
                if msg.message:
                    result_text += msg.message + '\n'
                    message_count += 1
            
            if message_count == 0:
                result_text += "No text messages were found in this channel.\n"

        except (ChannelPrivateError, PeerIdInvalidError):
            error_msg = f"Error: Channel '{channel_identifier}' is private or could not be found. Please ensure you are a member or the username is correct."
            print(error_msg)
            result_text += f"\n\n--- Channel: {channel_identifier} ---\n{error_msg}\n"

        except Exception as e:
            error_msg = f"An unexpected error occurred for '{channel_identifier}': {type(e).__name__} - {e}"
            print(error_msg)
            result_text += f"\n\n--- Channel: {channel_identifier} ---\n{error_msg}\n"

    handle_proxies_output(result_text)

with TelegramClient(session_name, api['api_id'], api['api_hash']) as client:
    client.loop.run_until_complete(main())
