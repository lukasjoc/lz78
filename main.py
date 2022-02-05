#!/usr/bin/env python3

import sys
import argparse

from lz78 import encoder, decoder

def main():
    # TODO: validate input more..
    # TODO: what happens if you encoded decoded multiple times
    parser = argparse.ArgumentParser(description="decode and encode text using lz78")
    parser.add_argument("--encode", help="encode the text")
    parser.add_argument("--decode", help="decode the text.")
    parser.add_argument("--version", action="version", version="%(prog)s 0.1.0")

    args = parser.parse_args()
    def read_std_to_string(stdin=sys.stdin):
        stdin_string = ""
        for line in stdin:
            stdin_string += line

        return stdin_string

    if args.encode:
        stdin_string = read_std_to_string()
        print(encoder(stdin_string))
        sys.exit(0)

    elif args.decode:
        stdin_string = read_std_to_string()
        print(decoder(stdin_string))
        sys.exit(0)

if __name__ == "__main__":
    main()
