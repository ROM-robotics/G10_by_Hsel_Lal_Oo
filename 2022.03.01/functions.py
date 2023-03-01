import numpy as np

def midpoint(x, y):
    return np.array([
        (x[0] + y[0]) / 2,
        (x[1] + y[1]) / 2
    ])

def distance(x, y):
    return np.sqrt(np.abs((x[0] - y[0]) ^ 2 + (x[1] - y[1]) ^ 2))

def slope(u, v):
    return (u[0] - v[0]) / (u[1] - v[1])

if __name__ == "__main__":
    print(midpoint(
        np.array([1, 1]), 
        np.array([3, 3])
    ))

    print(distance(
        np.array([1, 1]), 
        np.array([3, 3])
    ))

    print(slope(
        np.array([1, 1]), 
        np.array([3, 3])
    ))