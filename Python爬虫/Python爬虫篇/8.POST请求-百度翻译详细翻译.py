import urllib.request

url = 'https://fanyi.baidu.com/v2transapi?from=en&to=zh'

headers = {
    'Accept':' */*',
    # 'Accept-Encoding':' gzip, deflate, br',
    # 'Accept-Language':' zh-CN,zh;q=0.9',
    # 'Acs-Token':' 1695539181603_1695539185797_E6gWPppimk90LK1USGk0pnRLFy99jF6/1mtszbzT50tf6bWkRBTFsAPC/HiBAYTWg4yJgOuEP3JtS0eqc+fItJ5o/XpFlYldI5ACIzF/ufKrXgYq6SjTBKDPiN+fNIGXqrHY842N4pHTkyLmmxiApCQtyQx97Xq6d1X/WrC9IhRTibdA68gsyF3tYDJr/ePXSNJX6RwZF1Whv+lQUS72cGTqpdH/rfXm6MlycUFjh8M/hxdDNYiYiSJ/f46TKwVct2up6HmDZ9i7x1V02qmA8WZcHZGVQMTeOZHjHuRHbxtc9HQq0zfrQoeOOCj8xZXCIQYYS+GdnOu2OF67zb5hjARnLIl4yzUKkCdL3MDmWWpT2W14cVCtty2vyEH3bhYICTFLg2a1pWlEYLHCzq5DTY1SqqsU8u5gGC9G8LQsZs3fp2HCISOAmaSdXUVYYWCrqIxj0enNUMghRgBEsshzp08NL3aCHNOzS4N5sTt5pC64Wak8bEoea8dZdxgSvBvDCyW2KyLzXb42hnKrsLtJ/g==',
    # 'Connection':' keep-alive',
    # 'Content-Length':' 134',
    # 'Content-Type':' application/x-www-form-urlencoded; charset=UTF-8',
    'Cookie ': 'BDUSS=y1seEZ5cWx0OXpocWgxOE1nOWpVUn5vUmhqOGhGem5SWTN-ZjdLV0otNUkxRFJsRVFBQUFBJCQAAAAAAQAAAAEAAADuqtVIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAEhHDWVIRw1lT; BDUSS_BFESS=y1seEZ5cWx0OXpocWgxOE1nOWpVUn5vUmhqOGhGem5SWTN-ZjdLV0otNUkxRFJsRVFBQUFBJCQAAAAAAQAAAAEAAADuqtVIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAEhHDWVIRw1lT; newlogin=1; BIDUPSID=81082406306958A31A6229007A82DB57; PSTM=1695528939; BAIDUID=81082406306958A31A6229007A82DB57:SL=0:NR=10:FG=1; BA_HECTOR=a50kakal8k04ah8l00ala4ao1igvdvh1p; ZFY=KH76J:AQVSgBOCfa4NaliEDwkVxtkWbNkYwsqKZy8kmo:C; BAIDUID_BFESS=81082406306958A31A6229007A82DB57:SL=0:NR=10; APPGUIDE_10_6_5=1; REALTIME_TRANS_SWITCH=1; FANYI_WORD_SWITCH=1; HISTORY_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; ab_sr=1.0.1_NWZkMzE5MDE1N2JkZDk4YjE2Yzk1YzliYzg2MWJhOWFlZjIyMjM2OTkxMzE0MDA1NzQxNjc2MWFkM2FmZmI1ZDlkYzkxOWEwNTExYmQ5MWM2OGUwZTUxNjRhODA9MTNlYjI2MWFiYTM0NGYwNjU1ZjVkMDRhM2RiZWQ4NWM2OWUwYjE1YWNmYTkxMTIzZjE4NjViMWQ3ZjRmODZlMzcxNTE5NTRkODNiMGNmN2VkYTg0MGUwMDljOTI0MjdkY2Y1ODM4OWE2NzkyZjMzYTk3YmNjZjFhN2EyOTA1MGVjYTc2NDViNDBjNTQ5MWU2MWUyYjQ4ZTA8YmY1ZDU4'
    # 'Host':' fanyi.baidu.com',
    # 'Origin: https':'//fanyi.baidu.com',
    # 'Referer: https':'//fanyi.baidu.com/',
    # 'Sec-Fetch-Dest':' empty',
    # 'Sec-Fetch-Mode':' cors',
    # 'Sec-Fetch-Site':' same-origin',
    # 'User-Agent':' Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
    # 'X-Requested-With':' XMLHttpRequest',
}

data = {
    'from':' en',
    'to':' zh',
    'query':' spider',
    'simple_means_flag':' 3',
    'sign':' 63766.268839',
    'token':' 06af6cac17b778166c70730f42737fe9',
    'domain':' common',
    'ts':' 1695539185776',
}
# post请求必须编码,并且要调用encode方法
data = urllib.parse.urlencode(data).encode('utf-8')

# UA制定
request = urllib.request.Request(url=url,data=data,headers=headers)

# 模拟发送请求
response = urllib.request.urlopen(request)

# 获取数据
content = response.read().decode('utf-8')

# 打印数据
print(content)


'''下面总结一下urllib处理GET请求与POST请求的区别:

post请求的参数必须编码+转码,也即编码之后,必须调用encode方法:

data = urllib.parse.urlencode(data).encode('utf-8')
但get请求的参数只需要进行编码即可,也即:

data = urllib.parse.urlencode(data)
post请求的参数放在请求对象的定制过程中,而不是拼接字符串:

request = urllib.request.Request(url = url,data = data,headers = headers)
response = urllib.request.urlopen(request)
但get请求的参数使用字符串拼接在url上:

url = base_url + uni_data
request = urllib.request.Request(url = url,headers = headers)
response = urllib.request.urlopen(request)
'''
