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
    print_nums = False

    def solve1(self, nums):
        """

        Specifically, they need you to find the two entries that sum to 2020 and then multiply those two numbers together.

        a + b = 2020
        2020 - a = b
        """
        self.print_nums = True
        year = self.year
        print("start")

        pair = self.get_pair_which_sums_to_x(nums, year)
        assert pair is not None
        assert len(pair) == 2

        mult = pair[0] * pair[1]
        print(f"mult {mult}")
        return mult

    def _get_viable_list(self, nums, max_):
        if not nums:
            return None
        nums = sorted(list(filter(lambda num: self.viable(num, max_), nums)))
        nums = list(set(nums))
        return nums

    def get_pair_which_sums_to_x(self, nums, x):
        """Get pair of numbers from nums which in sum gives number x."""
        self.print(nums)

        nums = self._get_viable_list(nums, x)
        self.print(nums)

        subtracted_year = [x - num for num in nums]
        self.print(subtracted_year)
        subtracted_year = self._get_viable_list(subtracted_year, x)
        self.print(subtracted_year)

        num_2020 = list(set(nums) & set(subtracted_year))
        self.print(num_2020)

        if len(num_2020) == 2:
            return num_2020
        return None

    def solve2(self, nums):
        """In your expense report, what is the product of the three entries that sum to 2020?
        """
        year = self.year
        trio = self.get_trio_which_sums_to_x(nums, year)
        assert len(trio) == 3
        mult = trio[0] * trio[1] * trio[2]
        return mult

    def get_trio_which_sums_to_x(self, nums, x):
        """
        a + b + c = 2020
        d = a+b  # all combinations :(
        2020 - a = for each num in nums
        then find b+c from nums(without_a) which gives 2020-a
        """
        nums = self._get_viable_list(nums, x)
        for a in nums:
            wanted = x - a
            nums_wo_a = set(nums)
            nums_wo_a.discard(a)
            suc_pair = self.get_pair_which_sums_to_x(nums_wo_a, wanted)
            if suc_pair:
                solution = [a, *suc_pair]
                return solution


        return x


    @staticmethod
    def viable(nums, max_):
        if nums > max_ + 1:
            return False
        if nums <= 0:
            return False
        return True

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
    puzzle = PuzzleFactory(2020, 1).get_puzzle()
    x = SolverX1().solve1(in_numbers)

    y = SolverX1().solve2(in_numbers)
    print(">>>>>>>>>")
    print(f"solution 1 {x}")
    print(f"solution 2 {y}")

