import sys
from pathlib import Path


class HealingMoonInterpreter:

    A_COMMAND = "&&&-%%%+%+%+%+&%^^^/^+"
    B_COMMAND = "%&%+/%+%+%&/+%+%+%+^+^+%^%/"
    C_COMMAND = "////)/&%^^!'^'!'%%&++&^!&(/"
    COMMON_COMMAND = "+++++$½½{{{[{[]{$"

    def __init__(self):
        self.commands = {
            self.A_COMMAND: "A",
            self.B_COMMAND: "B",
            self.C_COMMAND: "C"
        }

        for letter in "DEFGHIJKLMNOPQRSTUVWXYZ":
            self.commands[self.COMMON_COMMAND + letter] = letter

        self.sorted_commands = sorted(
            self.commands.items(),
            key=lambda item: len(item[0]),
            reverse=True
        )

    def decode(self, source):
        result = []
        position = 0

        while position < len(source):

            if source[position] == "\n":
                result.append("\n")
                position += 1
                continue

            if source[position].isspace():
                result.append(source[position])
                position += 1
                continue

            matched = False

            for command, letter in self.sorted_commands:
                if source.startswith(command, position):
                    result.append(letter)
                    position += len(command)
                    matched = True
                    break

            if not matched:
                return None

        return "".join(result)

    def run_file(self, filename):
        try:
            path = Path(filename)

            if not path.exists():
                return

            source = path.read_text(encoding="utf-8")
            result = self.decode(source)

            if result is None:
                return

            sys.stdout.write(result)

        except Exception:
            return

    def interactive(self):
        while True:
            try:
                source = input()

                if source.lower() == "exit":
                    return

                result = self.decode(source)

                if result is not None:
                    print(result)

            except Exception:
                return


def main():
    interpreter = HealingMoonInterpreter()

    if len(sys.argv) > 1:
        interpreter.run_file(sys.argv[1])
    else:
        interpreter.interactive()


if __name__ == "__main__":
    main()