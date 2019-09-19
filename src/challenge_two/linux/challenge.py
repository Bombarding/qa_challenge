#################################################################
'''
@File:          script.py
@Author:        Alexander Steel
@Version:       0.0
@Usage:         py.test -v -s -r a --full-trace --color=yes --tb=long --cov && coverage xml
'''
#################################################################
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from pyvirtualdisplay import Display
import re, pytest
from selenium.common.exceptions import NoSuchElementException

def start_up(application_url):
    global web_driver, d
    d = Display(visible=0, size=(1920, 1080))
    d.start()
    web_driver = webdriver.Firefox(executable_path=r'/usr/local/bin/geckodriver')
    web_driver.get(application_url)
    
def register_new_account_section_one(register_link, 
                                     first_name, first_name_text, 
                                     last_name, last_name_text, 
                                     phone_number, phone_number_text, 
                                     email_address, email_address_text,
                                     country):
    web_driver.find_element_by_xpath(register_link).click()
    web_driver.find_element_by_name(first_name).send_keys(first_name_text)
    web_driver.find_element_by_name(last_name).send_keys(last_name_text)
    web_driver.find_element_by_name(phone_number).send_keys(phone_number_text)
    web_driver.find_element_by_name(email_address).send_keys(email_address_text)
    try:
        web_driver.find_element_by_xpath(country).click()
    except NoSuchElementException:
        pytest.fail("Expected Failure: Element Is not Available")
        
def book_a_flight(flight_link, destination_choice, future_destinations):
    web_driver.find_element_by_xpath(flight_link).click()
    try:
        nothing_clickable = web_driver.find_element_by_xpath(destination_choice)
    except NoSuchElementException:
        assert nothing_clickable == 0, "Nothing can be selected"
        web_driver.save_screenshot("C:/Users/Alex/workspace/qa_challenge/src/challenge_two/windows/flights_page.png")
    web_driver.find_element_by_xpath(future_destinations).click()
    
def tear_down(w_d, o_s):
    d.stop()
    w_d
    o_s
