import json
from time import sleep
from typing import Dict, List

from selenium import webdriver
from selenium.webdriver.common.by import By

'''
1.使用复用浏览器技术获取企业微信的cookie，点击添加成员
'''


class TestTest():
    def setup_method(self, method):
        # 复用浏览器
        chrome_opts = webdriver.ChromeOptions()
        chrome_opts.debugger_address = '127.0.0.1:9222'
        self.driver = webdriver.Chrome(options=chrome_opts)
        # self.driver.get("https://work.weixin.qq.com")
        self.driver.implicitly_wait(5)

    def teardown_method(self, method):
        self.driver.quit()

    def test_cookies(self):
        # sleep(20)
        # cookies = self.driver.get_cookies()
        # print(cookies)
        # with open("cookies.txt", 'w') as f:
        #     json.dump(cookies, f)
        with open("cookies.txt", 'r') as f:
            cookies: List[Dict] = json.load(f)

        for cookie in cookies:
            if "expiry" in cookie.keys():
                cookie.pop("expiry")
            self.driver.add_cookie(cookie)
        # self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
        self.driver.find_element(By.CSS_SELECTOR, '.index_service_cnt_itemWrap').click()
        self.driver.find_element(By.CSS_SELECTOR, '#username').send_keys("hello")
        self.driver.find_element(By.CSS_SELECTOR, '#memberAdd_acctid').send_keys("hello2")
        sleep(3)
