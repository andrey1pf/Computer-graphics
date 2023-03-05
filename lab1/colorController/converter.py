import colorsys


def cmyk_to_rgb(c, m, y, k):
    c = int(c) / 100
    m = int(m) / 100
    y = int(y) / 100
    k = int(k) / 100
    if 0 <= c <= 1 and 0 <= m <= 1 and 0 <= y <= 1 and 0 <= k <= 1:
        r = 255 * (1 - c) * (1 - k)
        g = 255 * (1 - m) * (1 - k)
        b = 255 * (1 - y) * (1 - k)
        return int(r), int(g), int(b)
    return -1, -1, -1


def rgb_to_cmyk(r, g, b):
    r = int(r)
    g = int(g)
    b = int(b)
    if 0 <= r <= 255 and 0 <= g <= 255 and 0 <= b <= 255:
        r, g, b = r / 255.0, g / 255.0, b / 255.0

        k = 1 - max(r, g, b)
        c = (1 - r - k) / (1 - k) if (1 - k) != 0 else 0
        m = (1 - g - k) / (1 - k) if (1 - k) != 0 else 0
        y = (1 - b - k) / (1 - k) if (1 - k) != 0 else 0

        return int(c * 100), int(m * 100), int(y * 100), int(k * 100)
    return -1, -1, -1, -1


def rgb_to_hls(r, g, b):
    r = int(r)
    g = int(g)
    b = int(b)
    if 0 <= r <= 255 and 0 <= g <= 255 and 0 <= b <= 255:
        r, g, b = r / 255.0, g / 255.0, b / 255.0

        max_val = max(r, g, b)
        min_val = min(r, g, b)

        l = (max_val + min_val) / 2.0

        if max_val == min_val:
            s = 0
        elif l < 0.5:
            s = (max_val - min_val) / (max_val + min_val)
        else:
            s = (max_val - min_val) / (2.0 - max_val - min_val)

        if max_val == min_val:
            h = 0
        elif r == max_val:
            h = (60 * ((g - b) / (max_val - min_val))) % 360
        elif g == max_val:
            h = 60 * ((b - r) / (max_val - min_val)) + 120
        else:
            h = 60 * ((r - g) / (max_val - min_val)) + 240

        if h < 0:
            h += 360

        return int(h), int(l * 100), int(s * 100)
    return -1, -1, -1


def hls_to_rgb(h, l, s):
    h = int(h)
    l = int(l) / 100
    s = int(s) / 100
    if 0 <= h < 360 and 0 <= l <= 1 and 0 <= s <= 1:
        h /= 360.0

        if s == 0:
            r, g, b = l, l, l
        else:
            def hue_to_rgb(p, q, t):
                if t < 0:
                    t += 1
                if t > 1:
                    t -= 1
                if t < 1 / 6:
                    return p + (q - p) * 6 * t
                if t < 1 / 2:
                    return q
                if t < 2 / 3:
                    return p + (q - p) * (2 / 3 - t) * 6
                return p

            q = l * (1 + s) if l < 0.5 else l + s - l * s
            p = 2 * l - q
            r = hue_to_rgb(p, q, h + 1 / 3)
            g = hue_to_rgb(p, q, h)
            b = hue_to_rgb(p, q, h - 1 / 3)

        r, g, b = int(r * 255), int(g * 255), int(b * 255)

        return r, g, b
    return -1, -1, -1


def cmyk_to_hls(c, m, y, k):
    c = int(c)
    m = int(m)
    y = int(y)
    k = int(k)
    r, g, b = cmyk_to_rgb(c, m, y, k)
    if r == -1 and g == -1 and b == -1:
        return -1, -1, -1
    h, l, s = rgb_to_hls(r, g, b)
    return int(h), int(l), int(s)


def hls_to_cmyk(h, l, s):
    h = int(h)
    l = int(l)
    s = int(s)
    r, g, b = hls_to_rgb(h, l, s)
    if r == -1 and g == -1 and b == -1:
        return -1, -1, -1
    c, m, y, k = rgb_to_cmyk(r, g, b)
    return int(c), int(m), int(y), int(k)


def hex_to_rgb(hex_value):
    hex_value = hex_value.lstrip('#')
    rgb_tuple = tuple(int(hex_value[i:i+2], 16) for i in (0, 2, 4))

    return rgb_tuple
