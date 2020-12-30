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

# get_md5
import hashlib
import os
def getMd5(file_path):
    md5 = None
    if os.path.isfile(file_path):
        f = open(file_path, 'rb')
        md5_obj = hashlib.md5()
        md5_obj.update(f.read())
        hash_code = md5_obj.hexdigest()
        f.close()
        md5 = str(hash_code).lower()
    return md5

'''获取文件的大小,结果保留两位小数，单位为MB'''
def get_FileSize(filePath):
	# import os
	# filePath = unicode(filePath,'utf8')
	fsize = os.path.getsize(filePath)
	fsize = fsize/float(1024*1024)
	return round(fsize,2)

def readJson(fileDir):
    '''readJson
    read json file
    Arguments:
            fileDir {[string]} -- [the dir of json]
    Returns:
            [dict] 
    '''
    import json
    with open(fileDir, 'r', encoding='utf-8') as file:
        return json.load(file)


def numQue(num):
    if num % 2 == 0:
        return 2 * num - 2
    else:
        return 2 * num - 1
