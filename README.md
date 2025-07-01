# v2ray

This Python script connects to multiple Telegram channels and scrapes their recent messages to extract proxy configurations, including **V2Ray** and **MTProto** links.

To use it first install `telethon` package using this command:
```
pip install telethon
# or
python -m pip install telethon
```

In the file `channels.json` you can see the list of telegram channels and the `api_hash` and `api_id`. In the channels section the numbers in front of the links is the number of recent messages to read. You add or remove channels to the list and change the message limit numbers.

You need `api_hash` and `api_id` for connecting to telegram using this app. By default it uses telegram desktop API keys and you can use them without any problem. But you can change them in `channels.json` file if you want.

Now you are ready to run `src/v2ray.py`.

Command Line Options
---
|option|description|
------|------|
|`-v,--v2ray`|Extract v2ray proxies|
|`-m,--mtproto`|Extract mtproto proxies|

⚠️ Disclaimer
---

I do **not** support any use of this tool for censorship, surveillance, or any form of human rights violation.

By using this code, you agree to take full responsibility for how it is used.
