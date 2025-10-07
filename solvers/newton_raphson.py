import numpy as np

from equations import f1, f2, jacobian


def run_newton_raphson(x0, y0, tol, max_iter):
    """Metode Newton-Raphson untuk sistem persamaan non-linear."""
    print("\n--- Menjalankan Metode Newton-Raphson ---")
    xk = np.array([x0, y0], dtype=float)

    for i in range(max_iter):
        J = jacobian(xk[0], xk[1])
        F = np.array([f1(xk[0], xk[1]), f2(xk[0], xk[1])])

        delta_x = np.linalg.solve(J, -F)
        xk_plus_1 = xk + delta_x

        error = np.linalg.norm(delta_x, 2)
        print(
            f"Iterasi {i+1}: x = {xk_plus_1[0]:.7f}, y = {xk_plus_1[1]:.7f}, Galat = {error:.7f}"
        )

        if error < tol:
            print(f"\nKonvergensi tercapai setelah {i+1} iterasi.")
            return xk_plus_1[0], xk_plus_1[1], i + 1

        xk = xk_plus_1

    print(f"\nMetode Newton-Raphson tidak konvergen dalam {max_iter} iterasi.")
    return None, None, max_iter
