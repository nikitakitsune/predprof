import math
import requests_manager
vmax = 2


def get_v(w, m):
    return vmax * (w // 80) * (200 // m)


def get_gn(go, kp):
    return go * (1 + kp)


def get_kp(t, oxi):
    return math.sin(math.pi / 2 + math.pi * (t + 0.5 * oxi) / 40)


def get_e(t):
    return sum(range(1, t + 1))


import requests, math

Fuel_price = 10
Oxygen_price = 7
Oxygen = 0
Fuel = 0
vmax = 2
sh = 8
oxi = min(Oxygen / sh, 60)


def get_v(w, m):
    return vmax * (w / 80) * (200 / m)


def get_gn(go, kp):
    return go * (1 + kp)


def get_kp(t, oxi):
    return math.sin(-math.pi / 2 + math.pi * (t + 0.5 * oxi) / 40)


def get_e(t):
    return sum(range(t + 1))


def func(data):
    for i in (data['message'])[0]['points'][::-1]:
        SH = i['SH'] + 8
        distance = i['distance']
        test_SH = 8
        time = 0
        k = 2
        w = 80
        days = math.log(SH, k)
        while test_SH < SH:
            time += 1 / get_v(w, test_SH + 192)
            test_SH *= 2
        time = math.ceil(time)
        if days < time:
            k = math.log(time, 8)
        else:
            t = time
            while days >= t:
                te = 0
                w -= 1
                test_SH = 8
                while test_SH < SH:
                    te += 1 / get_v(w, test_SH + 192)
                    test_SH *= 2
                t = te
        e = 100 - w
        temp = 0
        while get_e(temp) <= e:
            temp += 1
        return [distance, max(time, math.ceil(t)), days, k, w, temp]


print(func(requests_manager.get_json()))
