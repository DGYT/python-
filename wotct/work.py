'''
C:\Windows\System32>TRACERT.EXE
坦克世界公测服务器在德国，通过上述命令获得途径的路由器ip，每次输入浏览器太繁琐。

requests 头部等简单模拟无法成功，所以使用selenium来进行，重复查询。

先从文件 1 里读取要查询的ip地址，然后正则匹配获取ip，然后输出到文件1.txt

有些ip会重复，没有去重，复制cmd内容到文件1时注意下就可以了
'''
from selenium import webdriver
import re

pattern = re.compile('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}')
f = open('1', 'r')
buff = f.read()
ip_table = pattern.findall(buff)
driver = webdriver.PhantomJS()
driver.get("https://www.opengps.cn/Data/IP/IPSearch.aspx")
for ip in ip_table:
    ip_textbox = driver.find_element_by_xpath('//*[@id="txtIP"]')
    btn = driver.find_element_by_xpath('//*[@id="btnSearch"]')
    ip_textbox.clear()
    ip_textbox.send_keys(ip)
    btn.click()
    content = driver.find_element_by_xpath('//*[@id="lblMsg"]')
    text = content.text
    with open('1.txt', 'a') as f:
        f.write('-------------------------**************-------------------------' + '\n')
        f.write(text + '\n')
        f.write('-------------------------**************-------------------------' + '\n')
