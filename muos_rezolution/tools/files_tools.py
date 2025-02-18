import shutil
import sys
from os import EX_DATAERR
from pathlib import Path

import muos_rezolution.tools.display_tools as c


def deleteFile(path: Path):
    if not path.exists():
        c.warning(f"{path} does not exist")
    elif not path.is_file():
        c.warning(f"{path} is not a file")
    else:
        path.unlink()
        c.info(f"Deleted file {path}")


def deleteFolder(path: Path):
    if not path.exists():
        c.warning(f"{path} does not exist")
    elif not path.is_dir():
        c.warning(f"{path} is not a directory")
    else:
        deleteFilesInFolder(path)
        path.rmdir()
        c.info(f"Deleted folder {path}")


def deleteFilesInFolder(path: Path):
    if path.exists():
        for file in path.glob("*"):
            if file.is_file():
                deleteFile(file)
            else:
                deleteFolder(file)
    else:
        c.warning(f"{path} does not exist")


def readFile(filePath: Path) -> str:
    try:
        with filePath.open(mode="r", encoding="utf-8") as file:
            c.info(f"File {filePath} read successfully")
            return file.read()
    except FileNotFoundError:
        c.error(f"File not found : {filePath}")
        sys.exit(EX_DATAERR)


def saveFile(filePath: Path, content: str):
    try:
        with filePath.open(mode="w", encoding="utf-8") as file:
            file.write(content)
            c.info(f"File {filePath} saved successfully")
    except FileNotFoundError:
        c.error(f"File not found : {filePath}")
        sys.exit(EX_DATAERR)
    except IOError as e:
        c.error(f"Unable to edit '{filePath}': {e}")
        sys.exit(EX_DATAERR)


def createFolder(path: Path):
    if path.exists():
        c.warning(f"{path} already exists")
    else:
        path.mkdir(exist_ok=True)
        c.info(f"Created folder '{path}'")


def mergeFolders(srcPath: Path, destPath: Path, replace=False):
    if not destPath.exists():
        destPath.mkdir()

    for root, _, files in srcPath.walk():
        for file in files:
            srcFile: Path = root / file
            dstFile: Path = destPath / srcFile.relative_to(srcPath)

            if not dstFile.parent.exists():
                dstFile.parent.mkdir(parents=True, exist_ok=True)
            replaceable = dstFile.exists() and replace
            if not dstFile.exists() or replaceable:
                if replaceable:
                    c.warning(f"File {dstFile} exists, overwriting...")
                shutil.copy2(srcFile, dstFile)
            else:
                c.warning(f"File {dstFile} already exists")
    c.info(f"Merged {srcPath} to {destPath}")
