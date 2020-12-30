import requests
# 京东
url_jd = 'https://item.jd.com/100005207363.html'
# try:
# 	r = requests.get(url_jd)
# 	r.raise_for_status()
# 	r.encoding = r.apparent_encoding
# 	print(r.text[:1000])
# except:
# 	print('爬取失败')


# url_ymx = 'https://www.amazon.cn/dp/B01JRE0HKW?_encoding=UTF8&ref_=pc_cxrd_2045366051_recTab_2045366051_t_1&pf_rd_p=577c845d-13b2-4e81-8a3e-772c4d55db4b&pf_rd_s=merchandised-search-4&pf_rd_t=101&pf_rd_i=2045366051&pf_rd_m=A1AJ19PSB66TGU&pf_rd_r=2PB5701T46NA2CW8FWVH&pf_rd_r=2PB5701T46NA2CW8FWVH&pf_rd_p=577c845d-13b2-4e81-8a3e-772c4d55db4b'

# try:
# 	kv = {'user-agent':'Mozilla/5.0'}
# 	r= requests.get(url_ymx, headers = kv)
# 	r.raise_for_status()
# 	r.encoding = r.apparent_encoding
# 	print(r.text[1000:2000])
# except:
# 	print('爬取失败')


# baidu、360 关键字提交
keyword = 'Python'
try:
	kv = {'wd':keyword}
	r = requests.get('http://www.baidu.com/s', params = kv)
	print(r.requests.url)
	r.raise_for_status()
	print(len(r.text))
except:
	print('爬取失败')
finally:
	print('end')