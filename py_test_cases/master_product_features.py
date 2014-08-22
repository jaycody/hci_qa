# -*- coding: utf-8 -*-
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.common.action_chains import ActionChains
import time, unittest

def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False

class master_product_features(unittest.TestCase):
    def setUp(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)
    
    def test_master_product_features(self):
        success = True
        wd = self.wd
        wd.get("http://www.healthycommunitiesinstitute.com/")
        self.assertEqual("Healthy Communities Institute - The Leading Community Health Improvement Platform", wd.title)
        ActionChains(wd).move_to_element(wd.find_element_by_link_text("BLOG")).perform()
        ActionChains(wd).move_to_element(wd.find_element_by_id("menu-main")).perform()
        ActionChains(wd).move_to_element(wd.find_element_by_id("container-inner")).perform()
        ActionChains(wd).move_to_element(wd.find_element_by_link_text("ABOUT HCI")).perform()
        ActionChains(wd).move_to_element(wd.find_element_by_css_selector("#menu-item-49 > ul.sub-menu")).perform()
        ActionChains(wd).move_to_element(wd.find_element_by_css_selector("#menu-item-633 > a")).perform()
        ActionChains(wd).move_to_element(wd.find_element_by_link_text("Leadership")).perform()
        ActionChains(wd).move_to_element(wd.find_element_by_link_text("Join Our Team")).perform()
        if not (len(wd.find_elements_by_link_text("Join Our Team")) != 0):
            success = False
            print("verifyElementPresent failed")
        wd.find_element_by_link_text("Join Our Team").click()
        ActionChains(wd).move_to_element(wd.find_element_by_css_selector("html")).perform()
        ActionChains(wd).move_to_element(wd.find_element_by_css_selector("div.widget-inner")).perform()
        ActionChains(wd).move_to_element(wd.find_element_by_id("container-inner")).perform()
        ActionChains(wd).move_to_element(wd.find_element_by_css_selector("img.slider-image")).perform()
        ActionChains(wd).move_to_element(wd.find_element_by_css_selector("div.separator")).perform()
        ActionChains(wd).move_to_element(wd.find_element_by_css_selector("div.post-content")).perform()
        ActionChains(wd).move_to_element(wd.find_element_by_css_selector("div.su-spoiler-title")).perform()
        ActionChains(wd).move_to_element(wd.find_element_by_css_selector("span.su-spoiler-icon")).perform()
        if not (len(wd.find_elements_by_css_selector("span.su-spoiler-icon")) != 0):
            success = False
            print("verifyElementPresent failed")
        wd.find_element_by_css_selector("span.su-spoiler-icon").click()
        ActionChains(wd).move_to_element(wd.find_element_by_css_selector("div.su-spoiler-title")).perform()
        if not ("Master the product features" in wd.find_element_by_tag_name("html").text):
            success = False
            print("verifyTextPresent failed")
        if not ("QA/Support Engineer" in wd.find_element_by_tag_name("html").text):
            success = False
            print("verifyTextPresent failed")
        self.assertTrue(success)
    
    def tearDown(self):
        self.wd.quit()

if __name__ == '__main__':
    unittest.main()
