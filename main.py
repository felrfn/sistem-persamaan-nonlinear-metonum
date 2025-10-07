from equations import f1, f2
from solvers.jacobi import run_jacobi
from solvers.newton_raphson import run_newton_raphson
from solvers.secant_quasi_newton import run_secant_quasi_newton
from solvers.seidel import run_seidel

# --- Konfigurasi Awal ---
X0 = 1.5
Y0 = 3.5
EPSILON = 0.000001
MAX_ITER = 100


def main():
    """Fungsi utama untuk menjalankan semua solver dan menampilkan hasil."""
    results = {}
    results["jacobi"] = run_jacobi(X0, Y0, EPSILON, MAX_ITER)
    results["seidel"] = run_seidel(X0, Y0, EPSILON, MAX_ITER)
    results["newton"] = run_newton_raphson(X0, Y0, EPSILON, MAX_ITER)
    results["secant"] = run_secant_quasi_newton(X0, Y0, EPSILON, MAX_ITER)

    # --- Tampilkan Ringkasan Hasil ---
    print("\n\n" + "=" * 40)
    print("           RINGKASAN HASIL")
    print("=" * 40)
    print(f"Tebakan Awal: x0 = {X0}, y0 = {Y0}")
    print(f"Toleransi Galat: {EPSILON}")
    print("-" * 40)

    labels = {
        "jacobi": "Metode Jacobi",
        "seidel": "Metode Seidel",
        "newton": "Metode Newton-Raphson",
        "secant": "Metode Secant (Quasi-Newton)",
    }

    for method, result in results.items():
        x_res, y_res, iters = result
        if x_res is not None:
            print(f"{labels[method]}:")
            print(f"  -> Solusi: x = {x_res:.7f}, y = {y_res:.7f}")
            print(f"  -> Iterasi: {iters}")
            final_error_f1 = f1(x_res, y_res)
            final_error_f2 = f2(x_res, y_res)
            print(f"  -> Residu f1: {final_error_f1:.2e}, f2: {final_error_f2:.2e}")
        else:
            print(f"{labels[method]}: TIDAK KONVERGEN")
        print("-" * 40)


if __name__ == "__main__":
    main()
