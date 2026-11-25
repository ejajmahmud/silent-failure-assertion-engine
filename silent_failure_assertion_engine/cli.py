"""CLI for Silent Failure Assertion Engine."""
import argparse
import json
from .core import SilentFailureDetector


def main():
    parser = argparse.ArgumentParser(description="Silent Failure Assertion Engine CLI")
    parser.add_argument("--deleted-asserts", type=int, default=0, help="Count of removed test assertions")
    args = parser.parse_args()

    det = SilentFailureDetector()
    print(json.dumps(det.evaluate(["src/core.py"], deleted_assertions=args.deleted_asserts, ran_tests=True, patch_lines=12), indent=2))


if __name__ == "__main__":
    main()
