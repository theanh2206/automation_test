import time
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# ========= CONFIG =========
DEVICE_UDID = "R5CX34ETEDM"
APP_PACKAGE = "vms.com.vn.mymobifone"
PHONE_NUMBER = "0762203039"
OTP_CODE = "888888"
APPIUM_URL = "http://127.0.0.1:4723/wd/hub"

# ========= DRIVER SETUP =========
options = UiAutomator2Options()
options.platform_name = "Android"
options.device_name = DEVICE_UDID
options.udid = DEVICE_UDID

options.app_package = "vms.com.vn.mymobifone"
options.app_activity = "vms.com.vn.mymobi.activities.SplashScreenActivity"

# Hàm scroll
def scroll_and_find_by_text(driver, text, max_scroll=6):
    for _ in range(max_scroll):
        elements = driver.find_elements(
            AppiumBy.ANDROID_UIAUTOMATOR,
            f'new UiSelector().textContains("{text}")'
        )
        if elements:
            return elements[0]

        driver.execute_script(
            "mobile: scrollGesture",
            {
                "left": 100,
                "top": 300,
                "width": 800,
                "height": 1200,
                "direction": "down",
                "percent": 0.7
            }
        )

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
    # 1️⃣ Click button Menu 
    wait.until(
        EC.element_to_be_clickable(
            (AppiumBy.ID, "vms.com.vn.mymobifone:id/ivMenu")
        )
    ).click()
    # 2️⃣ Scroll Menu & click button Đăng xuất
    logout_btn = driver.find_element(
    AppiumBy.ANDROID_UIAUTOMATOR,
    'new UiScrollable(new UiSelector().scrollable(true))'
    '.scrollIntoView(new UiSelector().resourceId("vms.com.vn.mymobifone:id/rlLogout"))'
)
    logout_btn.click()

    # 3️⃣ Click button Xác nhận
    wait.until(
        EC.element_to_be_clickable(
            (AppiumBy.ID, "vms.com.vn.mymobifone:id/btConfirm")
        )
    ).click()
    
    home_element = wait.until(
    EC.presence_of_element_located(
        (AppiumBy.XPATH, "/hierarchy/android.widget.FrameLayout")
    )
)
    print("✅ LOGOUT TEST PASSED")

except Exception as e:
    print("❌ LOGOUT TEST FAILED")
    print(e)

finally:
    time.sleep(10)
    driver.quit()
