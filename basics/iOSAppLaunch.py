import time

from appium import webdriver
from appium.options.ios import XCUITestOptions
from appium.webdriver.common.appiumby import AppiumBy

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
driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value='station_name').send_keys('Shell Sucat')
driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value='Return').click()
driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value='save_entry').click()
driver.find_element(by=AppiumBy.XPATH, value='//XCUIElementTypeButton[@name="OK"]').click()
driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value='history').click()

time.sleep(5)
driver.quit()