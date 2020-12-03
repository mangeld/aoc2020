from dataclasses import dataclass


@dataclass
class Slope:
    x: int
    y: int


def find_trees(orography: str, slope: Slope) -> int:
    orography_matrix = [[col for col in row] for row in orography.splitlines()]
    width = len(orography_matrix[0])
    height = len(orography_matrix)
    curr_pos = (0, 0)
    trees_found = 0
    while curr_pos[1] + 1 != height:
        x = curr_pos[0] + slope.x
        curr_pos = (
            x if x < width else slope.x - (width - curr_pos[0]),
            curr_pos[1] + slope.y
        )
        if orography_matrix[curr_pos[1]][curr_pos[0]] == '#':
            trees_found += 1
    return trees_found


if __name__ == "__main__":
    import sys
    with open(sys.argv[1]) as input_data:
        trees = find_trees(
            input_data.read(),
            Slope(int(sys.argv[2]), int(sys.argv[3]))
        )
        print("Found:", trees,"trees")