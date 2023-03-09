import sys
sys.path.append('../2023.03.01')

from typing import Tuple
import numpy as np
import sympy as sp
import functions as la_funcs

def slope_and_point_to_equation(
    slope: float,
    point: np.ndarray[float, float]
) -> sp.Equality:
    # Put values into variables to make things clearer
    m = slope
    x = point[0]
    y = point[1]

    # Calculate mx and c
    mx = m * x
    c = y - mx
    
    # Turn x and y into symbols and return the equation
    x, y = sp.symbols('x y')
    return sp.Eq(y, (m * x) + c)

def point_pairs_to_slope_and_equation(
    point1: np.ndarray[float, float],
    point2: np.ndarray[float, float]
) -> Tuple[float, sp.Equality]:
    slope = la_funcs.slope(point1, point2)
    equation = slope_and_point_to_equation(slope, point1)

    return (slope, equation)

if __name__ == "__main__":
    equations = [
        slope_and_point_to_equation(5, np.array([2, 9])),
        slope_and_point_to_equation(1, np.array([1, -2])),
        slope_and_point_to_equation(-3, np.array([-1, 6])),
        slope_and_point_to_equation(-2, np.array([-1, 4]))
    ]
    print(
        equations[0].evalf(subs = { sp.Symbol('x'): 2 }),
        equations[1].evalf(subs = { sp.Symbol('x'): 1 }),
        equations[2].evalf(subs = { sp.Symbol('x'): -1 }),
        equations[3].evalf(subs = { sp.Symbol('x'): -1 }),
    )

    print()

    slope_and_equations = [
        point_pairs_to_slope_and_equation(np.array([2, 4]), np.array([6, 8])),
        point_pairs_to_slope_and_equation(np.array([-3, 5]), np.array([6, -1])),
        point_pairs_to_slope_and_equation(np.array([-2, 1]), np.array([-4, -2])),
    ]
    for slope_and_equation in slope_and_equations:
        print(slope_and_equation)