#!/usr/bin/python3

import tools.display_tools as c
import tools.files_tools as d
import tools.generate_tools as g

buildFolder = "../__build"
factoryFolder = "../__factory"
interFolder = f"{buildFolder}/__intermediate"
commonFolder = "../__common"


def generateMacro(themeName: str):
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
    g.zipFolder(interFolder, f"{buildFolder}/Rezolution{themeName}.zip")
    d.deleteFilesInFolder(interFolder)


c.task("Generating __build folder...")
d.deleteFolder(buildFolder)
d.createFolder(buildFolder)
generateMacro("Dark")
generateMacro("White")
generateMacro("Indigo")
generateMacro("OLED")
c.task("Cleaning up...")
d.deleteFolder(interFolder)
