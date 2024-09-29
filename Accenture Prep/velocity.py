def velocity(h, v, vn):
    e = v/vn
    h = h * (e**2)
    return int(h)

print(velocity(10, 20, 5))
