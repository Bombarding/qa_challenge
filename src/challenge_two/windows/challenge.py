#################################################################
'''
@File:          script.py
@Author:        Alexander Steel
@Version:       0.0
@Usage:         py.test -v -s -r a --full-trace --color=yes --tb=long --cov && coverage xml
'''
#################################################################
from selenium import webdriver
import re, pytest
from selenium.common.exceptions import NoSuchElementException

def start_up(driver_location, application_url):
    global web_driver
    browser_options = webdriver.ChromeOptions()
    browser_options.add_argument("start-maximized") #=> Runs System in Maximized Browser, for Debugging
    #browser_options.add_argument("--headless") #=> Runs System in Headless or Browserless Mode, for Jenkins
    web_driver = webdriver.Chrome(driver_location, options=browser_options)
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
    #text_src = web_driver.page_source
    #text_to_find = re.search(r'This section of our web site is currently under construction', text_src)
    #assert (text_to_find in web_driver.text_src)

def tear_down(w_d, o_s):
    w_d
    o_s