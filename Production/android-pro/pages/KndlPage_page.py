from pages.BasePage_page import BasePage
from pages.LocatorPage_page import LocatorPage
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.appiumby import AppiumBy
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import time

class KndlPage(BasePage):
    locators = LocatorPage()
    #Click tab KNDL
    def click_icon_kndl(self, index):
        locator = (By.XPATH, f'//android.widget.LinearLayout[@resource-id="vms.com.vn.mymobifone:id/bottomBar"]/android.widget.LinearLayout/android.widget.FrameLayout[{index}]')
        self.click(locator)
    def click_list_deals(self, index):
        locator = (By.XPATH, f'(//android.widget.ImageView[@resource-id="vms.com.vn.mymobifone:id/ivThumb"])[{index}]')
        self.click(locator)
    #Click guide by text
    def click_by_text(self, text):
        try:
            xpath = f'//android.widget.TextView[contains(@text,"{text}")]'
        
            element = WebDriverWait(self.driver, 10).until(
                lambda d: d.find_element(AppiumBy.XPATH, xpath)
            )
            element.click()
        except Exception as e:
            raise Exception(f"Không tìm thấy element chứa text: {text}") from e
    def click_text_by_resource_id(self, resource_id):
        try:
            xpath = f'//android.widget.TextView[@resource-id="{resource_id}"]'
            element = WebDriverWait(self.driver, 10).until(
                lambda d: d.find_element(AppiumBy.XPATH, xpath)
        )
            element.click()
        except Exception as e:
            raise Exception(f"Không tìm thấy text với resource-id: {resource_id}") from e
    def click_button_by_resource_id(self, resource_id):
        try:
            xpath = f'//android.widget.Button[@resource-id="{resource_id}"]'
            element = WebDriverWait(self.driver, 10).until(
                lambda d: d.find_element(AppiumBy.XPATH, xpath)
        )
            element.click()
        except Exception as e:
            raise Exception(f"Không tìm thấy button với resource-id: {resource_id}") from e
    #----------Hàm nhập OTP-----------
    def input_otp(self, otp_code):
        otp_inputs = self.wait.until(
            EC.presence_of_all_elements_located(
                (AppiumBy.XPATH, '//android.widget.EditText[@text="_"]')
        )
    )

        otp_inputs[0].click()
        time.sleep(0.5)

        for digit in otp_code:
            self.driver.press_keycode(7 + int(digit))

        self.wait.until(
            EC.presence_of_element_located(
                (AppiumBy.XPATH, "/hierarchy/android.widget.FrameLayout")
        )
    )
    def click_button_login(self):
        self.click(self.locators.BUTTON_LOGIN)
    #Click thêm gói cước quy đổi
    def click_add_pakage(self):
        self.click(self.locators.ADD_PAKAGE)
    def click_exchange_point(self):
        self.click(self.locators.EXCHANGE_POINT)
    #Click button Confirm
    def click_buttom_confirm(self):
        self.click(self.locators.GIFT_CONFIRM)
    def click_button_exchange(self):
        self.click(self.locators.BUTTON_EXCHANGE)
    def click_buy_now(self):
        self.click(self.locators.BUY_NOW)
    def click_button_accept(self):
        self.click(self.locators.BUTTON_ACCEPT)
    def click_kndl_confirm(self):
        self.click(self.locators.KNDL_CONFIRM)
    def click_button_seemore(self):
        self.click(self.locators.BUTTON_SEE_MORE)
    def click_button_refesh(self):
        self.click(self.locators.BUTTON_REFESH)
    # Hàm scroll tới phần tử cụ thể
    def scroll_to_element(self, text, max_scroll=6):
        size = self.driver.get_window_size()

        for i in range(max_scroll):
            print(f"🔍 Lần {i+1}: tìm '{text}'")

            elements = self.driver.find_elements(
                AppiumBy.ANDROID_UIAUTOMATOR,
                f'new UiSelector().textContains("{text}")'
                )

            if elements:
                return elements[0]

           # scroll mỗi vòng
            self.driver.execute_script(
                "mobile: scrollGesture",
                {
                "left": int(size["width"] * 0.1),
                "top": int(size["height"] * 0.3),
                "width": int(size["width"] * 0.8),
                "height": int(size["height"] * 0.6),
                "direction": "down",
                "percent": 0.7,
                "speed": 500
                }
            )

            time.sleep(1)  # cho UI load

        raise Exception(f"❌ Không tìm thấy: {text}")
    
    #Swipe banner ngang
    def swipe_banner(self, times=1, duration=1200, delay=0.5):
        try:
            banner = self.driver.find_element(
            By.ID, "vms.com.vn.mymobifone:id/rlSliderBannerKNDL"
        )
        except NoSuchElementException:
            raise Exception("❌ Không tìm thấy banner để swipe")
        location = banner.location
        size = banner.size
    # 👉 Tối ưu khoảng cách swipe (gần full width)
        start_x = int(location['x'] + size['width'] * 0.95)
        end_x = int(location['x'] + size['width'] * 0.05)
        y = int(location['y'] + size['height'] / 2)
        for i in range(times):
            print(f"👉 Swipe lần {i+1}")
            self.driver.swipe(start_x, y, end_x, y, duration)
            time.sleep(delay)
    #Click banner
    def click_banner(self):
        self.click(self.locators.BANNER)
    def search_list_deal_kndl(self, keyword):
        self.click(self.locators.SEARCH_BOX1)
        self.send_keys(self.locators.SEARCH_BOX1, keyword)
    def input_email(self, keyword):
        self.click(self.locators.INPUT_MAIL)
        self.send_keys(self.locators.INPUT_MAIL, keyword)
    #Back lại bước vừa xong 
    def press_back(self):
        return super().press_back()
    #         ===== VERIFY =====
    def wait_for_result(self, keyword):
        self.wait_for_text(keyword)

    def is_result_displayed(self, keyword):
        return self.is_text_displayed(keyword)