import requests


def get_json():
    return requests.get("https://dt.miet.ru/ppo_it_final/judge2", headers={"X-Auth-Token": "njcx7yms"}).json()
