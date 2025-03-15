import shutil
import sys
from pathlib import Path

import Aurora.tools.display_tools as c
import Aurora.tools.files_tools as d
import Aurora.tools.mustache_tools as m
from Aurora.tools.__global__ import ifttt


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


def zipFolder(srcPath: Path, destPath: Path, isMuxZip=False):
    if not srcPath.exists():
        c.error(f"Invalid path : {srcPath}")
        sys.exit(1)

    zipLabel = ifttt(isMuxZip, "muxzip", "muxthm")
    fullDestPath = str(destPath.parent / destPath.stem)
    shutil.make_archive(fullDestPath, "zip", root_dir=srcPath, base_dir=".")
    shutil.move(f"{fullDestPath}.zip", f"{fullDestPath}.{zipLabel}")

    c.info(f"Archived {srcPath} into {destPath}.{zipLabel}")
