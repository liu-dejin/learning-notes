# cookie登录 绕过登录爬取
# 个人信息页面是utf-8  但还是报编码错误,跳转到了登录界面  登录界面是不是utf-8
#

import urllib.request

url = 'https://h5.qzone.qq.com/mqzone/profile?hostuin=1913148409&no_topbar=1&srctype=10&stat=&g_f=2000000209#mine?res_uin=1913148409&ticket='

headers = {
	'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36 Edg/117.0.2045.60',

'Cookie':'pac_uid=0_b0f349f6fdae7; iip=0; pgv_pvid=939163046; eas_sid=P1G6Y9s5s6s0q8j7V613V894e6; RK=pjFgeLr9O1; ptcz=93113c1d32d3a6afe66522506cf76e202974ebe2d2002a95b92811e653ebce4f; _clck=3hbd4w|1|ffd|0; _qpsvr_localtk=0.14508677108922896; pgv_info=ssid=s2549857612; uin=o1913148409; skey=@0Qd2E1qs2; p_uin=o1913148409; pt4_token=TQ4rBGTrlqxsMDuaYLCLOypChGxgcOk4EH4aGb6*qSw_; p_skey=17oYziCBu51rmzI32PUlTWGa-2VLCBMs41K-FGrD9GI_; __Q_w_s_hat_seed=1',
'Referer':'https://user.qzone.qq.com/'	#做图片防盗链
}

request = urllib.request.Request(url=url, headers=headers)

response = urllib.request.urlopen(request)

content = response.read().decode('utf-8')

print(content)

with open('QQ空间.html', 'w', encoding='utf-8') as fp:
	fp.write(content)
