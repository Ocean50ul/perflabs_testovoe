import argparse
from dataclasses import dataclass
from fractions import Fraction
from pathlib import Path

@dataclass
class Ellipse:
    center: tuple[str]
    radii: tuple[str]

    def where(self, x: str, y: str) -> int:
        """
        0 - on the ellipse
        1 - inside the ellipse
        2 - outside the ellipse

        if ellipse is tilted, then the math wont work
        """

        x_f = Fraction(x)
        y_f = Fraction(y)
        h_f = Fraction(self.center[0])
        k_f = Fraction(self.center[1])
        a_f = Fraction(self.radii[0])
        b_f = Fraction(self.radii[1])

        magic_number = ((x_f - h_f) ** 2 / a_f ** 2) + ((y_f - k_f) ** 2 / b_f ** 2)

        if magic_number == 1:
            return 0
        elif magic_number < 1:
            return 1
        else:
            return 2

def get_stuff(file_path: Path) -> list[tuple[str]]:
    ans = []

    with open(file_path, "r") as file:
        for line in file:
            numbers = line.strip().split(" ")

            if len(numbers) != 2:
                raise Exception("Malformed file.")
            
            ans.append((numbers[0], numbers[1]))

    return ans

def test_where():
    eli_stuff = get_stuff(Path("./eli.txt"))
    points = get_stuff(Path("./points.txt"))

    ell = Ellipse(eli_stuff[0], eli_stuff[1])
    results = [ell.where(point[0], point[1]) for point in points]
    assert(results[0] == 0)
    assert(results[1] == 1)
    assert(results[2] == 2)

    print("test_where passed")

def init_argparser():
    parser = argparse.ArgumentParser("Task 2", "python ./main.py ellipse_path")
    parser.add_argument("ellipse_path", type=str)
    parser.add_argument("points_path", type=str)

    return parser

def main():
    # test_where()
    
    parser = init_argparser()
    args = parser.parse_args()

    eli_stuff_p = Path(args.ellipse_path)
    points_p = Path(args.points_path)

    if not eli_stuff_p.exists() or not points_p.exists():
        raise Exception("Wrong paths. Ha-ha!")

    eli_stuff = get_stuff(eli_stuff_p)
    points = get_stuff(points_p)
    ell = Ellipse(eli_stuff[0], eli_stuff[1])

    for point in points:
        where = ell.where(point[0], point[1])
        print(where)



if __name__ == "__main__":
    main()