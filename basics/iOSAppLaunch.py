import time

from appium import webdriver
from appium.options.ios import XCUITestOptions

desired_caps = dict(
    deviceName='iPhone 16',
    platformName='iOS',
    platformVersion='18.2',
    app='/Users/gregdelgado/Developer/scratchpad/appium/ios/GasTracker.app',
    automationName='XCUITest',
)

capabilities_options = XCUITestOptions().load_capabilities(desired_caps)
driver = webdriver.Remote('http://127.0.0.1:4723', options=capabilities_options)

time.sleep(5)
driver.quit()