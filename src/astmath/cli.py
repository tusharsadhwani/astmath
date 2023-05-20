"""CLI interface for astmath."""
import argparse

import astmath


def cli() -> None:
    """CLI interface."""
    parser = argparse.ArgumentParser()
    parser.add_argument("expression", help="Arithemetic expression to evaluate")
    args = parser.parse_args()

    try:
        print(astmath.eval(args.expression))
    except ValueError as exc:
        print("Error:", exc)
