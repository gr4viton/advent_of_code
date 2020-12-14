from puzzle_factory import PuzzleFactory
from aocd import lines

from typing import List
from pydantic import BaseModel


class SolverD2:
    year = 2020
    print_in_ = False

    def solve_a(self, in_):
        out = 69
        return out

    def solve_b(self, in_):
        out = 42
        return out

    def print(self, in_):
        if not in_:
            return
        print(f"count of numbers = {len(in_)}")
        if self.print_in_:
            print(in_)

    def test(self):
        print("> test")
        lin1 = ""
        self.test_it(self.solve_a, 2, lin1)
        self.test_it(self.solve_b, 1, lin1)

    def test_it(self, method, out, *args, **kwargs):
        got_out = method(*args, **kwargs)
        print(f"should: {out} | got: {got_out}")
        assert got_out == out



if __name__ == "__main__":
    """Load session.

    viz https://pypi.org/project/advent-of-code-data/
    and session: https://github.com/wimglenn/advent-of-code-wim/issues/1
    """
    DAY = None  # TODO change

    puzzle = None
    puzzle = PuzzleFactory(2020, DAY).get_puzzle()
    solver = SolverD2()

    in_ = lines
    a = solver.solve_a(in_)
    b = solver.solve_b(in_)

    print(">>>>>>>>>")
    print(f"solution 1 {a}")
    print(f"solution 2 {b}")
