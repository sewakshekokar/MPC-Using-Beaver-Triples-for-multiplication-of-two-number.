# Secure Multiplication with Beaver Triples (3-Party MPC)

This project implements a simple **3-Party Secure Multiplication** protocol using **Beaver Triples** for secure computation without revealing the inputs.  
It demonstrates **socket-based communication** between parties in Python.

## 📌 Overview
- **P0**: Holds shares `x0`, `y0` of secret inputs `x` and `y`.
- **P1**: Holds shares `x1`, `y1` of the same inputs.
- **P2 (Helper)**: Generates a Beaver triple `(a, b, c)` where `c = a * b`, splits it into shares, sends to P0 and P1, then exits.
- All computations are done **without revealing** the actual inputs to any party.

The final multiplication is done **in secret-shared form** — no party learns the full product unless shares are combined.

---

## ⚙️ Workflow Diagram


     ┌──────────┐
     │   P2     │
     │ (Helper) │
     └────┬─────┘
          │  Generates (a, b, c) with c = a*b
          │  Splits into (a0,b0,c0) & (a1,b1,c1)
          │
┌─────────▼──────────┐            ┌─────────▼──────────┐
│        P0           │<----------│        P1           │
│ x0, y0, a0,b0,c0    │ Exchange  │ x1, y1, a1,b1,c1    │
│ Compute d0, e0      │   d, e    │ Compute d1, e1      │
│ Final z0            │          │ Final z1            │
└─────────────────────┘          └─────────────────────┘

## 📂 File Structure

---

## ⚙️ How It Works
1. **P2** generates random values `a` and `b`, computes `c = a * b`.
2. P2 secret-shares `(a, b, c)` between P0 and P1.
3. **P0** and **P1** compute:
   - `d = x - a`
   - `e = y - b`
4. They exchange `d` and `e` values.
5. Each computes their share of the final result:
6. The product `x * y` can be reconstructed as `z0 + z1`.

---

## 🚀 Running the Code
Open **three terminals**:

**Terminal 1 (P0):**
```bash
python3 p0.py
python3 p1.py
python3 p2_helper.py'''

## References:
Pragmatic MPC
