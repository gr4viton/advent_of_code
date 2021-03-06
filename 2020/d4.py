from enum import Enum, auto
from typing import List, Optional, ClassVar

from puzzle_factory import PuzzleFactory
from aocd import data, lines

from pydantic import BaseModel, validator, Field, constr
from pydantic.dataclasses import dataclass


class PassportBase:

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

    @classmethod
    def from_words(cls, words):
        dic = {}
        for word in words:
            word = word.strip()
            if not word:
                continue
            code, value = word.split(":")
            dic[code] = value
        return cls.from_code_dict(dic)

    @classmethod
    def from_code_dict(cls, code_dict):
        kwargs = {
            cls.code_to_field[code]: value
            for code, value in code_dict.items()
            if code in cls.code_to_field
        }
        return cls(**kwargs)

    @classmethod
    def from_lines(cls, lines):
        words = lines.replace("\n", " ").split(" ")
        return cls.from_words(words)


class PassportA(PassportBase, BaseModel):
    birth_year: str
    issue_year: str
    expiry_year: str
    height: str
    hair_color: str
    eye_color: str
    passport_id: str
    country_id: Optional[str]


class Height(BaseModel):
    quantity: int
    unit: str
    _range_per_unit: ClassVar = {"cm": [150,193], "in":[59,76]}

    @classmethod
    def __get_validators__(cls):
        yield cls.validate
        yield cls.unit_and_quantity_validator

    @classmethod
    def unit_and_quantity_validator(cls, value):
        if value.unit not in cls._range_per_unit.keys():
            raise ValueError(f"unit has to be one of {cls._range_per_unit.keys()}")
        unit_range = cls._range_per_unit[value.unit]
        min_, max_ = unit_range
        if not (min_  <= value.quantity <= max_):
            raise ValueError(f"quantity [{value.quantity}] is not in selected unit [{value.unit}] range [{min_} : {max_}]")

    @classmethod
    def from_str(cls, txt):
        txt = txt.strip()
        quantity = txt[:-2]
        unit = txt[-2:]
        return cls(quantity=quantity, unit=unit)


class EyeColor(str, Enum):
    amb = "amb"
    blu = "blu"
    brn = "brn"
    gry = "gry"
    grn = "grn"
    hzl = "hzl"
    oth = "oth"


class PassportB(PassportBase, BaseModel):
    """

    byr (Birth Year) - four digits; at least 1920 and at most 2002.
    iyr (Issue Year) - four digits; at least 2010 and at most 2020.
    eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
    hgt (Height) - a number followed by either cm or in:
        If cm, the number must be at least 150 and at most 193.
        If in, the number must be at least 59 and at most 76.
    hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
    ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
    pid (Passport ID) - a nine-digit number, including leading zeroes.
    cid (Country ID) - ignored, missing or not.

    """
    birth_year: int = Field(type=int, ge=1920, le=2002)
    issue_year: int = Field(type=int, ge=2010, le=2020)
    expiry_year: int = Field(type=int, ge=2020, le=2030)
    height: Height
    hair_color: constr(regex=r'^#(?:[0-9a-f]{6})$')
    eye_color: EyeColor
    passport_id: constr(regex=r'^(?:[0-9]{9})$')
    country_id: Optional[str]

    @classmethod
    def from_code_dict(cls, code_dict):
        kwargs = {
            cls.code_to_field[code]: value
            for code, value in code_dict.items()
            if code in cls.code_to_field
        }
        key = "height"
        kwargs[key] = dict(Height.from_str(kwargs[key]))
        return cls(**kwargs)


class SolverD4:
    year = 2020
    print_in_ = False

    def create_valid_passports(self, data, passport_cls=PassportA):
        lines_of_passports = data.split("\n\n")

        passports = []
        for lines in lines_of_passports:
            try:
                passport = passport_cls.from_lines(lines)
            except Exception as exc:
                # print(exc)  # debug
                continue
            if not passport:
                continue
            passports.append(passport)

        return passports

    def solve_a(self, in_):
        passports = self.create_valid_passports(data=in_)
        valid_count = len(passports)
        out = valid_count
        return out

    def solve_b(self, in_):
        passports = self.create_valid_passports(data=in_, passport_cls=PassportB)
        valid_count = len(passports)
        out = valid_count
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
        b_inv = """
eyr:1972 cid:100
hcl:#18171d ecl:amb hgt:170 pid:186cm iyr:2018 byr:1926

iyr:2019
hcl:#602927 eyr:1967 hgt:170cm
ecl:grn pid:012533040 byr:1946

hcl:dab227 iyr:2012
ecl:brn hgt:182cm pid:021572410 eyr:2020 byr:1992 cid:277

hgt:59cm ecl:zzz
eyr:2038 hcl:74454a iyr:2023
pid:3556412378 byr:2007"""
        b_val = """pid:087499704 hgt:74in ecl:grn iyr:2012 eyr:2030 byr:1980
hcl:#623a2f

eyr:2029 ecl:blu cid:129 byr:1989
iyr:2014 pid:896056539 hcl:#a97842 hgt:165cm

hcl:#888785
hgt:164cm byr:2001 iyr:2015 cid:88
pid:545766238 ecl:hzl
eyr:2022

iyr:2010 hgt:158cm hcl:#b6652a ecl:blu byr:1944 eyr:2021 pid:093154719"""

        self.test_it(self.solve_a, 2, lin1)
        self.test_it(self.solve_a, 254, data)
        self.test_it(self.solve_b, 0, b_inv)
        self.test_it(self.solve_b, 4, b_val)

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

    a = b = None
    in_ = data
    a = solver.solve_a(in_)
    b = solver.solve_b(in_)

    print(">>>>>>>>>")
    print(f"solution 1 | {a}")
    print(f"solution 2 | {b}")
    solver.test()
