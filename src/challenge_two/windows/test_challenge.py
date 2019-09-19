#################################################################
'''
@File:          test_script.py
@Author:        Alex Steel
@Version:       0.0
@Usage:         py.test -v -s -r a --full-trace --color=yes --tb=long --cov && coverage xml
'''
#################################################################
from challenge_two.windows import challenge
import os
from challenge_two import configuration
def test_start_up():
    challenge.start_up("C:\Webdrivers\Test\chromedriver.exe", 
                   configuration.challenge_information[0])
    
def test_register_new_account_section_one():
    challenge.register_new_account_section_one("//a[contains(@href, 'mercuryregister.php')]",
                                             "firstName", "test",
                                             "lastName", "user",
                                             "phone", "1111111111",
                                             "userName", "email@email.com",
                                             "//select[@name='country']/option[text()='UNITED KINGDOM']")

def test_book_a_flight():
    challenge.book_a_flight("//a[contains(text(),'Flights')]",
                          "//tr[3]/td/table/tbody/tr/td/font",
                          "//a[contains(text(),'featured vacation destinations')]")

def test_tear_down():
    challenge.tear_down(challenge.web_driver.quit(), 
                                     os.system('coverage xml'))
