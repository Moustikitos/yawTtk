# -*- coding:latin-1 -*-
try:
	from setuptools import setup
except ImportError:
	from distutils.core import setup

import sys, os, shutil
from yawTtk import __version__

shutil.rmtree("build", ignore_errors = True)
print({'yawTtk': ['tcl/tile0.8.2/*.tcl', 'tcl/tile0.8.2/*.dll', 'tcl/tile0.8.2/*.lib']} if sys.version_info[:2] < (2,7) else {})
long_description = open("./rst/pypi.rst", "r")
setup(
	name = "yawTtk",
	version = __version__,
	author = "Bruno THOORENS",
	author_email = "bruno.thoorens@free.fr",
	description = "yawTtk is a Python wrapper for Tile. It provides classes which allow the display, positioning and control of native look'n feel widgets.",
	long_description = long_description.read(),
	platforms = ["win32"],
	packages = ['yawTtk'],
	package_data = ({'yawTtk': ['tcl/tile0.8.2/*.tcl', 'tcl/tile0.8.2/*.dll', 'tcl/tile0.8.2/*.lib']} if sys.version_info[:2] < (2,7) else {}),
	license = "Copyrightę 2006-2015, THOORENS Bruno, BSD licence",
)
long_description.close()
