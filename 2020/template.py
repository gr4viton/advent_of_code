from aocd.models import Puzzle
from aocd import lines

from dataclasses import dataclass

@dataclass
class PuzzleFactory:
    year: int
    day: int

    def get_puzzle(self):
        puzzle = Puzzle(year=self.year, day=self.day)
        return puzzle

class SolverX2:
    year = 2020
    print_nums = False

    def solve1(self, nums):
        pass

    def solve2(self, nums):
        pass

    def print(self, nums):
        if not nums:
            return
        print(f"count of numbers = {len(nums)}")
        if self.print_nums:
            print(nums)


if __name__ == "__main__":
    """Load session.

    viz https://pypi.org/project/advent-of-code-data/
    and session: https://github.com/wimglenn/advent-of-code-wim/issues/1
    """

    puzzle = None
    puzzle = PuzzleFactory(2020, 2).get_puzzle()
    solver = SolverX2()
    in_ = lines
    a = solver.solve1(in_)
    b = solver.solve2(in_)
    print(">>>>>>>>>")
    print(f"solution 1 {a}")
    print(f"solution 2 {b}")
