#!/usr/bin/env python3
from pathlib import Path

import Rezolution.tools.display_tools as c
import Rezolution.tools.files_tools as d
import Rezolution.tools.generate_tools as g
import Rezolution.tools.arguments_tools as p
from Rezolution.tools.__global__ import ifttt

# Paths
root = Path(__file__).parent / "resources"
iconsFolder = root / "icons"
buildFolder = Path("build")
factoryFolder = root / "factory"
interFolder = buildFolder / "__intermediate"
commonFolder = root / "common"

# Theme variants
supportedThemesList = ["Dark", "White", "Indigo", "OLED", "DMG"]


def generateTheme(themeName: str, gridSupport=False):
    gridNameSupplement = ifttt(gridSupport, "Grid", "")
    gridMsg = ifttt(gridSupport, " with Grid support", "")
    d.createFolder(interFolder)
    c.task(f"Generating theme file for {themeName} variant{gridMsg}...")
    g.cookTheme(interFolder, root / f"variants/{themeName}", commonFolder)
    d.createFolder(interFolder / "scheme")
    g.generateSchemes(factoryFolder / "template/global.ini",
                      factoryFolder / f"data/template{themeName}.json",
                      interFolder / "scheme/global.ini")
    g.generateSchemes(factoryFolder / "template/muxlaunch.ini",
                      factoryFolder / f"data/template{themeName}.json",
                      interFolder / "scheme/muxlaunch.ini")
    if gridSupport:
        g.generateSchemes(factoryFolder / "template/muxplore.ini",
                          factoryFolder / f"data/template{themeName}.json",
                          interFolder / "scheme/muxplore.ini")
    g.zipFolder(interFolder, buildFolder / f"Rezolution{themeName}{gridNameSupplement}.zip")
    d.deleteFilesInFolder(interFolder)
    c.success(f"{themeName} variant{gridMsg} generated successfully")


def clean():
    c.task("Cleaning up build folder...")
    d.deleteFolder(buildFolder)
    c.success("Cleaned successfully.")


def generateIconPack():
    c.task("Generating icon pack...")
    g.zipFolder(iconsFolder, buildFolder / "RezolutionIcons.zip", True)
    c.success("Icon pack generated successfully.")


def generateThemes(themes: list[str], grid: p.GridEnabler):
    clean()
    d.createFolder(buildFolder)
    if grid.declined():
        for theme in themes:
            generateTheme(theme)
    if grid.accepted():
        for theme in themes:
            generateTheme(theme, True)
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
            generateThemes(args.themes, args.grid)
