# 模拟浏览器功能，自动执行js代码，实现动态加载
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

path = 'chromedriver.exe'
service = Service(path)  # Here
browser = webdriver.Chrome(service=service)  # Here


url = 'http://www.jd.com'

browser.get(url)

# page_source
content = browser.page_source

print(content)
