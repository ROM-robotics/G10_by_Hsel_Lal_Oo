import numpy as np

def midpoint(
    point1: np.ndarray[float, float],
    point2: np.ndarray[float, float]
) -> np.ndarray[float, float]:
    return np.array([
        (point1[0] + point2[0]) / 2,
        (point1[1] + point2[1]) / 2
    ])

def distance(
    point1: np.ndarray[float, float],
    point2: np.ndarray[float, float]
) -> float:
    return np.sqrt(np.abs(
        ((point2[0] - point1[0]) ^ 2) +
        ((point2[1] - point1[1]) ^ 2)
    ))

def slope(
    point1: np.ndarray[float, float],
    point2: np.ndarray[float, float]
) -> float: return (point2[1] - point1[1]) / (point2[0] - point1[0])

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