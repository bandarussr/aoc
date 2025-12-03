import argparse

from utils import create_day, run_all, run_day

def main():
    parser = argparse.ArgumentParser(
        description="A cli to help with running and managing input for AoC Y25."
    )
    sub = parser.add_subparsers(dest="command", help="command to execute")

    # Create
    create = sub.add_parser("create", help="create a day")
    create.add_argument("-d", "--day", type=int, help="day to create (1-12)", default=None)

    # Run
    run = sub.add_parser("run", help="run a day")
    run.add_argument("-d", "--day", type=int, help="day to run (1-12)", default=None)
    run.add_argument("-t", "--test", action="store_true", help="use test input, else use actual input", default=False)

    # Run all
    runall = sub.add_parser("runall", help="runs all the days")
    runall.add_argument("-t", "--test", action="store_true", help="use test input, else use actual input", default=False)

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
                run_day(args.day, args.test)
            else:
                run_day(test=args.test)

        case "runall":
            run_all(test=args.test)

        case _:
            parser.print_help()

if __name__ == "__main__":
    main()
