<p align="center">
  <a href="README-fa.md">فارسی</a>
</p>

# v2ray scraper

This Python script connects to multiple Telegram channels and groups and extracts proxy configurations from recent messages, including **V2Ray** and **MTProto** links.

---

## 🚀 Installation

Fisrt, clone the repository:

```bash
git clone https://github.com/AmirAli1019/v2ray-scraper
```

Or as a better option download the lastest release from the [releases](https://github.com/AmirAli1019/v2ray-scraper/releases) page.

Install the required dependencies:

```bash
pip install telethon

# optional (for clipboard support)
pip install pyperclip

# optional (for proxy support) it is needed for HTTP, SOCKS5 and SOCKS4 proxies. But telethon can connect to MTProto proxies itself and pysocks is not needed for MTProto proxies.
pip install pysocks
```

I was using these versions while developing this program:

```
telethon 1.41.2 & 1.42.0 (These versions of telethon do not work with python3.14)
pysocks 1.7.1
pyperclip 1.11.0
```

To install all these dependencies with specified versions:

```
pip install -r requirements.txt
```

## ▶️ Usage

Run the script:

```bash
python src/v2ray-scraper.py [options]
```

After you run the program for the first time. It asks you for your telegram account phone number and other login requirements.
Actually it uses your telegram account to access channels so you can add a private channel or a private group to `channels.json` file. Edit this file according to the configuration guide below.

For scraping data from private channels and groups ensure that you have joined them in telegram.

**Warning: After logging in, a file with the extension `.session` will be created. this is the key to access your telegram account so you don't need to login every time you run the program, but notice that you must keep the `.session` file in a safe place to prevent others to access your telegram account**

## ⚙️ Configuration

The configuration file is channels.json.

- It contains:

  - A list of Telegram channels.

  - api_id and api_hash (needed for Telegram API authentication).

  - For each channel, you can specify how many recent messages to fetch.

By default, the script uses Telegram Desktop API keys, so you can run it without changes.
However, you may replace them with your own api_id and api_hash if needed.

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
|`-d,--disable-delay`|disables the delays between connections to different telegram channels (not recommended!)|
|`-r, --retries`|Set the number of retries when the connection to the telegram server is lost. (default: infinite).|
|`--proxy`|Specify a proxy in the form: scheme://host:port. Supported: HTTP, SOCKS4 and SOCKS5, MTProto|
|`--delay`|Specify the random delay interval in seconds in the format \<min\>-\<max\>. (default: 1.0-1.6)|
|`-h,--help`|Show the help message and exit|

For `--proxy` argument the given MTProto proxy must be like this: `https://t.me/proxy?server=...&port=...&secret=...`

**note: Always remember to put the MTProto link in a pair of quotation characters like this:
`--proxy "https://t.me/proxy?server=...&port=...&secret=..."`
Maybe your shell consider some of chracters in the MTProto link as codes and causes unexcepted outputs.**

## Termux Support

You can use `v2ray-scraper` on android using Termux. First download it from [f-droid](https://f-droid.org/packages/com.termux/).
Then clone the repo and install python3:

```bash
apt update && apt upgrade -y
pkg install git python3
git clone https://github.com/amirali1019/v2ray-scraper
```

Next, install `telethon`:

```bash
pip install telethon

# optional (for proxy support)
pip install pysocks
```

But if you want clipboard support you cannot use `pyperclip` for that. Instead install [Termux:API](https://f-droid.org/packages/com.termux.api/) from F-Droid and the package `termux-api` on termux:

```bash
pkg install termux-api
```

Then you can run it on your mobile in the same way you run it on your computer.

## 📋 Example

```bash
# Extract V2Ray proxies, copy them to clipboard, and print to console
python src/v2ray-scraper.py -v -c -p
```

## ⚠️ Disclaimer

I do not support any use of this tool for censorship, surveillance, or any form of human rights violation.

By using this code, you agree to take full responsibility for how it is used.

## Credits / Attribution

This project was originally inspired by a small script which was published on Telegram with no specified license.
This repository include some portions from the first version with many modifications and new feature.

The link of first version on Telegram (may be unavailable in future): [Telegram source](https://t.me/SoniaNotes/1015)

If the original author identifies themselves and requests changes, I will fully comply.
