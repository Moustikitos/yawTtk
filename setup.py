# -*- coding:latin-1 -*-
try:
	from setuptools import setup
except ImportError:
	from distutils.core import setup

import sys, os, shutil
from yawTtk import __version__

shutil.rmtree("build", ignore_errors = True)
long_description = open("./rst/pypi.rst", "r")
setup(
	name = "yawTtk",
	version = __version__,
	keywords = ["ttk", "tile", "wrapper"],
	author = "thoons",
	author_email = "bruno.thoorens@free.fr",
	maintainer = "thoons",
	maintainer_email = "bruno.thoorens@free.fr",
	url = "http://bruno.thoorens.free.fr",
	download_url = "https://github.com/Moustikitos/yawTtk",
	bugtrack_url = "https://github.com/Moustikitos/yawTtk/issues",
	description = "yawTtk is a Python wrapper for Tile. It provides classes which allow the display, positioning and control of native look'n feel widgets.",
	long_description = long_description.read(),
	packages = ['yawTtk'],
	package_data = ({'yawTtk': ['tcl/tile0.8.2/*.tcl', 'tcl/tile0.8.2/*.dll', 'tcl/tile0.8.2/*.lib']} if sys.version_info[:2] < (2,7) else {}),
	license = "Copyright© 2006-2015, THOORENS Bruno, BSD licence",
	classifier = [
		"License :: OSI Approved :: BSD License",
		"Operating System :: Microsoft :: Windows",
		"Operating System :: Unix",
		'Programming Language :: Python',
		"Programming Language :: Python :: 2",
		"Programming Language :: Python :: 3",
		"Topic :: Desktop Environment :: Window Managers"
	]
)
long_description.close()
