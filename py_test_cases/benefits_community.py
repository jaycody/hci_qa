#!/usr/bin/env python -tt
# -*- coding: utf-8 -*-

"""jstephens - tryouts: qa/support engineer - Healthy Communities Institute

Script to verify the presence of the 'Join Our Community' drop down message 
on the 'hospital-solutions' page


run as unittest:
$ python -m unittest -v benefits_community
"""


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
        
        # Set 'success' flag as True -- to be tripped if any verification fails
        success = True
        
        wd = self.wd
        wd.get("http://www.healthycommunitiesinstitute.com/")
        
        # Check that title matches expectation
        self.assertEqual("Healthy Communities Institute - The Leading Community Health Improvement Platform", wd.title)
        print "Verifying page title matches expected", wd.title
        
        ActionChains(wd).move_to_element(wd.find_element_by_link_text("SOLUTIONS")).perform()
        ActionChains(wd).move_to_element(wd.find_element_by_css_selector("ul.sub-menu")).perform()
        ActionChains(wd).move_to_element(wd.find_element_by_link_text("For Hospitals")).perform()
        wd.find_element_by_link_text("For Hospitals").click()
        
        # Check for expected URL
        print "Verifying current url", wd.current_url
        if wd.current_url != "http://www.healthycommunitiesinstitute.com/hospital-solutions/":
            success = False
            print("verifyCurrentUrl failed")
        wd.find_element_by_xpath("//div[@class='post-content']/div[7]/div[1]/span").click()
        
        # Look for expected text in entire page  <!-- this could be more precise -->
        print "Verifying the presence of specific text: 'is more than just technology'"
        if not ("is more than just technology" in wd.find_element_by_tag_name("html").text):
            success = False
            print("verifyTextPresent failed")
        
        wd.find_element_by_xpath("//div[@class='post-content']/div[7]/div[1]/span").click()
        self.assertTrue(success)
    
    def tearDown(self):
        self.wd.quit()

if __name__ == '__main__':
    unittest.main()
