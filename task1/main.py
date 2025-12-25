import argparse

def calc_path(n: int, m: int) -> list[int]:
    """
    Calculates the path.
    """
    mask = [i for i in range(1, n + 1)]
    head_i = 0
    ans = []

    while True:
        ans.append(mask[head_i])
        head_i = (head_i + m - 1) % n

        if head_i == 0:
            break

    return ans

def test_calc_path():
    (n, m) = 6, 3
    ans1 = calc_path(n, m)
    assert(ans1 == [1, 3, 5])

    (n, m) = 5, 4
    ans1 = calc_path(n, m)
    assert(ans1 == [1, 4, 2, 5, 3])

    (n, m) = 4, 2
    ans1 = calc_path(n, m)
    assert(ans1 == [1, 2, 3, 4])

    (n, m) = 6, 4
    ans1 = calc_path(n, m)
    assert(ans1 == [1, 4])

    print("test_calc_path passed!")

def solution(n1: int, m1: int, n2: int, m2: int) -> str:
    """
    Solution for task1. 
    """
    p1 = "".join([str(x) for x in calc_path(n1, m1)])
    p2 = "".join([str(x) for x in calc_path(n2, m2)])

    return p1 + p2

def test_solution():
    t1 = solution(6, 3, 5, 4)
    assert(t1 == "13514253")

    t2 = solution(4, 2, 6, 4)
    assert(t2 == "123414")

    print("test_solution passed!")


def init_argparser():
    parser = argparse.ArgumentParser("Task 1", "python ./main.py n1, m1, n2, m2\nfirst_tuple = (n1, m1), second_tuple = (n2, m2)")
    parser.add_argument("first_tuple", nargs=2, type=int, help="n1, m1")
    parser.add_argument("second_tuple", nargs=2, type=int, help="n2, m2")

    return parser

def main():
    # test_calc_path()
    # test_solution()

    parser = init_argparser()
    args = parser.parse_args()

    print(solution(args.first_tuple[0], args.first_tuple[1], args.second_tuple[0], args.second_tuple[1]))

if __name__ == "__main__":
    main()