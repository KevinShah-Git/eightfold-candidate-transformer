import argparse
import json
import os

from transformer import CandidateTransformer


def main():

    parser = argparse.ArgumentParser()

    parser.add_argument(
        "--config",
        default="config/default.json"
    )

    parser.add_argument(
        "--output",
        default="output/result.json"
    )

    args = parser.parse_args()

    transformer = CandidateTransformer()

    result = transformer.run(args.config)

    os.makedirs("output", exist_ok=True)

    with open(args.output, "w") as f:
        json.dump(result, f, indent=4)

    print(json.dumps(result, indent=4))


if __name__ == "__main__":
    main()