import requests
print(requests.get("https://dt.miet.ru/ppo_it_final",headers={"X-Auth-Token": "njcx7yms"}).json())