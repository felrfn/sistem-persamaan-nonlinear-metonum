import numpy as np

# --- Definisi Fungsi Awal (f1 dan f2) ---
def f1(x, y):
    """f1(x, y) = x^2 + xy - 10 = 0"""
    return x**2 + x * y - 10

def f2(x, y):
    """f2(x, y) = y + 3xy^2 - 57 = 0"""
    return y + 3 * x * y**2 - 57

# --- Definisi Fungsi Iterasi untuk Jacobi/Seidel ---
def g1B(y):
    """g1B berasal dari f2 -> x = (57 - y) / (3y^2)"""
    if y == 0:
        return float('inf')
    return (57 - y) / (3 * y**2)

def g2B(x):
    """g2B berasal dari f1 -> y = (10 - x^2) / x"""
    if x == 0:
        return float('inf')
    return (10 - x**2) / x

# --- Definisi Jacobian Analitik untuk Newton-Raphson ---
def jacobian(x, y):
    """
    Menghitung matriks Jacobian J(x, y).
    J = [[df1/dx, df1/dy],
         [df2/dx, df2/dy]]
    """
    df1_dx = 2 * x + y
    df1_dy = x
    df2_dx = 3 * y**2
    df2_dy = 1 + 6 * x * y
    return np.array([[df1_dx, df1_dy], [df2_dx, df2_dy]])
