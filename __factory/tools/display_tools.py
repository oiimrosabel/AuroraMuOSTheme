import sys


def task(text: str):
    print(f"▶️ > {text}")


def info(text: str):
    print(f"\tℹ️ > {text}")


def warning(text: str):
    print(f"\t⚠️ > {text}", file=sys.stderr)


def error(text: str):
    print(f"\t🛑 > {text}", file=sys.stderr)


def success(text: str):
    print(f"\t✅ > {text}")
