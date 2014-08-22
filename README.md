###HCI's prototype QA repo
>test scripts and related QA documenation for the [Healthy Communities Institute]  

__________________________

####repo directories:
#####[json_test_cases]
- json files representing test script prototypes recorded in the Firefox plugin: Selenium Builder
- each script is a test case that verifies a specific feature of the HCI website.
- to run the tests: import individual json files into Firefox's Selenium Buidler

#####[py_test_cases]
- Python unittests with Selenium Webdriver functionality.
- each script verifies a specific feature of the HCI website
- to run unittests from the command line (do not use the '.py' suffix)  

>
```cli
$ python -m unittest -v <name_of_script>
```

__________________________________
####Documenation:
#####[HCI Website Test Plan]
- a test automation plan for HCI's website: [www.healthycommunitiesinstitute.com] 

#####[HCI QA Wiki]
- a wiki for test documentation and qa procedures related to HCI

_________________________________
####ToDo:
#####HCI Website Testing [ToDo]:
- [] implement Page Object Model for test cases
- [] Add Remote for off-site testing
- [] connect SauceLabs Account
- [] investigate SauceLabs + MeterSomething for front-end + load testing
- [] add test fixture class to run as test cases as suite in pytest
- [] track down the bug with selenium action_chains
- [] add Chrome and Safari plugins for Selenium
- [] Sauce Labs dashboard and error handling
- [] Sauce Labs test configuration for multiplatform

#####Documentation [ToDo]:
- [] add READMEs to script directories in main repo
- [] 'end-of-shift_wiki-update' as described by Charles Stross in 'Rule 34'
- [] detail the assessment phase from the website [test plan](HCI Website Test Plan)

#####HCI Platform [ToDo]:
______________________________________

[py_test_cases]:https://github.com/jayjaycody/hci_qa/tree/master/py_test_cases
[HCI Website Test Plan]:https://github.com/jayjaycody/hci_qa/wiki/HCI-Website-Test-Plan
[Healthy Communities Institute]:https://healthycommunitiesinstitute.com
[www.healthycommunitiesinstitute.com]:https://healthycommunitiesinstitute.com
[HCI QA Wiki]:https://github.com/jayjaycody/hci_qa/wiki
[json_test_cases]:https://github.com/jayjaycody/hci_qa/tree/master/json_test_cases
