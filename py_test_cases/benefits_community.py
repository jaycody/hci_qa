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

class benefits_community(unittest.TestCase):
    def setUp(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)
    
    def test_benefits_community(self):
        success = True
        wd = self.wd
        wd.get("http://www.healthycommunitiesinstitute.com/")
        self.assertEqual("Healthy Communities Institute - The Leading Community Health Improvement Platform", wd.title)
        ActionChains(wd).move_to_element(wd.find_element_by_link_text("SOLUTIONS")).perform()
        ActionChains(wd).move_to_element(wd.find_element_by_css_selector("ul.sub-menu")).perform()
        ActionChains(wd).move_to_element(wd.find_element_by_link_text("For Hospitals")).perform()
        wd.find_element_by_link_text("For Hospitals").click()
        if wd.current_url != "http://www.healthycommunitiesinstitute.com/hospital-solutions/":
            success = False
            print("verifyCurrentUrl failed")
        wd.find_element_by_xpath("//div[@class='post-content']/div[7]/div[1]/span").click()
        if not ("is more than just technology" in wd.find_element_by_tag_name("html").text):
            success = False
            print("verifyTextPresent failed")
        wd.find_element_by_xpath("//div[@class='post-content']/div[7]/div[1]/span").click()
        self.assertTrue(success)
    
    def tearDown(self):
        self.wd.quit()

if __name__ == '__main__':
    unittest.main()
