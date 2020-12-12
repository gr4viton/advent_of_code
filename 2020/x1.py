from aocd.models import Puzzle
from aocd import numbers as in_numbers

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

class SolverX1:
    year = 2020

    def main(self, in_numbers):
        """

        Specifically, they need you to find the two entries that sum to 2020 and then multiply those two numbers together.
        """
        print("start")
        nums = in_numbers

        self.print(nums)

        max_ = 2001
        nums = sorted(list(filter(self.viable, set(nums))))
        self.print(nums)

        subtracted_year = [self.year - x for x in nums]
        self.print(subtracted_year)
        subtracted_year = list(filter(self.viable, subtracted_year))
        self.print(subtracted_year)

        num_2020 = list(set(nums) & set(subtracted_year))
        self.print(num_2020)

        assert len(num_2020) == 2

        mult = num_2020[0] * num_2020[1]
        print(f"mult {mult}")
        return mult

    def get_solution(self, in_numbers):
        return self.main(in_numbers)

    @staticmethod
    def viable(nums):
        if nums > 2001:
            return False
        if nums <= 0:
            return False
        return True

    def print(self, nums):
        print(f"count of numbers = {len(nums)}")
        print(nums)


if __name__ == "__main__":
    """Load session.

    viz https://pypi.org/project/advent-of-code-data/
    and session: https://github.com/wimglenn/advent-of-code-wim/issues/1
    """

    puzzle = None
    puzzle = PuzzleFactory(2020, 1).get_puzzle()
    x = SolverX1().get_solution(in_numbers)
