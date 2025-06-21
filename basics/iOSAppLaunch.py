import time

from appium import webdriver
from appium.options.ios import XCUITestOptions
from appium.webdriver.common.appiumby import AppiumBy

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions import action_builder
from selenium.webdriver.common.actions.pointer_input import PointerInput
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder

desired_caps = dict(
    deviceName='iPhone 16',
    platformName='iOS',
    platformVersion='18.2',
    app='/Users/gregdelgado/Developer/scratchpad/appium/ios/Gas Tracker.app',
    automationName='XCUITest',
)

capabilities_options = XCUITestOptions().load_capabilities(desired_caps)
driver = webdriver.Remote('http://127.0.0.1:4723', options=capabilities_options)

driver.find_element(by=AppiumBy.XPATH, value='//XCUIElementTypeTextField[@value="ENTER LICENSE PLATE"]').send_keys('ABC123')
driver.find_element(by=AppiumBy.XPATH, value='//XCUIElementTypeButton[@name="Diesel"]').click()
driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value='price_per_liter').send_keys('45.78')
driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value='number_of_liters').send_keys('20')
driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value='odometer').send_keys('123456')

screen_size = driver.get_window_size()
start_x = int(screen_size['width'] * 0.5)
start_y = int(screen_size['height'] * 0.8)
end_y = int(screen_size['height'] * 0.2)

actions = ActionChains(driver)
pointer = PointerInput(interaction.POINTER_TOUCH, 'finger')
action_builder = ActionBuilder(driver, mouse=pointer)

action_builder.pointer_action.move_to_location(x=start_x, y=start_y)
action_builder.pointer_action.pointer_down()
action_builder.pointer_action.move_to_location(x=start_x, y=end_y)
action_builder.pointer_action.pointer_up()

actions.w3c_actions = action_builder

actions.perform()

time.sleep(5)

driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value='station_name').send_keys('Shell Sucat')
driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value='Return').click()
driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value='save_entry').click()
driver.find_element(by=AppiumBy.XPATH, value='//XCUIElementTypeButton[@name="OK"]').click()
driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value='history').click()

time.sleep(5)
driver.quit()