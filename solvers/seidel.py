import numpy as np

from equations import g1B, g2B


def run_seidel(x0, y0, tol, max_iter):
    print("\n--- Menjalankan Metode Seidel ---")
    x_k, y_k = x0, y0
    for i in range(max_iter):
        x_prev, y_prev = x_k, y_k

        x_k = g1B(x_prev, y_prev)
        y_k = g2B(x_k, y_prev)

        if np.isnan(x_k) or np.isnan(y_k):
            print("Error: Hasil perhitungan NaN (Not a Number). Iterasi dihentikan.")
            return None, None, i + 1

        error = np.sqrt((x_k - x_prev) ** 2 + (y_k - y_prev) ** 2)
        print(f"Iterasi {i+1}: x = {x_k:.7f}, y = {y_k:.7f}, Galat = {error:.7f}")

        if error < tol:
            print(f"\nKonvergensi tercapai setelah {i+1} iterasi.")
            return x_k, y_k, i + 1

    print(f"\nMetode Seidel tidak konvergen dalam {max_iter} iterasi.")
    return None, None, max_iter
