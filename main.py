# encoding=utf-8
import argparse
import json
import time
import traceback
from typing import Dict
from selenium.webdriver.firefox.options import Options

from selenium import webdriver


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--config_file', required=True)
    parser.add_argument('--once', action='store_true', dest='once')
    return parser.parse_args()


class TelecomRebootTool(object):
    def __init__(self, config_dict: Dict):
        self.config_dict = config_dict
        self.driver_executable_path = config_dict.get("driver_executable_path")
        self.proxy = config_dict.get('proxy', None)
        self.home_url = config_dict.get("url")
        self.loop_seconds = int(config_dict.get("loop_seconds"))
        print(config_dict)
        profile = webdriver.FirefoxProfile()
        options = Options()
        options.headless = True
        if self.proxy is not None:
            ip, port = self.proxy.split(':')
            profile.set_preference('network.proxy.type', 1)
            profile.set_preference('network.proxy.socks', ip)
            profile.set_preference('network.proxy.socks_port', int(port))
        self.driver = webdriver.Firefox(executable_path=self.driver_executable_path,
                                        firefox_profile=profile,
                                        options=options)
        print("headless webdriver inited.")
        self.driver.get(self.home_url)

    def loop(self):
        while True:
            try:
                self.reboot()
                print("sleep for {} seconds".format(self.loop_seconds))
                time.sleep(self.loop_seconds)
            except:
                traceback.print_exc()

    def reboot(self):
        print("try reboot")
        # login
        self.driver.get(self.home_url)
        login_username_box = self.driver.find_element_by_id("login_username")
        login_username_box.send_keys(self.config_dict.get("username"))
        login_password_box = self.driver.find_element_by_id("login_password")
        login_password_box.send_keys(self.config_dict.get("passwd"))
        login_btn = self.driver.find_element_by_xpath('//button[text()="确认登录"]')
        login_btn.click()
        time.sleep(2)
        # find element
        frame = self.driver.find_element_by_tag_name("frame")
        self.driver.switch_to.frame(frame)
        time.sleep(2)
        manager_box = self.driver.find_element_by_xpath('//span[text()="管  理"]/..')
        manager_box.click()
        manager_box = self.driver.find_element_by_xpath('//span[text()="设备管理"]/..')
        manager_box.click()

        self.driver.switch_to.default_content()
        frame = self.driver.find_element_by_name("mainFrame")
        self.driver.switch_to.frame(frame)
        time.sleep(2)
        reboot_btn = self.driver.find_element_by_xpath('//input[@value="保存/重启"]')
        reboot_btn.click()
        print("reboot click")


if __name__ == '__main__':
    args = get_args()
    print(args)

    with open(args.config_file) as fop:
        config_dict = json.load(fop)
    rebootTool = TelecomRebootTool(config_dict)
    if args.once:
        rebootTool.reboot()
    else:
        rebootTool.loop()
