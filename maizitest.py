from selenium import webdriver
from public import Login

b = webdriver.Firefox()
b.get("http://www.maiziedu.com")


Login().user_login(b)#调用登录模块

Login().user_logout(b)#调用退出模块git 