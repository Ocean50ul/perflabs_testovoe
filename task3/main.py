import argparse
import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any

@dataclass
class TaskPaths:
    tests_path: Path
    values_path: Path
    report_path: Path

    @classmethod
    def from_args(cls, args: list[str]) -> 'TaskPaths':
        found_paths = {}

        for path_str in args:
            path = Path(path_str)

            if not path.exists():
                raise Exception(f"File path {path_str} does not exist.")
            
            name = path.name.lower()
            if "tests" in name:
                found_paths["tests_path"] = path
            elif "values" in name:
                found_paths["values_path"] = path
            elif "report" in name:
                found_paths["report_path"] = path
            else:
                raise Exception(f"Malformed file name: {path.name}. Should be either 'report.json', 'tests.json' or 'values.json'")
            
        return cls(**found_paths)


def test_from_args():
    args = ["./report.json", "./tests.json", "./values.json"]
    paths = TaskPaths.from_args(args)

    assert(paths.tests_path == Path("./tests.json"))
    assert(paths.values_path == Path("./values.json"))
    assert(paths.report_path == Path("./report.json"))

    print("test_from_args passed")

def parse_values(values_path: Path) -> dict[int, str]:
    normal_dict = {}

    with open(values_path, "r") as file:
        prsd: dict[Any] = json.load(file)
        
        values: list[dict[str, Any]] = prsd.get("values")
        if not values:
            raise ValueError("Malformed values.json, should contain 'values' object.")
        
        for stupid_dict in values:
            id = stupid_dict.get("id")
            value = stupid_dict.get("value")
            
            if not (id or value):
                raise ValueError("Malformed values.json, values should contain objects with 'id' and 'value'.")
            
            normal_dict[id] = value
    
    return normal_dict


def inject_values(tests_json: list[dict[str, Any]], values: dict[int, str]):
    for item in tests_json:

        obj_id: int = item.get("id")
        if obj_id in values and "value" in item:
            item["value"] = values.get(obj_id)

        inner_values = item.get("values")
        if inner_values:
            inject_values(inner_values, values)
            


def init_argparser():
    parser = argparse.ArgumentParser("Task 3", "python ./main.py test_path values_path report_path")
    parser.add_argument("file_paths", nargs=3, type=str)
    
    return parser

def main():
    parser = init_argparser()
    args = parser.parse_args()
    
    paths = TaskPaths.from_args(args.file_paths)

    values = parse_values(paths.values_path)

    with open(paths.tests_path, "r") as file:
        prsd: dict[Any] = json.load(file)
        tests_stuff = prsd.get("tests")

        if not tests_stuff:
            raise ValueError("Malformed tests.json, should contain 'tests' object.")

        inject_values(tests_stuff, values)

        with open(paths.report_path, "w") as f2:
            json.dump(prsd, f2, indent=4)


if __name__ == "__main__":
    main()