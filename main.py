import os, requests, json
os.system("cls") if os.name == "nt" else os.system("clear")
print("           > webhook flooder / tester < ")
print(" ")
# errors
try:
    f = open("config.json", "r")
    config = json.load(f)
except:
    print("config.json not found")
    os.system("pause")
    exit()
if not config["webhook_url"]:
    print('Webhook URL not defined')
    os.system("pause")
    exit()

# actual flooding
i = 0
webhook = {
    "content": "",
    "username": config["username"],
    "avatar_url": config["avatar_url"]
}
print("Using default username (username field in config.json blank)" if not config["username"] else f"Username set: {config['username']}")
print("Using default avatar (avatar_url field in config.json blank)" if not config["avatar_url"] else f"Username set: {config['avatar_url']}")
print(" ")
while True:
    message = input(f"#{i} >> ")
    i+=1
    if not message or message == " ":
        continue
    webhook["content"] = message
    s = requests.post(config["webhook_url"], data=webhook)
    if not s.status_code == 204:
        print(f" ! An error occurred and '{message}' was not sent. | Status Code: {s.status_code} | Error text: {s.text}")
