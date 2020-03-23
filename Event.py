#!/usr/bin/python3
#
# NAME - Event.py
# SYNOPSIS
## 
# DESCRIPTION
##
# INPUT:
## None
# OUTPUT:
## STDOUT
# AUTHOR: nathangcoats@gmail.com
#

import re
from util import *

from Config import Config

class Event(object):

	__config_object = {}

	__src_ip = ""
	__timestamp = ""
	__user_agent = ""
	__uri = ""
	__parameters = ""
	__response_code = ""
	__response_size = ""
	__request_method = ""
	__request_version = ""

	# Default constructor
	def __init__(self, src_ip, timestamp, user_agent, uri, response_code, response_size, request_method, request_version):

		try:
			self.__setConfig()
			self.setSrcIP(src_ip)
			self.setTimestamp(timestamp)
			self.setUserAgent(user_agent)
			self.setURI(uri)
			self.setParameters(uri)
			self.setResponseCode(response_code)
			self.setResponseSize(response_size)
			self.setRequestMethod(request_method)
			self.setRequestVersion(request_version)

		except Exception as e:
			print(e)


	def wasSuccessful(self):
		try:
			return self.getResponseCode() >= 200 and self.getResponseCode() < 300
		except:
			return False

	def hasOddity(self):
		has_oddity = self.hasParameterOddities() or self.hasPostFileOddities() or self.hasPostDirectoryOddities() or self.hasUserAgentOddities() or self.hasURIOddities()
		return has_oddity

	def hasUserAgentOddities(self):
		try:
			has_oddity = False
			config_obj = self.getConfig()

			regex = config_obj.get("blacklist")["user_agents"]
			result = re.search(regex, self.getURI())

			if not empty(result):
				has_oddity = True

			return has_oddity and self.wasSuccessful()

		except Exception as e:
			print(e)
			return False

	def hasURIOddities(self):
		try:
			has_oddity = False
			config_obj = self.getConfig()
			regex = config_obj.get("blacklist")["uris"]
			result = re.search(regex, self.getURI())

			if not empty(result):
				has_oddity = True

			return has_oddity and self.wasSuccessful()

		except Exception as e:
			print(e)
			return False


	def hasParameterOddities(self):
		try:
			has_oddity = False
			config_obj = self.getConfig()
			regex = config_obj.get("blacklist")["parameters"]
			result = re.search(regex, self.getParameters())

			if not empty(result):
				has_oddity = True

			return has_oddity and self.wasSuccessful()

		except Exception as e:
			print(e)
			return False

	def hasPostDirectoryOddities(self):
		try:
			has_oddity = False
			config_obj = self.getConfig()
			directory_regex = config_obj.get("blacklist")["post_directories"]

			if self.getRequestMethod() != "post":
				return False

			dir_result = re.search(directory_regex, self.getURI() )

			if not empty(dir_result):
				has_oddity = True

			return has_oddity and self.wasSuccessful()

		except Exception as e:
			print(e)
			return False

	def hasPostFileOddities(self):
		try:
			has_oddity = False
			config_obj = self.getConfig()
			filetype_regex = config_obj.get("blacklist")["post_filetypes"]

			if self.getRequestMethod() != "post":
				return False

			file_result = re.search(filetype_regex, self.getURI())

			if not empty(file_result):
				has_oddity = True

			return has_oddity and self.wasSuccessful()

		except Exception as e:
			print(e)
			return False

	def getConfig(self):
		return self.__config_object

	def __setConfig(self):
		config = Config()
		self.__config_object = config

	def setSrcIP(self, src_ip):
		ds = src_ip.split(":")
		try:
			self.__src_ip = str(ds[1])
		except Exception as e:
			self.__src_ip = str(src_ip)
		return self.__src_ip

	def setTimestamp(self, timestamp):
		self.__timestamp = timestamp
		return self.__timestamp

	def setUserAgent(self, user_agent):
		self.__user_agent = str(user_agent)
		return self.__user_agent

	def setURI(self, uri):
		parts = uri.split("?")
		self.__uri = str(parts[0])
		return self.__uri

	def setParameters(self, uri):
		parts = uri.split("?")
		try:
			self.__parameters = str(parts[1])
		except:
			self.__parameters = ""

		return self.__parameters


	def setResponseCode(self, response_code):
		self.__response_code = int(response_code)
		return self.__response_code

	def setResponseSize(self, response_size):
		self.__response_size = int(response_size)
		return self.__response_size

	def setRequestMethod(self, request_method):
		self.__request_method = str(request_method).lower()
		return self.__request_method

	def setRequestVersion(self, request_version):
		self.__request_version = str(request_version)
		return self.__request_version


	def getSrcIP(self):
		return str(self.__src_ip)

	def getTimestamp(self):
		return self.__timestamp

	def getUserAgent(self):
		return str(self.__user_agent)

	def getURI(self):
		return str(self.__uri)

	def getParameters(self):
		return str(self.__parameters)

	def getResponseCode(self):
		return int(self.__response_code)

	def getResponseSize(self):
		return int(self.__response_size)

	def getRequestMethod(self):
		return str(self.__request_method).lower()

	def getRequestVersion(self):
		return str(self.__request_version)
