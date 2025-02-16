from pathlib import Path
import shutil
import sys

import muos_rezolution.tools.display_tools as c
import muos_rezolution.tools.files_tools as d
import muos_rezolution.tools.mustache_tools as m


def mergeFolders(srcPath: Path, destPath: Path):
    if not destPath.exists():
        destPath.mkdir()

    for root, _, files in srcPath.walk():
        for file in files:
            srcFile: Path = root / file
            dstFile: Path = destPath / srcFile.relative_to(srcPath)

            if not dstFile.exists():
                dstFile.mkdir(exist_ok=True)
                shutil.copy2(srcFile, dstFile)
            else:
                c.warning(f"File {dstFile} already exists")
    c.success(f"Merged {srcPath} to {destPath}")


def generateSchemes(templatePath: Path, dataPath: Path, outputPath: Path):
    templateStr = d.readFile(templatePath)
    dataDict = m.interpretAsJson(d.readFile(dataPath))
    output = m.replaceMustaches(templateStr, dataDict)
    d.saveFile(outputPath, output)
    c.success(f"Scheme generated in {outputPath}")


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
    mergeFolders(commonPath, interPath)
    mergeFolders(srcPath, interPath)
    c.success(f"Theme cooked in {interPath}")


def zipFolder(srcPath: Path, destPath: Path):
    if not srcPath.exists():
        c.error(f"Invalid path : {srcPath}")
        sys.exit(1)
    if destPath.suffix == ".zip":
        destPath = destPath.stem

    shutil.make_archive(destPath, "zip", root_dir=srcPath, base_dir=".")
    c.success(f"Archived {srcPath} into {destPath}.zip")
