#!/usr/bin/python3
#
# NAME - Hunt.py
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

from util import *
import statistics

from Config import Config


class Hunt(object):

	__config_obj = None

	__events = []

	__coas = {}

	__ofis = {}

	__problem_events = []

	# Default constructor
	def __init__(self):

		try:
			self.__setConfig()
		except Exception as e:
			print(e)

	def start(self):
		for event_obj in self.__events:
			has_odity = False
			if event_obj.hasParameterOddities():
				msg = "Assure the statements attempted in the following parameters are disabled in the language configurations: " + str(event_obj.getParameters())
				self.addCOA(msg, "configuration")
				has_odity = True

			if event_obj.hasPostFileOddities():
				config_obj = self.getConfig()
				filetype_regex = config_obj.get("blacklist")["post_filetypes"]
				msg = "Assure script execution is disabled for all following file types " + str(filetype_regex)
				self.addCOA(msg, "configuration")
				has_odity = True

			if event_obj.hasPostDirectoryOddities():
				config_obj = self.getConfig()
				directories_regex = config_obj.get("blacklist")["post_directories"]
				msg = "Assure script execution is disabled for all following directories " + str(directories_regex)
				self.addCOA(msg, "configuration")
				has_odity = True

			if event_obj.hasURIOddities():
				config_obj = self.getConfig()
				directories_regex = config_obj.get("blacklist")["post_directories"]
				msg = "Investigate and potentially the file found at: " + str(event_obj.getURI())
				self.addCOA(msg, "removal")
				has_odity = True


			if has_odity == True:
				msg = "Investigate and potentially block to and from the following IP address: " + str(event_obj.getSrcIP())
				self.addCOA(msg, "pe")
				self.__problem_events.append(event_obj)



	def displayResults(self):
		if empty(self.__problem_events):
			print("No Webshells Detected, Dig Deeper")
			return

		print("")
		print("######################################")
		print("##### START POTENTIAL WEB SHELLS #####")
		print("######################################")
		print("")

		for event_obj in self.__problem_events:
			print(event_obj.getURI() + "?" + event_obj.getParameters())


		print("")
		print("######################################")
		print("###### END POTENTIAL WEB SHELLS ######")
		print("######################################")

	def displayGenericOFIs(self):
		config_obj = self.getConfig()
		ofi_obj = config_obj.get("ofis")
		if empty(ofi_obj):
			return
		print("")
		print("######################################")
		print("######### START GENERIC OFIS #########")
		print("######################################")
		print("")
		for key, ofis in ofi_obj.items():
			print(key.upper())
			for ofi in ofis:
				print("- " + str(ofi))

			print()

		print("")
		print("######################################")
		print("########## END GENERIC OFIS ##########")
		print("######################################")


	def displayGenericCOAs(self):
		config_obj = self.getConfig()
		coa_obj = config_obj.get("coas")
		if empty(coa_obj):
			return
		print("")
		print("######################################")
		print("######### START GENERIC COAS #########")
		print("######################################")
		print("")
		for key, coas in coa_obj.items():
			print(key.upper())
			for coa in coas:
				print("- " + str(coa))

			print()

		print("")
		print("######################################")
		print("########## END GENERIC COAS ##########")
		print("######################################")


	def displaySpecificCOAs(self):
		if empty(self.__coas):
			return
		print("")
		print("######################################")
		print("######### START SPECIFIC COAS ########")
		print("######################################")
		print("")
		for key, coas in self.__coas.items():
			print(key.upper())
			for coa in coas:
				print("- " + str(coa))

			print()


		print("")
		print("######################################")
		print("########## END SPECIFIC COAS #########")
		print("######################################")


	def clearEvents(self):
		self.__events = []

	def getEvents(self):
		return self.__events

	def addEvent(self, event):
		if empty(event):
			return
		self.__events.append(event)


	def getConfig(self):
		return self.__config_obj

	def addCOA(self, value, key=None):
		if key in self.__coas:
			self.__coas[key].append(value)
		else:
			self.__coas[key] = [value]


	def getCOA(self, key=None):
		try: 
			if empty(key):
				return self.__coas
			else:
				self.__coas[key] = value
		except Exception as e:
			print(e)
			return None

	def getCOAs(self, key=None):
		return self.__coas

	def __setConfig(self):
		config = Config()
		self.__config_obj = config


	# def getOutliers(self, dataset):
	# 	outliers = []
	# 	if len(dataset) <= 1:
	# 		return []


	# 	mean = statistics.mean(dataset)
	# 	stdev = statistics.stdev(dataset)

	# 	for item in dataset:
	# 		if abs(item - mean) > stdev:
	# 			outliers.append(item)

	# 	return outliers

	# def requestMethodByURI(self):
	# 	separated_events = {}
	# 	for event in self.getEvents():
	# 		key = event.getURI()

	# 		if key in separated_events:
	# 			separated_events[key].append(event.getRequestMethod())
	# 		else:
	# 			separated_events[key] = [event.getRequestMethod()]
	# 	return separated_events


	# def responseSizeByURI(self):
	# 	separated_events = {}
	# 	for event in self.getEvents():
	# 		key = event.getURI()

	# 		if key in separated_events:
	# 			separated_events[key].append(event.getResponseSize())
	# 		else:
	# 			separated_events[key] = [event.getResponseSize()]
	# 	return separated_events


	# def postRequests(self):
	# 	separated_events = []
	# 	for event in self.getEvents():
	# 		if event.getRequestMethod() == "post":
	# 			separated_events.append(event)

	# 	return separated_events
