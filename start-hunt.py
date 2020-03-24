#!/usr/bin/python3
#
# NAME - hunt.py
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
# https://www.acunetix.com/websitesecurity/introduction-web-shells/
# https://medium.com/@p.matkovski/detection-of-php-web-shells-with-access-log-waf-and-audit-deamon-e798d4c95ec

# Import relevent libraries
import sys, getopt
from util import *

import apache_log_parser

from Hunt import Hunt
from Event import Event
from Config import Config

apache_access = "%h %l %u %t \"%r\" %>s %b \"%{Referer}i\" \"%{User-agent}i\""
# apache_error = "%h %l %u %t \"%r\" %>s %b \"%{Referer}i\" \"%{User-agent}i\""

def parseLine(line, type):
	try:
		line_parser = apache_log_parser.make_parser(apache_access)
		return line_parser(line)
	except apache_log_parser.LineDoesntMatchException as e:
		return None



# Print the help message and then exit
def printHelpAndExit():
	error_message = "hunt.py -t <type: I.e apache-access> -f <file: Filename>"
	print(error_message)
	sys.exit()


def main(argv):
	hunt = Hunt()
	try:
		opts, args = getopt.getopt(argv,"t:",["type="])
	except getopt.GetoptError:
		printHelpAndExit()
	
	requests = {}
	log_type = "apache_access"

	# Iterate through options
	for opt, arg in opts:
		if opt == "-h":
			printHelpAndExit()
		elif opt in ("-t", "--type"):
			log_type = arg


	for line in sys.stdin:
		event = parseLine(line, log_type)
		if event != None:
			event_obj = Event(event['remote_host'], event['time_received'], event['request_header_user_agent'], event['request_url'], event['status'], event['response_bytes_clf'], event['request_method'], event['request_http_ver'])
			hunt.addEvent(event_obj)

	hunt.start()
	hunt.displayResults()
	# hunt.displaySpecificCOAs()
	# hunt.displayGenericCOAs()
	# hunt.displayGenericOFIs()

			# hunt.addEvent(event_obj)
	# events = hunt.responseSizeByURI()
	# events = hunt.requestMethodByURI()
	# for event in hunt.postRequests():
	# 	print(event.getURI() + " " + str(event.getResponseSize()) )



	# for key, value in events.items():
	# 	outliers = hunt.getOutliers(value)
	# 	if len(outliers) > 0:
	# 		print(key)

	# for key,request in requests.items():
	# 	if len(request) > 1:
	# 		outliers = getOutliers(request)
	# 		if len(outliers) > 0:
	# 			print(key)
	# 			print(request)


	# print(requests)

if __name__ == "__main__":
   # Set Default Auth Headers
   main(sys.argv[1:])
