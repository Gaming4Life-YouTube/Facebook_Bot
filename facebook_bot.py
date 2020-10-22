"""
Facebook Bot
"""

from selenium import webdriver
from selenium.common.exceptions import *
import sys


class facebook_bot():
    def __init__(self, driver, url, username, password):
        chrome_options = webdriver.ChromeOptions()
        #ChromeOptions options = new ChromeOptions()
        prefs = {"profile.default_content_setting_values.notifications": 2}
        chrome_options.add_experimental_option("prefs", prefs)
        chrome_options.add_argument("--user-data-dir = /Users/derekcalabro/Library/Application Support/Google/Chrome/Default")
        #chrome_options.add_argument("--user-data-dir = /Users/derekcalabro/Desktop/Python_Projects/Facebook_Bot/Chrome/Custom")
        chrome_options.add_argument("--profile-directory = Default")
        #chrome_options.add_argument("--profile-directory = Custom")
        chrome_options.add_argument("--disable-notifications")

        self.driver = webdriver.Chrome(driver)
        self.driver.get(url)
        self.login(username, password)

    def show_exception(self, e):
        print(e)
        self.driver.quit()
        sys.exit()

    def login(self, username, password):
        try:
            email_box = self.driver.find_element_by_id("email")
            email_box.send_keys(username)

            pass_box = self.driver.find_element_by_id("pass")
            pass_box.send_keys(password)

            login_btn = self.driver.find_element_by_id("u_0_b")
            login_btn.click()

        except NoSuchElementException as e:
            self.show_exception(e)

        except Exception as e:
            self.show_exception()

    def post_on_wall(self, message):
        go_home = self.driver.find_element_by_class_name("_3qcu _cy7")
        go_home.click()
        #post_box = self.driver.find_element_by_tag_name("textarea")
        post_box = self.driver.find_element_by_class_name("_1mwp navigationFocus _395 _1mwq _4c_p _5bu_ _3t-3 _34nd _21mu _5yk1")
        post_box.send_keys(message)

        #post_btn = self.driver.find_element_by_class_name("kr520xx4 b5wmifdl ms05siws pnx7fd3z b7h9ocf4 pmk7jnqg j9ispegn kr9hpln1")
        post_btn = self.driver.find_element_by_class_name("_1mf7 _4r1q _4jy0 _4jy3 _4jy1 _51sy selected _42ft")
        post_btn.click()

