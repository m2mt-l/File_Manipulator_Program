import sys
from argparse import ArgumentParser, Action, Namespace
from os.path import exists


class ReverseAction(Action):
    def __call__(
        self,
        parser: ArgumentParser,
        namespace: Namespace,
        values: list,
        option_string: str,
    ):
        # print(f"parse: {parser} , type: {type(parser)}")
        # print(f"parse: {namespace} , type: {type(namespace)}")
        # print(f"parse: {values} , type: {type(values)}")
        # print(option_string)
        input_path = values[0]
        output_path = values[1]
        if not exists(input_path):
            print(f"Input file {input_path} does not exist")
            return
        contents = ""

        with open(input_path) as f:
            contents = f.read()

        with open(output_path, "x") as f:
            f.write(contents[::-1])


class CopyAction(Action):
    def __call__(
        self,
        parser: ArgumentParser,
        namespace: Namespace,
        values: list,
        option_string: str,
    ):
        input_path = values[0]
        output_path = values[1]
        if not exists(input_path):
            print(f"Input file {input_path} does not exist")
            return
        contents = ""

        with open(input_path) as f:
            contents = f.read()

        with open(output_path, "x") as f:
            f.write(contents)


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument(
        "--reverse",
        type=str,
        nargs=2,
        action=ReverseAction,
        metavar=("[input file]", "[output file]"),
        help="Output file that contains reversed texts in input file.",
    )

    parser.add_argument(
        "--copy",
        type=str,
        nargs=2,
        action=CopyAction,
        metavar=("[input file]", "[output file]"),
        help="Copy input file and name output file.",
    )

    parser.add_argument(
        "--duplicate-contents",
        type=str,
        nargs=2,
        help="--duplicate-contents [input file] [n]",
    )

    parser.add_argument(
        "--replace-string",
        type=str,
        nargs=3,
        help="--replace-string [input file] [needle] [newstring]",
    )
    args = parser.parse_args()
