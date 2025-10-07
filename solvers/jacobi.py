import numpy as np

from equations import g1B, g2B


def run_jacobi(x0, y0, tol, max_iter):
    """Metode Iterasi Jacobi."""
    print("--- Menjalankan Metode Jacobi ---")
    x_k, y_k = x0, y0
    for i in range(max_iter):
        x_k_plus_1 = g1B(y_k)
        y_k_plus_1 = g2B(x_k)

        error = np.sqrt((x_k_plus_1 - x_k) ** 2 + (y_k_plus_1 - y_k) ** 2)
        print(
            f"Iterasi {i+1}: x = {x_k_plus_1:.7f}, y = {y_k_plus_1:.7f}, Galat = {error:.7f}"
        )

        if error < tol:
            print(f"\nKonvergensi tercapai setelah {i+1} iterasi.")
            return x_k_plus_1, y_k_plus_1, i + 1

        x_k, y_k = x_k_plus_1, y_k_plus_1

    print(f"\nMetode Jacobi tidak konvergen dalam {max_iter} iterasi.")
    return None, None, max_iter
