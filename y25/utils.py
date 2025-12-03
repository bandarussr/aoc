import datetime as dt
import importlib
import pathlib
import runpy

def read_input(day: int, test: bool=False) -> list[str]:
    filename = "test.in"
    if not test:
        filename = "actual.in"


    with open(f"./d{day:02d}/{filename}", "r") as f:
       return list(map(str.strip, f.readlines()))

def create_day(day: int=dt.date.today().day):
    if day < 1 or day > 12:
        print("Day must be between 1 and 12.")
        exit(1)

    print(f"Creating day {day}...")

    # Check to see if path already exists.
    folder = pathlib.Path(f"./d{day:02d}")
    if folder.exists():
        print(f"Day {day} already exists.")
        exit(1)

    with open("./template.py", "r") as t:
        template = t.read()

    # Create folder and copy template.
    folder.mkdir()
    with open(folder / f"d{day:02d}.py", "w") as f:
        f.write(template)
    
    # Create placeholders for test and actual input.
    test = folder / "test.in"
    test.touch()
    actual = folder / "actual.in"
    actual.touch()


def run_day(day: int=dt.date.today().day, test: bool=False):
    if day < 1 or day > 12:
        print("Day must be between 1 and 12.")
        exit(1)

    # Check to see if day exists.
    folder = pathlib.Path(f"./d{day:02d}")
    if not folder.exists():
        print(f"Day {day} does not exist.")
        exit(1)
    
    print(f"Running Day {day}...")

    # Import the day's module and run both stars.
    module = importlib.import_module(f"d{day:02d}.d{day:02d}")
    print(f"Star 1: {module.star1(test)}")
    print(f"Star 2: {module.star2(test)}")

def run_all(test: bool=False):
    for day in range(1, 13):
        folder = pathlib.Path(f"./d{day:02d}")
        if folder.exists():
            run_day(day, test)
