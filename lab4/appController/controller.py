import matplotlib.pyplot as plt


def step_by_step_algorithm(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    k = dy / dx
    x = x1
    y = y1
    answer = []
    while x <= x2:
        y += k
        x += 1
        answer.append((x, int(y)))

    return answer


def cda_algorithm(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    steps = max(abs(dx), abs(dy))
    xincrement = dx / steps
    yincrement = dy / steps
    x = x1
    y = y1
    points = [(x, y)]
    for i in range(steps):
        x += xincrement
        y += yincrement
        points.append((x, y))
    return points


def bresenham_algorithm(x1, y1, x2, y2):
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    x = x1
    y = y1
    xincrement = 1 if x2 > x1 else -1
    yincrement = 1 if y2 > y1 else -1
    if dx > dy:
        p = 2 * dy - dx
        for i in range(dx):
            yield (x, y)
            if p >= 0:
                y += yincrement
                p -= 2 * dx
            x += xincrement
            p += 2 * dy
    else:
        p = 2 * dx - dy
        for i in range(dy):
            yield (x, y)
            if p >= 0:
                x += xincrement
                p -= 2 * dy
            y += yincrement
            p += 2 * dx
    yield (x, y)


def bresenham_circle_algorithm(xc, yc, r):
    x = 0
    y = r
    delta = 1 - 2 * r
    error = 0

    answer = []

    while y >= x:
        answer.append((xc + x, yc + y))
        answer.append((xc + x, yc - y))
        answer.append((xc - x, yc + y))
        answer.append((xc - x, yc - y))

        answer.append((xc + y, yc + x))
        answer.append((xc + y, yc - x))
        answer.append((xc - y, yc + x))
        answer.append((xc - y, yc - x))

        error = 2 * (delta + y) - 1

        if (delta < 0) and (error <= 0):
            x += 1
            delta += 2 * x + 1
            continue

        if (delta > 0) and (error > 0):
            y -= 1
            delta -= 2 * y + 1
            continue

        x += 1
        y -= 1

        delta += 2 * (x - y)

    return answer
