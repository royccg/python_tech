#  function 
def creatUuid5(name):
	'''creat UUID
	use uuid5
	Arguments:
		name {[string]} -- [file's name]
	Returns:
		[string] -- [the only uuid]
	'''
	import uuid
	return uuid.uuid5(uuid.NAMESPACE_DNS, name)
	# return uuid.uuid5(uuid.NAMESPACE_URL, nameSpace)

def readJson(fileDir):
	'''readJson
	read json file
	Arguments:
		fileDir {[string]} -- [the dir of json]
	Returns:
		[dict] 
	'''
	import json
	with open(fileDir, 'r',encoding = 'utf-8') as file:
		return json.load(file)



