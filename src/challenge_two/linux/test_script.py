#################################################################
'''
@File:          test_script.py
@Author:        Alex Steel
@Version:       0.0
@Usage:         py.test -v -s -r a --full-trace --color=yes --tb=long --cov && coverage xml
'''
#################################################################
import imp
script = imp.load_source('module.name', '/home/asteel/qa_challenge/src/challenge_two/linux/script.py')
configuration = imp.load_source('module.name', '/home/asteel/qa_challenge/src/challenge_two/configuration.py')
import os

def test_start_up():
    script.start_up(configuration.challenge_information[0])

def test_register_new_account_section_one():
    script.register_new_account_section_one("//a[contains(text(),'REGISTER')]",
                                             "firstName", "test",
                                             "lastName", "user",
                                             "phone", "1111111111",
                                             "userName", "email@email.com",
                                             "//select[@name='country']/option[text()='UNITED KINGDOM']")

def test_book_a_flight():
    script.book_a_flight("//a[contains(text(),'Flights')]",
                          "//tr[3]/td/table/tbody/tr/td/font",
                          "//a[contains(text(),'featured vacation destinations')]")

def test_tear_down():
    script.tear_down(script.web_driver.quit(), 
                        os.system('coverage xml'))
