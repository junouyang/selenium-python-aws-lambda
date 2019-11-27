from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os
import time

# chrome_options = Options()
# chrome_options.add_argument('--headless')
# chrome_options.add_argument('--no-sandbox')
# chrome_options.add_argument('--disable-gpu')
# chrome_options.add_argument('--window-size=1280x1696')
# chrome_options.add_argument('--user-data-dir=/tmp/user-data')
# chrome_options.add_argument('--hide-scrollbars')
# chrome_options.add_argument('--enable-logging')
# chrome_options.add_argument('--log-level=0')
# chrome_options.add_argument('--v=99')
# chrome_options.add_argument('--single-process')
# chrome_options.add_argument('--data-path=/tmp/data-path')
# chrome_options.add_argument('--ignore-certificate-errors')
# chrome_options.add_argument('--homedir=/tmp')
# chrome_options.add_argument('--disk-cache-dir=/tmp/cache-dir')
# chrome_options.add_argument('user-agent=Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36')
# chrome_options.binary_location = os.getcwd() + "/bin/headless-chromium"

# driver = webdriver.Chrome(chrome_options=chrome_options)

def lambda_handler(event, context):
    # TODO implement
    print("Starting google.com")
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--window-size=1280x1696')
    chrome_options.add_argument('--user-data-dir=/tmp/user-data')
    chrome_options.add_argument('--hide-scrollbars')
    chrome_options.add_argument('--enable-logging')
    chrome_options.add_argument('--log-level=0')
    chrome_options.add_argument('--v=99')
    chrome_options.add_argument('--single-process')
    chrome_options.add_argument('--data-path=/tmp/data-path')
    chrome_options.add_argument('--ignore-certificate-errors')
    chrome_options.add_argument('--homedir=/tmp')
    chrome_options.add_argument('--disk-cache-dir=/tmp/cache-dir')
    chrome_options.add_argument('user-agent=Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36')
    chrome_options.binary_location = os.getcwd() + "/bin/headless-chromium"

    browser = webdriver.Chrome(chrome_options=chrome_options)
    browser.get('https://www.1point3acres.com/bbs')
    browser.find_element_by_id("ls_username").send_keys(os.environ['USERNAME'])
    print("username filled")

    password = browser.find_element_by_id("ls_password")
    password.send_keys("os.environ['PASSWORD']")
    print("password filled")

    password.submit()
    print("submit filled")

    time.sleep(5)
    browser.find_element_by_partial_link_text("签到领奖").click()
    print("go to qiandao")

    time.sleep(2)
    browser.find_element_by_xpath("//img[contains(@src,'source/plugin/dsu_paulsign/img/emot/kx.gif')]").click()
    print("click kaixin qiandao")

    browser.find_element_by_id("todaysay").send_keys("我要签到领奖我要签到领奖！")
    print("fill today mood")

    browser.find_element_by_xpath("//button[contains(@onclick, 'qiandao')]").click()
    print("click qiandao")
    return ""
