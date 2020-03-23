#!/usr/bin/python3
#
# NAME - Config.py
# SYNOPSIS
## 
# DESCRIPTION
## \
# INPUT:
## None
# OUTPUT:
## STDOUT
# AUTHOR: nathangcoats@gmail.com
#

import json
from util import *

class Config(object):

	__config_file = "./config.json"
	__config = {}

	# Default constructor
	def __init__(self):

		try:
			self.setConfig()
		except Exception as e:
			print(e)

	def setConfig(self):
		with open(self.__config_file) as file:
			config = json.load(file)
			self.__config = config

	def get(self, key=None):
		try:
			if empty(key):
				return self.__config
			else:
				return self.__config[key]
		except Exception as e:
			print(e)
			return None

	def getConfig(self):
		return self.__config

