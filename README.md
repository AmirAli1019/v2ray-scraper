# v2ray

This Python script connects to multiple Telegram channels and scrapes their recent messages to extract proxy configurations, including **V2Ray** and **MTProto** links.

To use it first install `telethon` package using this command:
```
pip install telethon
# or
python -m pip install telethon
```

In the file `channels.json` you see the list of telegram channels and the `api_hash` and `api_id`. In the channels section the numbers in front of the links is the number of recent messages to read. You add or remove channels to the list and change the message limit numbers.

You need `api_hash` and `api_id` for connecting to telegram using this app. To get them go to `my.telegram.org` and login to your account, then go to `API Developement Tools` and fill the form. Now you can get your own `api_hash` and `api_id`. Paste then within the `channels.json` file in the specified fields.

Now you are ready to run `src/v2ray.py`.

Command Line Options
---
|option|description|
------|------|
|`-v,--v2ray`|Extract v2ray proxies|
|`-m,--mtproto`|Extract mtproto proxies|

⚠️ Disclaimer
---

The author does **not** support any use of this tool for censorship, surveillance, or any form of human rights violation.

By using this code, you agree to take full responsibility for how it is used.
