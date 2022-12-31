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


class DuplicateContentsAction(Action):
    def __call__(
        self,
        parser: ArgumentParser,
        namespace: Namespace,
        values: list,
        option_string: str,
    ):
        input_path = values[0]
        dup_times = values[1]
        if not exists(input_path):
            print(f"Input file {input_path} does not exist")
            return
        contents = ""

        try:
            dup_times = int(dup_times)
        except ValueError:
            print("The second argument must be a number.")
            return

        with open(input_path) as f:
            contents = f.read()

        with open(input_path, "w") as f:
            f.write(contents * dup_times)


class ReplaceString(Action):
    def __call__(
        self,
        parser: ArgumentParser,
        namespace: Namespace,
        values: list,
        option_string: str,
    ):
        input_path, needle, new_string = values

        if not exists(input_path):
            print(f"Input file {input_path} does not exist")
            return
        contents = ""

        with open(input_path) as f:
            contents = f.read()

        if contents.find(needle) == -1:
            print(f"This file does not contain {needle}.")
            return

        with open(input_path, "w") as f:
            f.write(contents.replace(needle, new_string))


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
        action=DuplicateContentsAction,
        metavar=("[input file]", "[duplicate times]"),
        help="Duplicate contents and write them duplicate times in the input file.",
    )

    parser.add_argument(
        "--replace-string",
        type=str,
        nargs=3,
        action=ReplaceString,
        metavar=("[input file]", "[needle]", "[new string]"),
        help="Replace string [needle] by [new string] in the input file.",
    )
    args = parser.parse_args()
