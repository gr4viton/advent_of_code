from puzzle_factory import PuzzleFactory
from aocd import lines

import pandas as pd
from dataclasses import dataclass

from typing import List
from pydantic import BaseModel


class Slope(BaseModel):
    x: int
    y: int

    @classmethod
    def from_right_down(cls, right, down):
        return cls(x=right, y=down)


@dataclass
class Map:
    df: pd.DataFrame

    @classmethod
    def _init_row(cls, line):
        line = line.replace("#", "1").replace(".", "0")
        line = list(int(char) for char in line)
        return pd.Series(line)

    @classmethod
    def from_lines(cls, lines):
        map_ = pd.DataFrame(lines)
        map_ = map_[0].apply(lambda line: cls._init_row(line))
        print(map_.shape)
        return cls(df=map_)

    def get_tree_count(self, slope):
        terrain = self.get_passed_terrain(slope)
        tree_count = sum(terrain)
        return tree_count

    def get_passed_terrain(self, slope):
        """

        x = (x + slope.x) % cols
        0123401234
        x
           x
         x    x
            x    x
        slope.x = 3
        0 = (0+3) % 5 = 3
        3 = (3+3) % 5 = 1
        1 = (1+3) % 5 = 4
        """
        cols = self.df.shape[1]
        print(f"cols={cols}")
        x = 0
        points = []
        for i, row in self.df.iterrows():
            point = row[x]
            points.append(point)
            x = (x + slope.x) % cols

        return points


class SolverD3:
    year = 2020
    print_in_ = False
    def __init__(self, slops=None):
        self.slops = slops

    def solve_a(self, in_):
        map_ = Map.from_lines(in_)
        x, y = 3, 1
        slope = Slope.from_right_down(x, y)
        tree_count = map_.get_tree_count(slope)
        return tree_count

    def solve_b(self, in_, slops=None):
        """
        slops = list of lists [x,y]
        """
        if slops is None:
            slops = self.slops
        map_ = Map.from_lines(in_)
        slopes = [Slope.from_right_down(x, y) for x, y in slops]
        mult = 1
        for slope in slopes:
            tree_count = map_.get_tree_count(slope)
            mult *= tree_count
        return mult

    def print(self, in_):
        if not in_:
            return
        print(f"count of numbers = {len(in_)}")
        if self.print_in_:
            print(in_)

    def test(self):
        print("> test")
        lin1 = """..##.......
#...#...#..
.#....#..#.
..#.#...#.#
.#...##..#.
..#.##.....
.#.#.#....#
.#........#
#.##...#...
#...##....#
.#..#...#.#"""
        lin1 = lin1.splitlines()
        lin2 = ["".join([lin, lin]) for lin in lin1]
        self.test_it(self.solve_a, 7, lin1)
        self.test_it(self.solve_a, 7, lin2)
        self.test_it(self.solve_b, 336, lin1, self.slops)
        self.test_it(self.solve_b, 336, lin2, self.slops)

    def test_it(self, method, out, *args, **kwargs):
        got_out = method(*args, **kwargs)
        print(f"should: {out} | got: {got_out}")
        assert got_out == out


if __name__ == "__main__":
    """Load session.

    viz https://pypi.org/project/advent-of-code-data/
    and session: https://github.com/wimglenn/advent-of-code-wim/issues/1

    https://adventofcode.com/2020/day/3
    """
    DAY = 3  # TODO change

    puzzle = None
    puzzle = PuzzleFactory(2020, DAY).get_puzzle()

    slops = [[1, 1], [3, 1], [5, 1], [7, 1], [1, 2]]
    solver = SolverD3(slops=slops)

    in_ = lines

    solver.test()
    a = solver.solve_a(in_)
    b = solver.solve_b(in_)

    print(">>>>>>>>>")
    print(f"solution 1 {a}")
    print(f"solution 2 {b}")
