import time

from appium import webdriver
from appium.options.android import UiAutomator2Options

desired_caps = dict(
    deviceName='Android Emulator',
    platformName='Android',
    platformVersion='15',
    app='/Users/gregdelgado/Developer/scratchpad/appium/android/ApiDemos-debug.apk',
    automationName='UiAutomator2',
)

capabilities_options = UiAutomator2Options().load_capabilities(desired_caps)
driver = webdriver.Remote('http://127.0.0.1:4723', options=capabilities_options)

time.sleep(5)
driver.quit()