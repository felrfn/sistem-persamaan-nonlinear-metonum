import numpy as np

from equations import f1, f2


def approximate_jacobian(x, y, h=1e-6):
    """Menghitung aproksimasi Jacobian menggunakan beda hingga."""
    J_approx = np.zeros((2, 2))

    f_val_plus_h_x = np.array([f1(x + h, y), f2(x + h, y)])
    f_val_minus_h_x = np.array([f1(x - h, y), f2(x - h, y)])
    J_approx[:, 0] = (f_val_plus_h_x - f_val_minus_h_x) / (2 * h)

    f_val_plus_h_y = np.array([f1(x, y + h), f2(x, y + h)])
    f_val_minus_h_y = np.array([f1(x, y - h), f2(x, y - h)])
    J_approx[:, 1] = (f_val_plus_h_y - f_val_minus_h_y) / (2 * h)

    return J_approx


def run_secant_quasi_newton(x0, y0, tol, max_iter):
    """Metode Secant (Quasi-Newton) menggunakan aproksimasi Jacobian."""
    print("\n--- Menjalankan Metode Secant (Quasi-Newton) ---")
    xk = np.array([x0, y0], dtype=float)

    for i in range(max_iter):
        J_approx = approximate_jacobian(xk[0], xk[1])
        F = np.array([f1(xk[0], xk[1]), f2(xk[0], xk[1])])

        if np.linalg.det(J_approx) == 0:
            print("Jacobian aproksimasi singular. Metode dihentikan.")
            return None, None, i + 1

        delta_x = np.linalg.solve(J_approx, -F)
        xk_plus_1 = xk + delta_x

        error = np.linalg.norm(delta_x, 2)
        print(
            f"Iterasi {i+1}: x = {xk_plus_1[0]:.7f}, y = {xk_plus_1[1]:.7f}, Galat = {error:.7f}"
        )

        if error < tol:
            print(f"\nKonvergensi tercapai setelah {i+1} iterasi.")
            return xk_plus_1[0], xk_plus_1[1], i + 1

        xk = xk_plus_1

    print(f"\nMetode Secant tidak konvergen dalam {max_iter} iterasi.")
    return None, None, max_iter
