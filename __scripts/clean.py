#!/usr/bin/python3

import tools.display_tools as c
import tools.files_tools as d

c.task("Cleaning __build folder...")
d.deleteFolder('../__build')
