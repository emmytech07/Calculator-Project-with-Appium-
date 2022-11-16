from appium import webdriver
from appium.webdriver.appium_service import AppiumService
from appium.webdriver.common.appiumby import By, AppiumBy
import time as sl
import pytest

def test_cal():
    desired_cap = {}

    desired_cap['platformName'] = 'Android'
    desired_cap['deviceName'] = 'Android'
    desired_cap['appPackage'] = 'com.transsion.calculator'
    desired_cap['appActivity'] = '.Calculator'

    driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_cap)
    driver.implicitly_wait(5)

    el2 = driver.find_element(by=AppiumBy.ID, value="com.transsion.calculator:id/digit_8")
    el2.click()
    el3 = driver.find_element(by=AppiumBy.ID, value="com.transsion.calculator:id/digit_1")
    el3.click()

    el6 = driver.find_element(by=AppiumBy.ID, value="com.transsion.calculator:id/op_mul")
    el6.click()
    el7 = driver.find_element(by=AppiumBy.ID, value="com.transsion.calculator:id/digit_6")
    el7.click()
    el8 = driver.find_element(by=AppiumBy.ID, value="com.transsion.calculator:id/eq_front")
    el8.click()

    result = driver.find_element(by=AppiumBy.ID, value="com.transsion.calculator:id/result").text

    print("The value is", result)
    assert int(result) == 486


    print("Successful")
    sl.sleep(10)
    driver.quit()

test_cal()