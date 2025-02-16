from os import EX_DATAERR
from pathlib import Path
import sys

import muos_rezolution.tools.display_tools as c


def deleteFile(path: Path):
    if not path.exists():
        c.warning(f"{path} does not exist")
        return
    if not path.is_file():
        c.warning(f"{path} is not a file")
        return
    path.unlink()
    c.success(f"Deleted file {path}")


def deleteFolder(path: Path):
    if not path.exists():
        c.warning(f"{path} does not exist")
        return
    if not path.is_dir():
        c.warning(f"{path} is not a directory")
    path.rmdir()
    c.success(f"Deleted folder {path}")


def deleteFilesInFolder(path: Path):
    if not path.exists():
        c.warning(f"{path} does not exist")
        return
    for file in path.glob("*"):
        if file.is_file():
            deleteFile(file)
        else:
            deleteFolder(file)


def readFile(filePath: Path) -> str:
    try:
        with filePath.open(mode="r", encoding="utf-8") as file:
            c.success(f"File {filePath} read successfully")
            return file.read()
    except FileNotFoundError:
        c.error(f"File not found : {filePath}")
        sys.exit(EX_DATAERR)


def saveFile(filePath: Path, content: str) -> None:
    try:
        with filePath.open(mode="w", encoding="utf-8") as file:
            file.write(content)
            c.success(f"File {filePath} saved successfully")
    except FileNotFoundError:
        c.error(f"File not found : {filePath}")
        sys.exit(EX_DATAERR)
    except IOError as e:
        c.error(f"Unable to edit '{filePath}': {e}")
        sys.exit(EX_DATAERR)


def createFolder(path: Path):
    if path.exists():
        c.warning(f"{path} already exists")
        return
    path.mkdir(exist_ok=True)
    c.success(f"Created folder '{path}'")
