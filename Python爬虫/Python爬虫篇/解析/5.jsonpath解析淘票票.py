import urllib.request

url = 'https://dianying.taobao.com/showAction.json?_ksTS=1698028806089_64&jsoncallback=jsonp65&action=showAction&n_s=new&event_submit_doGetSoon=true'

headers = {
	# 'Content-Encoding': 'gzip',
	# 'Content-Language': 'zh-CN',
	# 'Content-Type': 'text/html;charset=UTF-8',
	'Date': urllib.parse.quote('Mon, 23 Oct 2023 02:52'),
	'Eagleeye-Traceid': '213e1fbb16980295271136016e3e4e',
	'Server': 'Tengine/Aserver',
	'Strict-Transport-Security': 'max-age=31536000',
	'Timing-Allow-Origin': '*',
	'Vary': 'Accept-Encoding',
	'Accept': 'text/javascript, application/javascript, application/ecmascript, application/x-ecmascript, */*; q=0.01',
	# 'Accept-Encoding': 'gzip, deflate, br',
	# 'Accept-Language': 'zh-CN,zh;q=0.9',
	'Cookie': 'tb_city=110100; tb_cityName="sbG+qQ=="; t=47b68d00f1e1e0ad8a9bc615cac3ab4a; cookie2=12810bfa137a1978bbb35e0b6228391d; v=0; _tb_token_=63e95660e713; isg=BA0NWbeTVNnkGPD1bEWHpBnZHCmH6kG8eiFcPU-SSaQcRi34FTpRjFvfsNogu1l0; l=fBQay7JuP_iW-f6OBOfZFurza77OSIRxSuPzaNbMi9fP96fBfCURW13WbRY6CnGVF6J6-3RpoAReBeYBqBdKnxv9nAHOraDmne_7Qn5..; tfstk=dNm2buwjNnKVhoPXJrqa4OUXjPqYXkdIocN_IADghSVD6qZZ7xG45jMg1llZ_fPbSIEjbbljNcgffAXaIbZ0WqN_G5rZBXJWOHtIHxETqBOBALi-HlFoPegpAxHYXWktZBtCbgblRGiKVOYclrAnC7mY78DqMUI_gGjimhUYTxb1jGmz3rkriOyh68bjWc3VsNz0e8PBULr6S181.',
	'Referer': 'https://dianying.taobao.com/index.htm?spm=a1z21.3046609.city.1.207c112a1KVjEr&n_s=new&city=110100',
	'Sec-Ch-Ua': '"Chromium";v="118", "Google Chrome";v="118", "Not=A?Brand";v="99"',
	'Sec-Ch-Ua-Mobile': '?0',
	'Sec-Ch-Ua-Platform': '"Windows"',
	'Sec-Fetch-Dest': 'empty',
	'Sec-Fetch-Mode': 'cors',
	'Sec-Fetch-Site': 'same-origin',
	'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36',
	'X-Requested-With': 'XMLHttpRequest',
}
request = urllib.request.Request(url=url, headers=headers)

reponse = urllib.request.urlopen(request)

content = reponse.read().decode('utf-8')

# 切片
content = content.split('(')[1].split(')')[0]
#
# with open('淘票票.json', 'w', encoding='utf-8') as fp:
# 	fp.write(content)

import json
import jsonpath

obj = json.load(open('淘票票.json','r',encoding='utf-8'))
city_list = jsonpath.jsonpath(obj,'$..showName')
print(city_list)


