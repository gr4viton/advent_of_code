from puzzle_factory import PuzzleFactory
from aocd import data, lines

from typing import List, Optional, ClassVar
from pydantic import BaseModel
from pydantic.dataclasses import dataclass


class Passport(BaseModel):
    birth_year: Optional[str]
    issue_year: Optional[str]
    expiry_year: Optional[str]
    height: Optional[str]
    hair_color: Optional[str]
    eye_color: Optional[str]
    passport_id: Optional[str]
    country_id: Optional[str]

    code_to_field: ClassVar[dict] = {
        "byr": "birth_year",
        "iyr": "issue_year",
        "eyr": "expiry_year",
        "hgt": "height",
        "hcl": "hair_color",
        "ecl": "eye_color",
        "pid": "passport_id",
        "cid": "country_id",
    }

    @property
    def is_valid(self):
        """Is this passport considered valid.

        Consider it valid if `country_id` is missing
        """
        checked_dict = dict(self)
        checked_dict.pop("country_id")
        all_checked_values_defined = all(value is not None for value in checked_dict.values())
        return all_checked_values_defined

    @classmethod
    def from_words(cls, words):
        dic = {}
        for word in words:
            word = word.strip()
            if not word:
                continue
            code, value = word.split(":")
            dic[code] = value

        kwargs = {
            cls.code_to_field[code]: value
            for code, value in dic.items()
            if code in cls.code_to_field
        }
        return cls(**kwargs)

    @classmethod
    def from_lines(cls, lines):
        words = lines.replace("\n", " ").split(" ")
        return cls.from_words(words)


class SolverD4:
    year = 2020
    print_in_ = False

    def create_passports(self, data):
        lines_of_passports = data.split("\n\n")
        return [Passport.from_lines(lines) for lines in lines_of_passports]

    def solve_a(self, in_):
        passports = self.create_passports(data=in_)
        valid_count = sum(pas.is_valid for pas in passports)
        out = valid_count
        return out

    def solve_b(self, in_):
        out = None
        return out

    def print(self, in_):
        if not in_:
            return
        print(f"count of numbers = {len(in_)}")
        if self.print_in_:
            print(in_)

    def test(self):
        print("> test")
        lin1 = """ecl:gry pid:860033327 eyr:2020 hcl:#fffffd
byr:1937 iyr:2017 cid:147 hgt:183cm

iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884
hcl:#cfa07d byr:1929

hcl:#ae17e1 iyr:2013
eyr:2024
ecl:brn pid:760753108 byr:1931
hgt:179cm

hcl:#cfa07d eyr:2025 pid:166559648
iyr:2011 ecl:brn hgt:59in
"""
        self.test_it(self.solve_a, 2, lin1)
        self.test_it(self.solve_b, 1, lin1)

    def test_it(self, method, out, *args, **kwargs):
        got_out = method(*args, **kwargs)
        if got_out is None:
            print("got None in test - skipping")
            return
        print(f"should: {out} | got: {got_out}")
        assert got_out == out


if __name__ == "__main__":
    """Load session.

    viz https://pypi.org/project/advent-of-code-data/
    and session: https://github.com/wimglenn/advent-of-code-wim/issues/1
    """
    DAY = 4  # TODO change

    puzzle = None
    puzzle = PuzzleFactory(2020, DAY).get_puzzle()
    solver = SolverD4()

    solver.test()

    in_ = data
    a = solver.solve_a(in_)
    b = solver.solve_b(in_)

    print(">>>>>>>>>")
    print(f"solution 1 {a}")
    print(f"solution 2 {b}")
