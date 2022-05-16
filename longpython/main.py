"""CLI tool to print long python."""

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
    r"   \ \ ".rstrip(),
)
TAIL = dedent(
    r"""
    {0}   \ \ _ ,
    {0}    \___/
    """
).strip("\n")


def check_natural(v: str) -> int:
    v_int = int(v)
    if v_int < 0:
        raise argparse.ArgumentTypeError("length should be greater than or equal to 0.")
    return v_int


def parse_args() -> argparse.Namespace:
    """Parse CLI arguments."""
    parser = argparse.ArgumentParser(
        prog="longpython",
        description="CLI tool to print long python",
    )
    parser.add_argument(
        "-l",
        "--length",
        metavar="INT",
        type=check_natural,
        default=1,
        help="length of python (default: %(default)r)",
    )
    return parser.parse_args()


def main() -> None:
    """Print an ascii art of python."""
    args = parse_args()
    lines = []
    lines.append(HEAD)
    for x in range(args.length):
        lines.append(BODY[x % 2])
    if len(lines) % 2 == 1:
        lines.append(TAIL.format(" "))
    else:
        lines.append(TAIL.format(""))

    print("\n".join(lines))


if __name__ == "__main__":
    main()
