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
- to run unittests from the command line
```cli
$ python -m unttest -v name_of_script
# do not use the '.py' suffix
```

__________________________________
####Documenation:
#####[HCI Website Test Plan]
- a test automation plan for HCI's website: [www.healthycommunitiesinstitute.com] 

#####[HCI QA Wiki]
- a wiki for test documentation and qa procedures related to HCI






[HCI Website Test Plan]:https://github.com/jayjaycody/hci_qa/wiki/HCI-Website-Test-Plan
[Healthy Communities Institute]:https://healthycommunitiesinstitute.com
[www.healthycommunitiesinstitute.com]:https://healthycommunitiesinstitute.com
[HCI QA Wiki]:https://github.com/jayjaycody/hci_qa/wiki
[json_test_cases]:https://github.com/jayjaycody/hci_qa/tree/master/json_test_cases
