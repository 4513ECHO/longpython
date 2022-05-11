#!/usr/bin/env python3
from argparse import ArgumentParser

head = "  _\n(\" ヽ\n   \\ \\"
body = ["   / /", "   \\ \\"]
tail = "{0}   \\ \\ _ ,\n{0}    \\___/"


def main() -> None:
    parser = ArgumentParser(
        description="CLI tool to print long python",
    )
    parser.add_argument("-l", "--length", type=int, default=1, help="length of python")
    args = parser.parse_args()
    print(head)
    for x in range(args.length):
        print(body[x % 2])
    if x % 2 == 1:
        print(tail.format(" "))
    else:
        print(tail.format(""))


if __name__ == "__main__":
    main()
