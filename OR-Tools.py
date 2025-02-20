# or_tools_optimization.py
# Data: 2025-02-20
# Autorius: Mantas Kryževičius ir Agnė Bučytė

from ortools.linear_solver import pywraplp

def or_tools_optimization():
    """Sprendžia paprastą linijinį optimizavimo uždavinį su OR-Tools"""
    solver = pywraplp.Solver.CreateSolver('GLOP')

    # Kintamieji
    x = solver.NumVar(0, 10, 'x')
    y = solver.NumVar(0, 10, 'y')

    # Tikslo funkcija: Maksimizuoti 3x + 4y
    solver.Maximize(3 * x + 4 * y)

    # Apribojimai
    solver.Add(2 * x + y <= 14)
    solver.Add(4 * x - 5 * y >= -10)
    solver.Add(x - y <= 2)

    # Išspręsti problemą
    status = solver.Solve()

    if status == pywraplp.Solver.OPTIMAL:
        print('Optimalus sprendimas:')
        print(f'x = {x.solution_value()}, y = {y.solution_value()}')
        print('Maksimali vertė =', solver.Objective().Value())
    else:
        print('Optimalus sprendimas nerastas.')

or_tools_optimization()
