#!/usr/bin/python3

import tools.display_tools as c
import tools.files_tools as d
import tools.generate_tools as g

iconsFolder = "../__icons"
buildFolder = "../__build"
factoryFolder = "../__factory"
interFolder = f"{buildFolder}/__intermediate"
commonFolder = "../__common"


def generateMacro(themeName: str, gridSupport=False):
    gridNameSupplement = ""
    if gridSupport:
        gridNameSupplement = "Grid"
    d.createFolder(interFolder)
    c.task(f"Generating schemes for {themeName} version...")
    g.cookTheme(interFolder, f"../{themeName}/", commonFolder)
    d.createFolder(f"{interFolder}/scheme")
    g.generateSchemes(f"{factoryFolder}/template/default.txt",
                      f"{factoryFolder}/data/template{themeName}.json",
                      f"{interFolder}/scheme/default.txt")
    g.generateSchemes(f"{factoryFolder}/template/muxlaunch.txt",
                      f"{factoryFolder}/data/template{themeName}.json",
                      f"{interFolder}/scheme/muxlaunch.txt")
    if gridSupport:
        g.generateSchemes(f"{factoryFolder}/template/muxplore.txt",
                          f"{factoryFolder}/data/template{themeName}.json",
                          f"{interFolder}/scheme/muxplore.txt")
    g.zipFolder(interFolder, f"{buildFolder}/Rezolution{themeName}{gridNameSupplement}.zip")
    d.deleteFilesInFolder(interFolder)


c.task("Generating __build folder...")
d.deleteFolder(buildFolder)
d.createFolder(buildFolder)
res = c.ask("Do you want to generate the theme with grid support ?", ["No", "Yes", "Both"])
if res != 1:  # if No or Both
    generateMacro("Dark")
    generateMacro("White")
    generateMacro("Indigo")
    generateMacro("OLED")
if res > 0:  # if Yes or Both
    generateMacro("Dark", True)
    generateMacro("White", True)
    generateMacro("Indigo", True)
    generateMacro("OLED", True)
    g.zipFolder(iconsFolder, f"{buildFolder}/RezolutionIcons.zip")
c.task("Cleaning up...")
d.deleteFolder(interFolder)
