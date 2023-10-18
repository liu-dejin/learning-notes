import urllib.request

# 下载网页
url_page = 'http://www.baidu.com'
# 使用urillib.request.urlretrieve() 函数，
# 传参分别是url(网页的地址路径)、filename(网页文件的名字)
urllib.request.urlretrieve(url_page,'baidu.html')

# 下载图片
url_img = 'https://gimg2.baidu.com/image_search/src=http%3A%2F%2Fsafe-img.xhscdn.com%2Fbw1%2F1b51f9c2-ec4b-4803-90e1-94511c6a5698%3FimageView2%2F2%2Fw%2F1080%2Fformat%2Fjpg&refer=http%3A%2F%2Fsafe-img.xhscdn.com&app=2002&size=f9999,10000&q=a80&n=0&g=0n&fmt=auto?sec=1698121073&t=e9cf66779106ad001481de09358b4de7'

urllib.request.urlretrieve(url_img,'鞠婧祎.jpg')

# 下载视频
url_video = 'blob:https://content-static.cctvnews.cctv.com/d9ece7ca-4b47-4943-9c59-1c01621bbeae'
urllib.request.urlretrieve(url_video,'亚运会.mp4')