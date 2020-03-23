import json, sys

## Helper functions
# checks to see if the data given is "", None, 0, or false
# returns a boolean
# on Exception returns False
def empty(data):
	try:
		return (data == "") or (data == None) or (data == 0) or (data == False) or (len(data) == 0)
	except:
		return False

# prints out the value of an object
# then instantly exits the script
def dd(data={}):
	print(data)
	sys.exit()

# Pretty Print json and then exit
def ppJSON(js):
	print( json.dumps(js, indent=4, sort_keys=True) )
	sys.exit()
