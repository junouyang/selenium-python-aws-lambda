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


def get_element(browser, getfunc, message):
    element = None
    number = 0
    while not element and number < 40:
        try:
            element = getfunc(browser)
        except:
            time.sleep(1)
        number += 1
    if not element:
        raise ValueError("element not found: " + message)
    return element


def lambda_handler(event, context):
    # TODO implement
    print("start 一亩三分地签到!")
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

    get_element(browser, lambda b: b.find_element_by_id("ls_username"), "username").send_keys(os.environ['USERNAME'])
    print("username filled")

    password = browser.find_element_by_id("ls_password")
    password.send_keys(os.environ['PASSWORD'])
    print("password filled")

    password.submit()
    print("submitted")

    get_element(browser, lambda b: b.find_element_by_xpath("//a[contains(@onclick,'dsu_paulsign')]"), "qiandao").click()
    print("go to 签到")

    get_element(browser, lambda b: b.find_element_by_xpath(
        "//img[contains(@src,'source/plugin/dsu_paulsign/img/emot/kx.gif')]"), "kaixin").click()
    print("click 开心")

    browser.find_element_by_id("todaysay").send_keys("我要签到领奖我要签到领奖！")
    print("fill 心情")

    browser.find_element_by_xpath("//button[contains(@onclick, 'qiandao')]").click()
    print("click 签到")
    return ""