# Sistem Persamaan Nonlinear - Metode Numerik

Halo! 👋  
Repositori ini adalah tugas metode numerik untuk menyelesaikan sistem persamaan nonlinear menggunakan **Python 3.x**.

## Installation

Clone the project

```bash
git clone https://github.com/felrfn/sistem-persamaan-nonlinear-metonum.git
cd sistem-persamaan-nonlinear-metonum
```

Install dependency

```bash
pip install -r requirements.txt
```

Run

```bash
python main.py
```

## Folder Structure

```
├── equations.py
├── main.py
├── README.md
├── requirements.txt
└── solvers
    ├── __init__.py
    ├── jacobi.py
    ├── newton_raphson.py
    ├── secant_quasi_newton.py
    └── seidel.py
```

---

## Content

```
Persamaan non-linear:
    f₁(x, y) = x² + xy - 10 = 0
    f₂(x, y) = y + 3xy² - 57 = 0

Tebakan awal:
    x₀ = 1.5
    y₀ = 3.5

Epsilon:
    ε = 0.000001

Solusi iterasi:
    g1B = √(10 - xₙ * yₙ)
    g2B = √((57 - yₙ) / (3 * g1B))
```

### Solvers

- Jacobi
- Newton-Raphson
- Secant
- Seidel

### Conclusion

`(Newton−Raphson ≈ Secant) > Seidel > Jacobi`
