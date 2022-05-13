import argparse
from textwrap import dedent

HEAD = dedent(
    r"""
      _
    (" ヽ
       \ \
    """
).strip("\n")
BODY = (
    "   / /",
    r"   \\ \\",
)
TAIL = dedent(
    r"""
    {0}   \ \ _ ,
    {0}    \___/
    """
).strip("\n")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        prog="longpython",
        description="CLI tool to print long python",
    )
    parser.add_argument(
        "-l",
        "--length",
        metavar="INT",
        type=int,
        default=1,
        help="length of python (default: %(default)r)",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    print(HEAD)
    for x in range(args.length):
        print(BODY[x % 2])
    if x % 2 == 1:
        print(TAIL.format(" "))
    else:
        print(TAIL.format(""))


if __name__ == "__main__":
    main()
