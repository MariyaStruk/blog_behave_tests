#pip install selenium-requests behave_driver
import behave_webdriver

def before_all(context):
    context.behave_driver = behave_webdriver.Firefox()

def after_all(context):
    # cleanup after tests run
    context.behave_driver.quit()