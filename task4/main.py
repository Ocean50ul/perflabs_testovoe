import argparse
import math
from pathlib import Path

def init_argparser():
    parser = argparse.ArgumentParser("Task 4", "python ./main.py file_path")
    parser.add_argument("file_path", type=str)

    return parser

def parse_file(file_path: Path) -> list[int]:
    ans = []
    with open(file_path, "r") as file:
        for line in file:
            try:
                num = int(line.strip())
                ans.append(num)
            except ValueError as e:
                raise Exception(f"Failed to parse line {line.strip()}: {e}")
            
    return ans


def test_parse_file():
    file_path = "./test_file.txt"

    with open(file_path, "w") as file:
        for i in range(0, 10):
            line = f"{i}\n"
            file.write(line)

    nums = parse_file(Path(file_path))
    assert(nums == [*range(0, 10)])

    print("Test passed!")
            

def calc_distance(arr: list[int], n: int) -> int:
    distance = 0
    for i in arr:
        distance += abs(n - i)
    return distance

def solution(arr: list[int]) -> int:
    '''
    Quadratic complexity.

        for number in min..max:
            traverse array to calculate distance
    '''
    mn = min(arr)
    mx = max(arr)

    min_distance = math.inf

    for i in range(mn, mx + 1):
        dist = calc_distance(arr, i)
        if dist < min_distance:
            min_distance = dist

    return min_distance

def test_solution():
    nums1 = [4, 5, 6]
    ans1 = solution(nums1)
    assert(ans1 == 2)

    nums1 = [3, 6, 8, 9]
    ans1 = solution(nums1)
    assert(ans1 == 8)

    nums1 = [1, 16, 3, 20]
    ans1 = solution(nums1)
    assert(ans1 > 20)

def test_end_to_end():
    parser = init_argparser()
    arg = parser.parse_args().file_path

    file_path = Path(arg)
    if not file_path.exists():
        raise Exception(f"File not found: {file_path}.")

    nums = parse_file(Path(file_path))
    assert(nums == [3, 6, 8, 9])
    ans = solution(nums)
    assert(ans == 8)

def main():
    # test_parse_file()
    # test_solution()
    # test_end_to_end()

    parser = init_argparser()
    arg = parser.parse_args().file_path

    file_path = Path(arg)
    if not file_path.exists():
        raise Exception(f"File not found: {file_path}.")
    
    arr = parse_file(file_path)
    ans = solution(arr)

    if ans > 20:
        print("20 ходов недостаточно для приведения всех элементов массива к одному числу")
        return

    print(ans)



if __name__ == "__main__":
    main()