import time
import pytest
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# ========= CONFIG =========
DEVICE_UDID = "R83X20ACPQV"
APP_PACKAGE = "vms.com.vn.mymobifone"
PHONE_NUMBER = "0762196780"
OTP_CODE = "0000"
APPIUM_URL = "http://127.0.0.1:4723/wd/hub"
TEXT = "D5"

# ========= DRIVER SETUP =========
options = UiAutomator2Options()
options.platform_name = "Android"
options.device_name = DEVICE_UDID
options.udid = DEVICE_UDID

options.app_package = "vms.com.vn.mymobifone"
options.app_activity = "vms.com.vn.mymobi.activities.SplashScreenActivity"

# ⭐ CỰC KỲ QUAN TRỌNG
options.no_reset = True
options.force_app_launch = False
options.dont_stop_app_on_reset = True

options.new_command_timeout = 300

driver = webdriver.Remote(
    command_executor="http://127.0.0.1:4723/wd/hub",
    options=options
)

print("✅ CONNECTED SUCCESSFULLY")

wait = WebDriverWait(driver, 20)

# ========= TEST STEPS =========

try:
    # 1️⃣ Click button Đăng nhập (màn 1)
        wait.until(
        EC.element_to_be_clickable(
            (AppiumBy.ID, "vms.com.vn.mymobifone:id/btLogin")
        )
    ).click()

    # 2️⃣ Nhập số điện thoại
        phone_input = wait.until(
        EC.presence_of_element_located(
            (AppiumBy.ID, "vms.com.vn.mymobifone:id/etPhoneNumber")
        )
    )
        phone_input.clear()
        phone_input.send_keys(PHONE_NUMBER)

    # 3️⃣ Click button Đăng nhập (màn 2)
        wait.until(
        EC.element_to_be_clickable(
            (AppiumBy.ID, "vms.com.vn.mymobifone:id/tvLogin")
        )
        ).click()

    # Chờ OTP screen load
        time.sleep(5)

    # Nhập OTP fix cứng

        otp_inputs = wait.until(
        EC.presence_of_all_elements_located(
        (AppiumBy.XPATH, '//android.widget.EditText[@text="_"]')
        )
        )
        otp_inputs[0].click()
        time.sleep(0.5)

        for digit in OTP_CODE:
            driver.press_keycode(7 + int(digit))
     
     
        wait.until(
            EC.presence_of_element_located(
            (AppiumBy.XPATH, "/hierarchy/android.widget.FrameLayout")
                )
            )
        print("✅ LOGIN OTP TEST PASSED")

except Exception as e:
        print("❌ LOGIN OTP TEST FAILED")
        print(e)
        raise

finally:
        time.sleep(2)
