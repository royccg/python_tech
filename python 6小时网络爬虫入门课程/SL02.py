import requests
import os
# 爬取图片
# url = 'http://image.nationalgeographic.com.cn/2017/0211/20170211061910157.jpg'
# root = 'D://pics//'
# path = root+ url.split('/')[-1]
# try:
# 	if not os.path.exists(root):
# 		os.mkdir(root)
# 	if not os.path.exists(path):
# 		r = requests.get(url)
# 		with open(path, 'wb') as f:
# 			f.write(r.content)
# 			f.close()
# 		print('文件保存成功')
# 	else:
# 		print('文件已存在')
# except:
# 	print('爬取失败')

## ip地址返回
url = 'http://m.ip138.com/iplookup.asp?ip='
try:
	r = requests.get(url+ '202.204.80.112')
	r.raise_for_status()
	r.encoding = r.apparent_encoding
	# print(r.request.headers)
	print(r.text[-500:])
except:
	print('爬取失败')
