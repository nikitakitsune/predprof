import math

vmax = 2
oxi = 0


def get_v(w, m):
    return vmax * (w // 80) * (200 // m)


def get_gn(go, kp):
    return go * (1 + kp)


def get_kp(t):
    return math.sin(math.pi / 2 + math.pi * (t + 0.5 * oxi) / 40)


def get_e(t):
    return sum(range(t + 1))

print(math.sin())