#!/usr/bin/env python -tt
# -*- coding: utf-8 -*-

""" jstephens - tryouts: qa/support engineer - Healthy Communities Institute

Script to test the presence of the solutions-hospital webpage.

ToDo:  
[] Page Object Model for test cases
[] Add Remote for off-site testing

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

class Test_solutions_hospital(unittest.TestCase):
    """Added 'Test' to the class name"""

    def setUp(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)
    
    def test_solutions_hospital(self):
        """Verify the presence of the solutions-hospital page"""

        # set success flag to True and await otherwise
        success = True

        wd = self.wd
        wd.get("http://www.healthycommunitiesinstitute.com/")
        
        # Verify we've landed on the correct page
        print "Verifying website title"
        self.assertEqual("Healthy Communities Institute - The Leading Community Health Improvement Platform", wd.title)
        ActionChains(wd).move_to_element(wd.find_element_by_link_text("SOLUTIONS")).perform()
        ActionChains(wd).move_to_element(wd.find_element_by_css_selector("ul.sub-menu")).perform()
        ActionChains(wd).move_to_element(wd.find_element_by_link_text("For Hospitals")).perform()
        wd.find_element_by_link_text("For Hospitals").click()
        
        # Verifying correct url
        print "Verifying webpage url"
        if wd.current_url != "http://www.healthycommunitiesinstitute.com/hospital-solutions/":
            success = False
            print "verifyCurrentUrl failed"
        
        # Did we make it all the way without triggering the flag?
        self.assertTrue(success)
    
    def tearDown(self):
        self.wd.quit()

if __name__ == '__main__':
    unittest.main()
