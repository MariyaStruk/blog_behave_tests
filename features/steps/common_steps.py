import pdb
from behave import *
from behave_webdriver.steps import *
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import time



#from selenium.webdriver.support.ui import WebDriverWait


#--no-capture
#pdb.set_trace()
#~/.local/lib/python2.7/site-packages/behave_webdriver/steps/expectations.py

@when ('I go to "{url}"')
def step(context, url):
    context.behave_driver.get(url)

@then ('I click on the link "{name}"')
def step(context, name):
   context.behave_driver.find_element_by_link_text(name).click()

@then ('I fill "{text}" in the field with the label "{name}"')
def step(context, text, name):
   xpath = "//label[text() = '{}']".format(name)
   label = context.behave_driver.find_element_by_xpath(xpath)
   label_for = label.get_attribute("for")
   input = context.behave_driver.find_element_by_id(label_for)
   input.send_keys(text)

@when ('I press the button "{name}"')
def step(context, name):
   xpath = "//input[@type='submit' and @value='{}']".format(name)
   context.behave_driver.find_element_by_xpath(xpath).click()

@then ('the page has "{text}"')
def step(context, text):
   assert (text in context.behave_driver.page_source) 

@then ('I wait for "{number:d}"')
def step(context, number):
   time.sleep(number)

@then ('the page does not have "{text}"')
def step(context, text):
   assert (text not in context.behave_driver.page_source)

@then ('I click on the last link with the text "{name}"')
def step(context, name):
   xpath = "(//a[text() = '{}'])[last()]".format(name)
   context.behave_driver.find_element_by_xpath(xpath).click()

@then ('I accept alert')
def step(context):
   alert = context.behave_driver.switch_to.alert
   alert.accept()

@then ('stop')
def step(context):
   pdb.set_trace()






   





@when('I press button "{name}"')
def step(context, name):
   xpath = "//input[@type='submit' and @value='{}']".format(name)
   context.behave_driver.find_element_by_xpath(xpath).click()
