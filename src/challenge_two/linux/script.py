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
import re

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
    web_driver.find_element_by_name(register_link).click()
    web_driver.find_element_by_name(first_name).send_keys(first_name_text)
    web_driver.find_element_by_name(last_name).send_keys(last_name_text)
    web_driver.find_element_by_name(phone_number).send_keys(phone_number_text)
    web_driver.find_element_by_name(email_address).send_keys(email_address_text)
    web_driver.find_element_by_xpath(country).click()
    
def book_a_flight(flight_link, destination_choice, future_destinations):
    web_driver.find_element_by_xpath(flight_link).click()
    nothing_clickable = web_driver.find_element_by_xpath(destination_choice)
    if(len(nothing_clickable) == 0):
        assert len(nothing_clickable) == 0, "Nothing can be selected"
        web_driver.save_screenshot("flights_page.png")
    web_driver.find_element_by_xpath(future_destinations).click()
    text_src = web_driver.page_source
    text_to_find = re.search(r'This section of our web site is currently under construction', text_src)
    assert (text_to_find in web_driver.text_src)
    
def tear_down(w_d, o_s):
    d.stop()
    w_d
    o_s
