from aocd.models import Puzzle
from aocd import lines

from dataclasses import dataclass
from typing import List
from pydantic import BaseModel

@dataclass
class PuzzleFactory:
    year: int
    day: int

    def get_puzzle(self):
        puzzle = Puzzle(year=self.year, day=self.day)
        return puzzle


class Directive(BaseModel):
    letter: str
    min_: int
    max_: int
    @classmethod
    def from_words(cls, count_word: str, letter_word: str):
        assert len(letter_word) == 2
        letter = letter_word.replace(":", "")
        assert isinstance(count_word, str)
        numbers = [int(num_word) for num_word in count_word.split("-")]
        min_, max_ = numbers
        return cls(letter=letter, min_=min_, max_=max_)

    def check_correctness(self, password):
        orig = len(password)
        without_letter = len(password.replace(self.letter, ""))
        letter_count = orig - without_letter
        return self.min_ <= letter_count <= self.max_


@dataclass
class Line:
    line: str
    password: str
    directives: List[Directive]

    @property
    def is_correct(self):
        return all(dire.check_correctness(self.password) for dire in self.directives)

    @classmethod
    def from_line(cls, line):

        words = line.split(" ")
        pwd = words.pop(-1)
        directives = []
        count_word = None
        for i, word in enumerate(words):
            is_count_word = not (i % 2)
            if is_count_word:
                count_word = word
            else:
                dire = Directive.from_words(count_word=count_word, letter_word=word)
                directives.append(dire)

        return cls(line=line, password=pwd, directives=directives)


class SolverX2:
    year = 2020
    print_nums = False

    def solve1(self, in_):
        lines = [Line.from_line(line) for line in in_]
        __import__('pudb').set_trace()
        return sum(line.is_correct for line in lines)

    def solve2(self, in_):
        pass

    def print(self, in_):
        if not in_:
            return
        print(f"count of numbers = {len(in_)}")
        if self.print_nums:
            print(in_)

    def test(self):
        print("> test")
        lin1 = """1-3 a: abcde
1-3 b: cdefg
2-9 c: ccccccccc
""".splitlines()
        x1 = self.solve1(lin1)
        print(x1)
        assert x1 == 2



if __name__ == "__main__":
    """Load session.

    viz https://pypi.org/project/advent-of-code-data/
    and session: https://github.com/wimglenn/advent-of-code-wim/issues/1
    """

    puzzle = None
    puzzle = PuzzleFactory(2020, 2).get_puzzle()
    solver = SolverX2()
    solver.test()
    in_ = lines
    a = b = None
    a = solver.solve1(in_)
    # b = solver.solve2(in_)
    print(">>>>>>>>>")
    print(f"solution 1 | {a}")
    print(f"solution 2 | {b}")
