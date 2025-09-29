# v2ray Scraper

This Python script connects to multiple Telegram channels and extracts proxy configurations from recent messages, including **V2Ray** and **MTProto** links.

---

## 🚀 Installation

First, install the required dependencies:

```bash
pip install telethon
# optional (for clipboard support)
pip install pyperclip
```

## ⚙️ Configuration

The configuration file is channels.json.

- It contains:

    - A list of Telegram channels.

    - api_id and api_hash (needed for Telegram API authentication).

    - For each channel, you can specify how many recent messages to fetch.

By default, the script uses Telegram Desktop API keys, so you can run it without changes.
However, you may replace them with your own api_id and api_hash if needed.

## ▶️ Usage

Run the script:

```bash
python src/v2ray.py [options]
```

## Command Line Options

|option|description|
|------|------|
|`-v,--v2ray`|Extract v2ray proxies|
|`-m,--mtproto`|Extract mtproto proxies|
|`-s,--session`|The name of the session file (default: session_name.session)|
|`-n,--no-save-messages`|Do not save the full messages of proxy channels to a file|
|`-f,--messages-file`|The name of the file to save channels messages (default: channels_messages.txt)|
|`-c,--auto-copy`|Automatically copy extracted proxies to clipboard|
|`-e,--save-extracted`|Save the extracted proxies in a file|
|`-p,--print-proxies`|Print the extracted proxy configurations to the console|
|`-d`,`--disable-delay`|disables the delays between connections to different telegram channels (not recommended!)|
|`-r, --retries`|Set the number of retries when the connection to the telegram server is lost. (default: infinite).|
|`-h,--help`|Show the help message and exit|

## Termux Support

You can use `v2ray-scraper` on android using Termux. First download it from [f-droid](https://f-droid.org/packages/com.termux/).
Then clone the repo and install python3:

```bash
pkg install git python3
git clone https://github.com/amirali104/v2ray-scraper
```

Next, install `telethon`:

```bash
pip install telethon
```

But if you want clipboard support you cannot use `pyperclip` for that. Instead install [Termux:API](https://f-droid.org/packages/com.termux.api/) from F-Droid and the package `termux-api` on termux:

```bash
pkg install termux-api
```

Then you can run it on your mobile in the same way you run it on your computer.

## 📋 Example

```bash
# Extract V2Ray proxies, copy them to clipboard, and print to console
python src/v2ray.py -v -c -p
```

## ⚠️ Disclaimer

I do not support any use of this tool for censorship, surveillance, or any form of human rights violation.

By using this code, you agree to take full responsibility for how it is used.
