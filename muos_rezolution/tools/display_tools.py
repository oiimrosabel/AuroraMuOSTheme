import sys

from muos_rezolution.tools.__global__ import config as cf


def task(text: str):
    print(f"\033[95m[🛈]\033[0m > {text}")


def info(text: str):
    if cf.VERBOSE:
        print(f"\033[94m[🮕]\033[0m > {text}")


def warning(text: str):
    if cf.VERBOSE:
        print(f"\033[93m[⚠]\033[0m > {text}", file=sys.stderr)


def error(text: str):
    print(f"\033[31m[!]\033[0m > {text}", file=sys.stderr)


def success(text: str):
    print(f"\033[32m[✓]\033[0m > {text}")


def ask(text: str, choices: list[str], default=0) -> int:
    question = f"\n\033[36m[🯄]\033[0m > {text} (default = {default}) \n"
    for i, c in enumerate(choices):
        question += f"\t{i} : {c}\n"
    question += "\n < "
    res = input(question)
    if res == "":
        info(f"Chose {choices[default]} ({default}, default).")
        return default
    try:
        res = int(res)
    except ValueError:
        error("Invalid input. Try again.")
        return ask(text, choices, default)
    if res < 0 or res > len(choices):
        error("Invalid input. Try again.")
        return ask(text, choices, default)
    info(f"Chose {choices[res]} ({res})\n")
    return res
