#!/usr/bin/env python3

from pathlib import Path

import muos_rezolution.tools.arguments_tools as p
import muos_rezolution.tools.display_tools as c
import muos_rezolution.tools.files_tools as d
import muos_rezolution.tools.generate_tools as g

# Paths
root = Path(__file__).parent / "resources"
iconsFolder = root / "icons"
buildFolder = Path("build")
factoryFolder = root / "factory"
interFolder = buildFolder / "__intermediate"
commonFolder = root / "common"

# Theme variants
supportedThemesList = ["Dark", "Indigo", "OLED", "White"]


def generateMacro(themeName: str, gridSupport=False):
    gridNameSupplement = p.ifttt(gridSupport, "Grid", "")
    gridMsg = p.ifttt(gridSupport, " with Grid support", "")
    d.createFolder(interFolder)
    c.task(f"Generating theme file for {themeName} variant{gridMsg}...")
    g.cookTheme(interFolder, root / f"variants/{themeName}", commonFolder)
    d.createFolder(interFolder / "scheme")
    g.generateSchemes(factoryFolder / "template/default.txt",
                      factoryFolder / f"data/template{themeName}.json",
                      interFolder / "scheme/default.txt")
    g.generateSchemes(factoryFolder / "template/muxlaunch.txt",
                      factoryFolder / f"data/template{themeName}.json",
                      interFolder / "scheme/muxlaunch.txt")
    if gridSupport:
        g.generateSchemes(factoryFolder / "template/muxplore.txt",
                          factoryFolder / f"data/template{themeName}.json",
                          interFolder / "scheme/muxplore.txt")
    g.zipFolder(interFolder, buildFolder / f"Rezolution{themeName}{gridNameSupplement}.zip")
    d.deleteFilesInFolder(interFolder)
    c.success(f"{themeName} variant{gridMsg} generated successfully")


def clean():
    c.task("Cleaning up build folder...")
    d.deleteFolder(buildFolder)
    c.success("Cleaned successfully.")


def generate(themes: list[str], grid: p.GridEnabler):
    d.deleteFolder(buildFolder)
    d.createFolder(buildFolder)
    if grid.declined():
        for macro in themes:
            generateMacro(macro)
    if grid.accepted():
        for macro in themes:
            generateMacro(macro, True)
        g.zipFolder(iconsFolder, buildFolder / "RezolutionIcons.zip")
    c.task("Cleaning up...")
    d.deleteFolder(interFolder)
    c.success("Cleaned successfully. Enjoy !")


if __name__ == "__main__":
    parser = p.RezParser(supportedThemesList)
    args = parser.parseArgs()
    if args.cleanUp:
        clean()
    else:
        generate(args.themes, args.grid)
