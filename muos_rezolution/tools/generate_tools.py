import shutil
import sys
from pathlib import Path

import muos_rezolution.tools.display_tools as c
import muos_rezolution.tools.files_tools as d
import muos_rezolution.tools.mustache_tools as m


def process(template: str, data: dict[str, str | bool]):
    return (
        m.replaceMustaches(
            m.replaceConditionals(
                m.removeCommentaries(template),
                data
            ),
            data
        )
    )


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


def zipFolder(srcPath: Path, destPath: Path):
    if not srcPath.exists():
        c.error(f"Invalid path : {srcPath}")
        sys.exit(1)

    shutil.make_archive(str(destPath.parent / destPath.stem), "zip", root_dir=srcPath, base_dir=".")
    c.info(f"Archived {srcPath} into {destPath}.zip")
