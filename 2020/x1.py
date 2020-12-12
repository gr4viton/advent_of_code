from aocd import data
from aocd.models import Puzzle

from dataclasses import dataclass

@dataclass
class PuzzleFactory:
    year: int
    day: int

    def get_puzzle(self):
        puzzle = Puzzle(year=self.year, day=self.day)
        return puzzle


# from aocd import submit
# my_answer = 42
# submit(my_answer, part="a", day=25, year=2017)


# from aocd.models import Puzzle
# puzzle = Puzzle(year=2017, day=20)
# puzzle
# # <Puzzle(2017, 20) at 0x107322978 - Particle Swarm>
# puzzle.input_data

# class SolverX1:

def aaa():
    """

    Specifically, they need you to find the two entries that sum to 2020 and then multiply those two numbers together.
    """

def main(puzzle):
    print("start")
    pass


if __name__ == "__main__":
    """Load session.

    viz https://pypi.org/project/advent-of-code-data/
    and session: https://github.com/wimglenn/advent-of-code-wim/issues/1
    """

    puzzle = None
    puzzle = PuzzleFactory(2020, 1).get_puzzle()
    main(puzzle)
