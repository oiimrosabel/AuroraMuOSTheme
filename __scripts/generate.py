import tools.display_tools as c
import tools.files_tools as d
import tools.generate_tools as g

buildFolder = "../__build"
factoryFolder = "../__factory"
interFolder = f"{buildFolder}/__intermediate"
commonFolder = "../__common"


def generateMacro(themeName: str, tempateName: str):
    d.createFolder(interFolder)
    c.task(f"Generating schemes for {themeName} version...")
    g.cookTheme(interFolder, f"../{themeName}/", commonFolder)
    d.createFolder(f"{interFolder}/schemes")
    g.generateSchemes(f"{factoryFolder}/template/default.txt",
                      f"{factoryFolder}/data/{tempateName}.json",
                      f"{interFolder}/schemes/default.txt")
    g.generateSchemes(f"{factoryFolder}/template/muxlaunch.txt",
                      f"{factoryFolder}/data/{tempateName}.json",
                      f"{interFolder}/schemes/muxlaunch.txt")
    g.zipFolder(interFolder, f"{buildFolder}/Rezolution{themeName}.zip")
    d.deleteFilesInFolder(interFolder)


c.task("Generating __build folder...")
d.deleteFolder(buildFolder)
d.createFolder(buildFolder)
generateMacro("Dark", "templateDark")
generateMacro("White", "templateWhite")
generateMacro("Indigo", "templateIndigo")
c.task("Cleaning up...")
d.deleteFolder(interFolder)
