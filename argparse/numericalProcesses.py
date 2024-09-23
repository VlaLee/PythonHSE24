import argparse


parser = argparse.ArgumentParser(
    prog="Numerical processes",
    description="You can sum, get a maximum or "
    "a minimum from numbers or get a difference "
    "between the extremes values",
    allow_abbrev=False,
)

# Positional argument
parser.add_argument(
    "-s",
    "--set",
    help="enter a number for actions",
    action="extend",
    type=int,
    nargs="*",
    required=True,
    metavar="collection",
)

# Optional argument with a default value
parser.add_argument(
    "-ac",
    "--action",
    choices=["sum", "max", "min", "diff"],
    help="what to do with numbers - sum, max, min, diff",
    default="sum",
)

args = parser.parse_args()

if args.action == "sum":
    print(sum(args.set))
elif args.action == "max":
    print(max(args.set))
elif args.action == "min":
    print(max(args.set))
elif args.action == "diff":
    print(max(args.set) - min(args.set))
