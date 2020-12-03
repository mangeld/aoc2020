from . import day3


OROGRAPHY = """..##.......
#...#...#..
.#....#..#.
..#.#...#.#
.#...##..#.
..#.##.....
.#.#.#....#
.#........#
#.##...#...
#...##....#
.#..#...#.#
"""


def test_find_trees():
    assert day3.find_trees(OROGRAPHY, day3.Slope(3, 1)) == 7