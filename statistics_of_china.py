import requests

HEADERS = {
	# 'Accept':'application/json, text/javascript, */*; q=0.01',
	# 'Acceptbept-Encoding':'gzip, deflate',
	# 'Accept-Language':'zh-CN,zh;q=0.9,zh-TW;q=0.8,en;q=0.7,ja;q=0.6',
	# 'Connection':'keep-alive',
  	# 'Cookie':'_trs_uv=jab1tmyg_6_5ovj; acmrAutoLoginUser=""; acmrAutoSessionId=""; JSESSIONID=0FFF5C57733F998EB0D5397303D786ED; u=5',
	'Host':'data.stats.gov.cn',
	'Referer':'http://data.stats.gov.cn/easyquery.htm?cn=C01',
	'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36',
	'X-Requested-With':'XMLHttpRequest',
}
payload = {
	'm':'QueryData',
	'dbcode':'hgnd',
	'rowcode':'zb',
	'colcode':'sj',
	'wds':'[]',
	'dfwds':'[{"wdcode":"sj","valuecode":"LAST20"}]',
	'k1':'1511359034609',
}


s = requests.Session()
s.get('http://data.stats.gov.cn/easyquery.htm?cn=C01')
html = s.get('http://data.stats.gov.cn/easyquery.htm?',params=payload,headers=HEADERS)
print(html.text)
print(s.headers)