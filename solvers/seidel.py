import numpy as np

from equations import g1B, g2B


def run_seidel(x0, y0, tol, max_iter):
    """Metode Iterasi Gauss-Seidel."""
    print("\n--- Menjalankan Metode Seidel ---")
    x_k, y_k = x0, y0
    for i in range(max_iter):
        x_prev, y_prev = x_k, y_k

        x_k = g1B(y_k)
        y_k = g2B(x_k)  # Langsung gunakan x_k yang baru

        error = np.sqrt((x_k - x_prev) ** 2 + (y_k - y_prev) ** 2)
        print(f"Iterasi {i+1}: x = {x_k:.7f}, y = {y_k:.7f}, Galat = {error:.7f}")

        if error < tol:
            print(f"\nKonvergensi tercapai setelah {i+1} iterasi.")
            return x_k, y_k, i + 1

    print(f"\nMetode Seidel tidak konvergen dalam {max_iter} iterasi.")
    return None, None, max_iter
