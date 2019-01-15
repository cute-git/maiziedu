from selenium import webdriver
# 登录
def login(): 
    b.find_element_by_class_name("globalLoginBtn").click()
    b.find_element_by_id(uid).clear()
    b.find_element_by_id(uid).send_keys(username)
    b.find_element_by_id(pid).clear()
    b.find_element_by_id(pid).send_keys(pwd)
# 退出
def logout():
    b.quit()

b = webdriver.Firefox()
b.get("http://www.maiziedu.com")

uid = "id_account_l"
pid = "id_password_l"
username = "18230343435"
pwd = "18230343435"

login() #引用登录的方法

logout() #引用退出的方法


# 线性测试
# b = webdriver.Firefox()
# b.get("http://www.maiziedu.com")

# username = "18230343435"
# pwd = "18230343435"

# b.find_element_by_class_name("globalLoginBtn").click()
# b.find_element_by_id("id_account_l").clear()
# b.find_element_by_id("id_account_l").send_keys(username)
# b.find_element_by_id("id_password_l").clear()
# b.find_element_by_id("id_password_l").send_keys(pwd)

# b.find_element_by_id("login_btn").click()

