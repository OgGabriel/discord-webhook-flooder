# Discord Webhook Flooder / Tester
Discord Webhook flooder/tester made with Python.

It is either tester or flooder because you can do both.

## Requirements
This python script only uses standard python libraries.

## How to use
You just need to setup ``config.json`` file with the required information about the webhook then do ``py main.py``

## Setting up config.json
- ``"webhook_url"``
This field is reserved to the webhook's url
- ``"avatar_url"``
This field is reserved to overwrite the webhook's icon when the message is sent
- ``"username"``
This field is reserved to overwrite the webhook's username when the message is sent

## Errors
Whenever you do not provide a value for ``"webhook_url"`` or ``config.json`` is not found it throws an error.
- value for ``"webhook_url"`` not provided
![wbhknotprovided](https://prnt.sc/wm6x3c "Webhook URL not defined")
- ``config.json`` not found
![configjsonnotfound](https://prnt.sc/wm6xni "config.json not found")
