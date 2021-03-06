from puzzle_factory import PuzzleFactory
from aocd import lines

from typing import List
from pydantic import BaseModel


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
        raise NotImplementedError()


class DirectiveD2A(Directive):
    def check_correctness(self, password):
        orig = len(password)
        without_letter = len(password.replace(self.letter, ""))
        letter_count = orig - without_letter
        return self.min_ <= letter_count <= self.max_


class DirectiveD2B(Directive):

    def _contains_letter(self, index, password):
        return password[index-1] == self.letter

    def check_correctness(self, password):
        """
        Each policy actually describes two positions in the password, where 1 means the first character, 2 means the second character, and so on. (Be careful; Toboggan Corporate Policies have no concept of "index zero"!) Exactly one of these positions must contain the given letter. Other occurrences of the letter are irrelevant for the purposes of policy enforcement.
        """
        # xor :)
        return self._contains_letter(self.min_, password) != self._contains_letter(self.max_, password)


class Line(BaseModel):
    line: str
    password: str
    directives: List[Directive]

    @property
    def is_correct(self):
        return all(dire.check_correctness(self.password) for dire in self.directives)

    @classmethod
    def from_line(cls, line, directive_cls=DirectiveD2A):

        words = line.split(" ")
        pwd = words.pop(-1)
        directives = []
        count_word = None
        for i, word in enumerate(words):
            is_count_word = not (i % 2)
            if is_count_word:
                count_word = word
            else:
                dire = directive_cls.from_words(count_word=count_word, letter_word=word)
                directives.append(dire)

        return cls(line=line, password=pwd, directives=directives)


class SolverX2:
    year = 2020
    print_nums = False

    def solve1(self, in_):
        lines = [Line.from_line(line) for line in in_]
        return sum(line.is_correct for line in lines)

    def solve2(self, in_):
        lines = [Line.from_line(line, directive_cls=DirectiveD2B) for line in in_]
        return sum(line.is_correct for line in lines)

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
        self.test_it(self.solve1, lin1, 2)
        self.test_it(self.solve2, lin1, 1)

    def test_it(self, method, lins, out):
        got_out = method(lins)
        print(f"should: {out} | got: {got_out}")
        assert got_out == out


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
    b = solver.solve2(in_)
    print(">>>>>>>>>")
    print(f"solution 1 | {a}")
    print(f"solution 2 | {b}")
