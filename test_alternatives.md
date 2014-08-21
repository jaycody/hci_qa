> alternative test methods and tools for HCI's website
______________________________

    
#####[Robot Framework]
- Robot Framework is a Python-based keyword-driven test automation framework with an easy-to-use tabular syntax for creating test cases. Its testing capabilities can be extended by test libraries implemented either with Python or Java. Users can also create new keywords from existing ones using the same simple syntax that is used for creating test cases.
- [Intro to Robot Framework](https://www.youtube.com/watch?v=CrkfmqFbJpU) - video from uTest
- Robot Framework, implemented with Selenium Library, allows for quick creation of keyword based Automation scripts
Implementation of a keyword library is simplified and allows for automation scripts that are human readable. Implemented correctly, users end up with executable documents that are automation scripts and documented requirements. Robot Framework includes several built in libraries and can be extended using python
- [RIDE] - the test data editor for Robot Framework test data
- acceptance testing framework
- **keyword** driven
- selenium plugins
- installation:
  - pip install robotframeworks
- good at separating test cases from the test code.
- simple test case
  - user can create an account and login.  ACTION: create valid user.  
- data drive the tests:
  - Test Cases:  passwordsTooLong..  passwordsTooShort
- Jenkins integration with Jenkins Plugins
- [robot + selenium video tutorials]
- rebot plugin aggregates all reporting feedback

#####[multi-mechanize] - performance test framework
- scripts written similar to Martin's padospeed.  
- only way to test scalalbitity and stability before your users do
- what does it provide?
  - report genration
  - graphs
  - aggregrates statistics
  - easily scalable
  - pure python
- setup the config.cfg file
  - run_time, rampup, results_ts_interval, progress_bar, xml_report
- performance trend feedback from JENKINS

#####lettuce
- python's version of Ruby's Cucumber
- Behavior Driven Development (BDD) done as Test Driven Development (TDD) in **Gherkin**
- uses *Gherkin* - "business readable, domain specific language"
```
Given I have the input foo
When I compute the bar of foo
Then I see the expected number bus
```
