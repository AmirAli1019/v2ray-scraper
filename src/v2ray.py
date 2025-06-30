import argparse,asyncio
from telethon.sync import TelegramClient
from telethon.tl.functions.messages import GetHistoryRequest
from telethon.errors import ChannelPrivateError, PeerIdInvalidError
import random, json, os, extractors

__version__ = '1.0.0'

parser = argparse.ArgumentParser(prog='v2ray',description='A simple program to extract v2ray and mtproto proxies from multiple telegram channels')
parser.add_argument('-v','--v2ray', action='store_true', help='Extract v2ray proxies')
parser.add_argument('-m','--mtproto', action='store_true', help='Extract mtproto proxies')
args = parser.parse_args()

session_name = 'session_name.session'

channels_path = os.path.join(os.path.dirname(__file__), 'channels.json')
with open(channels_path) as f:
    channels,api = json.load(f)

channels = list(channels.items())
random.shuffle(channels)
channels = dict(channels)

async def main():
    result_text = ""
    for channel_identifier in channels:
        try:
            print(f"Attempting to connect to channel: {channel_identifier} ...")
            channel = await client.get_entity(channel_identifier)

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

    with open("all_channel_messages.txt", "w", encoding="utf-8") as f:
        f.write(result_text)

    print("\nOperation finished. All messages have been saved to 'all_channel_messages.txt'.")

    if args.v2ray:
        v2ray_proxies = extractors.extract_v2ray_proxies(result_text)
        print(v2ray_proxies)

    if args.mtproto:
        mtproto_proxies = extractors.extract_mtproto_proxies(result_text)
        print(mtproto_proxies)

with TelegramClient(session_name, api['api_id'], api['api_hash']) as client:
    client.loop.run_until_complete(main())
