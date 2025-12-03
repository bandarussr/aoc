import argparse

from utils import create_day, run_all, run_day

def main():
    parser = argparse.ArgumentParser(
        description="A cli to help with running and managing input for AoC Y25."
    )
    sub = parser.add_subparsers(dest="command", help="command to execute")

    # Create
    create = sub.add_parser("create", help="create a day")
    create.add_argument("-d", "--day", type=int, help="day to create (1-31)", default=None)

    # Run
    run = sub.add_parser("run", help="run a day")
    run.add_argument("-d", "--day", type=int, help="day to run (1-31)", default=None)

    # Run all
    sub.add_parser("runall", help="runs all the days")

    args = parser.parse_args()

    # Handle args
    match args.command:
        case "create":
            if args.day is not None:
                create_day(args.day)
            else:
                create_day()

        case "run":
            if args.day is not None:
                run_day(args.day)
            else:
                run_day()

        case "runall":
            run_all()

        case _:
            parser.print_help()

if __name__ == "__main__":
    main()
