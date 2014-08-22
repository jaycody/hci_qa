#!/usr/bin/env python -tt
# -*- coding: utf-8 -*-

""" jstephens - tryouts: qa/support engineer - Healthy Communities Institute

Script to verify successful loading of HCI website.

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

class Test_site_load(unittest.TestCase):
    """Added 'Test' to class name"""

    def setUp(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)
    
    def test_site_load(self):
        """Verify we've landed on the correct page"""

        # set 'success' flag to True and wait to hear otherwise
        success = True
        
        wd = self.wd
        wd.get("http://www.healthycommunitiesinstitute.com/")
        
        # Assert title matches expected
        print "verifying webpage title"
        self.assertEqual("Healthy Communities Institute - The Leading Community Health Improvement Platform", wd.title)
        self.assertTrue(success)
    
    def tearDown(self):
        self.wd.quit()

if __name__ == '__main__':
    unittest.main()
