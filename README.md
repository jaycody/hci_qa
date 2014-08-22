##HCI - Website Test Plan
>a test automation plan for HCI's web page:
[www.healthycommunitiesinstitute.com](https://healthycommunitiesinstitute.com)  
see [HCI QA wiki](github.com/jayjaycody/hci_qa.wiki) for more test related documentation
________________________



###Overview:
[1. Objectives](#1-objectives)  
[2. Required Steps](#2-required-steps)  
[3. Assessment Phase](#3-assessment-phase)    
[4. Test Coverage](#4-test-coverage)    
[5. Proposed Approach](#5-proposed-approach)    
[6. Method](#6-method)    
[7. Defect Management](#7-defect-managment)    
[8. Resources and Notes](#8-resources-and-notes)  


_________________________________

###1. Objectives
- Continuously verify and validate HCI website functionality according to specs and requirements. 
- Build and deploy a test automation framework capable of continuous verification and validation of the HCI website.
- Devise and implement documentation conventions
- Review QA procedures (you know, for the new guy)

_________________________________

###2. Required Steps
1. **Elucidate existing workflow (website and test documentation)**  
    - what does it do? and how?
2. **Transform the website workflow into test scripts**
    - create test cases for each feature
    - create test suite for each use case
    - automate the verification of features and use cases
    - establish version control for test scripts and related documentation
3. **Automate test run**
    - trigger test scripts on checkin AND at regular intervals
4. **Pipe test output and documentation as required**
    - useful graphics and regular updates - to whom?
    - where is source of truth?

_________________________

###3. Assessment Phase
1. **Learn who's who.**
    - introductions, roles, responsibilities
2. **Learn the workflow and generate a UI sketch**
    - document the documentation procedures
    - for UI/UX, use [interactive sketching notation], Illustrator, and tablet
3. **Define current and desired requirements for functional testing** 
    - priorities
    - inputs, outputs, and expectations 
4. **Determine current and desired procedures for writing and running test scripts**
    - version control
    - test framework
    - test location
5. **Determine current and desired pipeline for test results**
    - examples of current failure notifications (content and delivery method)
    - Where do the auto-emailed failure notifications?  SMS?
    - Logs and log archives
6. **Identify process and next steps**
    - what requires updating? and what remains the same?
    - timeline and priortization of required updates
    - schedule deliverables

#####Assessment for Version 2 of the automation project:
- Define and test the operational requirements for HCI website (version 2 features)
    - eg. Performance, Stress and Volume

#####Assessment for Version 3 of the automation project:
- Define and test the functional and operational requirements for the **HCI Platform**



_____________________________

###4. Test Coverage  
This test plan covers basic UI and DB functionality as would be required for general user and client scenarios within a wide variety of environments and platforms.

####**In-Scope:**
#####Platforms and Environments
- **MOBILE:**
  - All major mobile browsers for current and recent versions iOS and Android
- **Desktop:**
  - All major browsers for all current and recent versions of Mac OS and Windows 
    
#####Features covered in this test plan
- **All Users:**
  - Page Load (main)
  - Subsidiary page loads
  - page content
  - internal links
  - drop down menus
  - HCI newsletter subscribe
  - Search
  - promotions (eg limited-time incentives)
  - on-demand webinar replay
  - videos (eg overview of HCI embedded options)
  - social-media links
  - online demos functionality
  - scheduling online demos
  - user feedback popup menu
- **Clients:**
  - client center
  - client login
  - switching client accounts
  - client permissions


####**v.2:**
- UX/usability 
- performance and load testing

####**v.3+:**
- automated test framework for the **The HCI Platform**

___________________________________

###5. Proposed Approach for v.1
A Selenium-based multi-platform test automation suite written in Python and executed on [SauceLabs] test servers  

**Components:**  
- [Selenium Builder]
- [Selenium WebDriver]
- [Python]
- [SauceLabs]
- [pytest]



___________________________________



###6. Method:

####Step 0. Devise test documentation procedures
- what's the current HCI documentation method?
- determine ongoing format (wiki? google docs, asana)
- solidify best practices (naming conventions, layout, frequency, etc)
- transfer, update, rebuild, rewrite, reintegrate current test documentation as required
- references:
  - [IEEE 823-2012]
  - [IEEE 1012-2004]
  - [IEEE 723-2014]

####Step 1. Build test suite prototype with [Selenium Builder]
- record and modify test cases
- organize test cases as suite
- execute test suite locally
- execute test suite remotely on multi platforms
- manage error reporting
- pro: 
    - rapid prototyping, extensive platform coverage
- con:
    - clumsy. lacks abstraction, won't scale

####Step 2. Create Python test scripts from prototype test suite
- from SE-Builder prototypes, port test cases to Python
- fix translation issues caused by porting test cases
- expand unittest features
- add command line interface to test cases

####Step 3. Modify Python test scripts to run multi-platform tests remotely
- to run test cases on remote servers, add:
```
webdriver.Remote()
```
- update setUp() to extend test case testing environment by specifying browsers, versions and platform
- add SauceLab account login for access to remote test servers
- improve error reporting: switch test framework from **unittest** to **[pytest]**
- why **[pytest]**
    - improved reporting
    - run test cases as a single test suite
    - test in parallel on multiple platforms
    - executing parallel tests from command line:
    ```
    $ py.test -n2 --boxed example.py
    ```
    - Example pytest response from parallel tests
    ```
        ============================== test session starts ==============================
        platform darwin -- Python 2.7.5 -- pytest-2.5.1
        plugins: xdist
        gw0 [2] / gw1 [2]
        scheduling tests via LoadScheduling
        ..
        =========================== 2 passed in 17.30 seconds ===========================
    ```
    - investigate [pytest_sauce]

####Step 4. Incorporate Continuous Integration Testing
- objective:  trigger execution of test suite at regular intervals AND upon change to code base
- connect [Github] <-> [Jenkins] <-> [SauceLabs]
- [Travis] - continuous integration platform
- Pingdom and Google App Engine for regular interval testing.  
- Alternative:  setup cron job on a remote server. (investigate)

####Step 5. Improve test script resilience: implement code abstractions
- [Page Object Model]
- Test Fixtures
- share common login procedures via pytest
- provide a test interface for developers and staff

####Step 6. Feedback - Recommendations - Alternatives

#####Feedback:  
- ?

#####Recommendations:    
- ?

#####Alternatives:
- python script using urllib2 running on Google App Engine triggered either from the command line or at regular intervals from a 3rd party (eg Pingdom)
- [robot + selenium video tutorials]
- [multi-mechanize]



__________________________________


###7. Defect Management:
#####error reporting:
- pytests
- Dashboard on SauceLabs
- triggered emails
- In-office Alert System
    - sirens and blinking lights triggered when Raspberry Pi detects error msg

#####bug tracking
- HCI's current system?
- Asana
- Jira 

_______________________________

###8. Resources and Notes
- [Building a CI System Using SE-Builder Github, Travis and SauceLabs](http://sauceio.com/index.php/2013/03/building-a-ci-system-using-selenium-builder-github-travis-and-sauce-labs/)
    - The great thing about this setup is that if you put your site code and your tests into the same GitHub repository, then whenever you update the site code, and whenever you update the tests, Travis will rerun your Selenium tests on Sauce OnDemand – and then send you an email about whether or not they still work!


_______________________________

[se-builder-testSuite]:
[interactive sketching notation]:http://www.linowski.ca/downloads/InteractiveSketchingNotation_0.1.pdf
[Selenium WebDriver]:http://docs.seleniumhq.org/docs/03_webdriver.jsp
[Python]:http://selenium-python.readthedocs.org
[pytest]:https://pypi.python.org/pypi/pytest/2.5.2
[unittest]:https://docs.python.org/2/library/unittest.html
[SauceLabs]:https://saucelabs.com
[Jenkins]:https://docs.saucelabs.com/ci-integrations/jenkins/
[Github]:http://sauceio.com/index.php/2013/03/building-a-ci-system-using-selenium-builder-github-travis-and-sauce-labs/
[pytest_sauce]:https://pypi.python.org/pypi/pytest_sauce
[Selenium Builder]:http://sauceio.com/index.php/2013/03/building-a-ci-system-using-selenium-builder-github-travis-and-sauce-labs/
[Robot Framework]:https://github.com/robotframework/robotframework
[Page Object Model]:http://martinfowler.com/bliki/PageObject.html
[unittests]:
[Automation Engineer]:http://linkedin.com/in/videoalchemy/
[HCI]:http://healthycommunitiesinstitute.com
[robot + selenium video tutorials]:http://robotframework.org/#documentation
[RIDE]:https://github.com/robotframework/RIDE/wiki
[multi-mechanize]:http://testutils.org/multi-mechanize/
[Travis]:https://travis-ci.org
