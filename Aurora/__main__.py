#!/usr/bin/env python3
from pathlib import Path

import Aurora.tools.arguments_tools as p
import Aurora.tools.display_tools as c
import Aurora.tools.files_tools as d
import Aurora.tools.generate_tools as g

# Paths
root = Path(__file__).parent / "resources"
iconsFolder = root / "icons"
buildFolder = Path("build")
factoryFolder = root / "factory"
interFolder = buildFolder / "__intermediate"
commonFolder = root / "common"

# Theme variants
supportedThemesList = ["Moon", "Cloud", "Twilight", "Midnight", "Retro"]


def generateTheme(themeName: str):
    d.createFolder(interFolder)
    c.task(f"Generating theme file for {themeName} variant...")
    g.cookTheme(interFolder, root / f"variants/{themeName}", commonFolder)
    d.createFolder(interFolder / "scheme")
    g.generateSchemes(factoryFolder / "template/global.ini",
                      factoryFolder / f"data/template{themeName}.json",
                      interFolder / "scheme/global.ini")
    g.generateSchemes(factoryFolder / "template/muxlaunch.ini",
                      factoryFolder / f"data/template{themeName}.json",
                      interFolder / "scheme/muxlaunch.ini")
    g.generateSchemes(factoryFolder / "template/muxplore.ini",
                      factoryFolder / f"data/template{themeName}.json",
                      interFolder / "scheme/muxplore.ini")
    g.zipFolder(interFolder, buildFolder / f"Aurora{themeName}.zip", "muxthm")
    d.deleteFilesInFolder(interFolder)
    c.success(f"{themeName} variant generated successfully")


def clean():
    c.task("Cleaning up build folder...")
    d.deleteFolder(buildFolder)
    c.success("Cleaned successfully.")


def generateIconPack():
    c.task("Generating icon pack...")
    g.zipFolder(iconsFolder, buildFolder / "AuroraConsoleIcons.zip", "muxzip")
    c.success("Icon pack generated successfully.")


def generateThemes(themes: list[str]):
    clean()
    d.createFolder(buildFolder)
    for theme in themes:
        generateTheme(theme)
    generateIconPack()
    c.task("Cleaning up...")
    d.deleteFolder(interFolder)
    c.success("Cleaned successfully. Enjoy !")


if __name__ == "__main__":
    parser = p.RezParser(supportedThemesList)
    args = parser.parseArgs()
    match True:
        case args.cleanUp:
            clean()
            exit()
        case args.iconPack:
            generateIconPack()
            exit()
        case _:
            generateThemes(args.themes)
