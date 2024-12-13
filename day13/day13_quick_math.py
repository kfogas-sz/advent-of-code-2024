import re
import sympy as sp

PATTERN = r"\b\d+\b"

if __name__ == "__main__":
    tokens_part1 = 0
    tokens_part2 = 0
    x, y = sp.symbols('x y', integer=True)

    with open(r"day13\input") as f:
        machines = f.read().split("\n\n")

    for machine in machines:
        machine = machine.split("\n")

        machine_iter = iter(machine)

        matches = re.findall(PATTERN, next(machine_iter))
        ax, ay = map(int, matches)

        matches = re.findall(PATTERN, next(machine_iter))
        bx, by = map(int, matches)

        matches = re.findall(PATTERN, next(machine_iter))
        prize_x, prize_y = map(int, matches)

        eq1_part1 = sp.Eq(ax*x + bx*y, prize_x)
        eq2_part1 = sp.Eq(ay*x + by*y, prize_y)

        eq1_part2 = sp.Eq(ax*x + bx*y, 10000000000000 + prize_x)
        eq2_part2 = sp.Eq(ay*x + by*y, 10000000000000 + prize_y)

        solutions = sp.solve((eq1_part1, eq2_part1), (x, y))

        if solutions:
            tokens_part1 += (solutions[x]*3 + solutions[y]*1)

        solutions = sp.solve((eq1_part2, eq2_part2), (x, y))

        if solutions:
            tokens_part2 += (solutions[x]*3 + solutions[y]*1)

    print(tokens_part1)
    print(tokens_part2)
