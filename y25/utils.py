import datetime as dt
import pathlib
import runpy

def read_input(day: int, test: bool=False) -> list[str]:
    filename = "test.in"
    if not test:
        filename = "actual.in"


    with open(f"./d{day:02d}/{filename}", "r") as f:
       return f.readlines()

def create_day(day=dt.date.today().day):
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


def run_day(day=dt.date.today().day):
    # Check to see if day exists.
    folder = pathlib.Path(f"./d{day:02d}")
    if not folder.exists():
        print(f"Day {day} does not exist.")
        exit(1)
    
    # Import the day's module and run its main function.
    runpy.run_module(f"d{day:02d}.d{day:02d}", run_name="__main__")

def run_all():
    for day in range(1, 32):
        folder = pathlib.Path(f"./d{day:02d}")
        if folder.exists():
            print(f"Running Day {day}...")
            run_day(day)
