import shutil
import sys
from pathlib import Path

import Rezolution.tools.display_tools as c
import Rezolution.tools.files_tools as d
import Rezolution.tools.mustache_tools as m
from Rezolution.tools.__global__ import ifttt


def process(template: str, data: dict[str, str | bool]):
    output = m.removeCommentaries(template)
    output = m.replaceConditionals(output, data)
    output = m.removeInvalidConditionals(output)
    output = m.replaceMustaches(output, data)
    return output


def generateSchemes(templatePath: Path, dataPath: Path, outputPath: Path):
    templateStr = d.readFile(templatePath)
    dataDict = m.interpretAsJson(d.readFile(dataPath))
    output = process(templateStr, dataDict)
    d.saveFile(outputPath, output)
    c.info(f"Scheme generated in {outputPath}")


def cookTheme(interPath: Path, srcPath: Path, commonPath: Path):
    if not interPath.exists():
        c.error(f"Invalid intermediate path : {interPath}")
        sys.exit(1)
    if not srcPath.exists():
        c.error(f"Invalid source path : {srcPath}")
        sys.exit(1)
    if not commonPath.exists():
        c.error(f"Invalid common path : {commonPath}")
        sys.exit(1)
    d.mergeFolders(commonPath, interPath)
    d.mergeFolders(srcPath, interPath, True)
    c.info(f"Theme cooked in {interPath}")


def zipFolder(srcPath: Path, destPath: Path, keepAsZip=False):
    if not srcPath.exists():
        c.error(f"Invalid path : {srcPath}")
        sys.exit(1)

    fullDestPath = str(destPath.parent / destPath.stem)
    shutil.make_archive(fullDestPath, "zip", root_dir=srcPath, base_dir=".")
    if not keepAsZip:
        shutil.move(f"{fullDestPath}.zip", f"{fullDestPath}.muxthm")

    c.info(f"Archived {srcPath} into {destPath}.{ifttt(keepAsZip, 'zip', 'muxthm')}")
