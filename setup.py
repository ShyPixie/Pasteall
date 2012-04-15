#!/usr/bin/env python
# Este arquivo faz parte do PastSlack

import os
import os.path
import commands

from distutils.core import setup
from distutils.core import Command
from distutils.command.install import install
from distutils.command.install_data import install_data

setup(
	name = "PastSlack",
	description = "Um monitor de clipboard para o Slackware",
	author = "Lara Maia",
	author_email = "lara@craft.net.br",
	url = "http://github.com/mrk3004/PastSlack/",
	license = "GNU GPL v3",
	version = "0.0.1",
	scripts = ["pastslack"])