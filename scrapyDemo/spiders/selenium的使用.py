from selenium import webdriver

# 构造浏览器
chrome = webdriver.Chrome()

# 发送请求，访问url
url = 'http://www.baidu.com'
url = 'https://desk.zol.com.cn/bizhi/9996_119871_2.html'
chrome.get(url)

# 截图
chrome.save_screenshot('baidu.png')
print('截图成功')

# 获取源代码
html = chrome.page_source
print(html)

chrome.quit()