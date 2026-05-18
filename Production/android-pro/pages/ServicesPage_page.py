from pages.BasePage_page import BasePage
from pages.LocatorPage_page import LocatorPage
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.appiumby import AppiumBy
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import time

class ServicesPage(BasePage):
    locators = LocatorPage()
    #Click tab dịch vụ
    def click_icon_services(self, index):
        locator = (By.XPATH, f'//android.widget.LinearLayout[@resource-id="vms.com.vn.mymobifone:id/bottomBar"]/android.widget.LinearLayout/android.widget.FrameLayout[{index}]')
        self.click(locator)
    def click_button_login(self):
        self.click(self.locators.BUTTON_LOGIN)
    #Search gói cước trên thanh tìm kiếm
    def search_package(self, keyword):
        self.click(self.locators.SEARCH_BOX)
        self.send_keys(self.locators.SEARCH_INPUT, keyword)
    def search_package1(self, keyword):
        self.click(self.locators.SEARCH_BOX1)
        self.send_keys(self.locators.SEARCH_INPUT, keyword)
    #Click thẻ gói cước D5
    def click_card_D5(self):
        self.click(self.locators.DETAIL_D5)
    #Click vào menu
    def click_menu(self):
        self.click(self.locators.MENU)   
    #Click button đăng ký D5
    def click_register_d5(self):
        self.click(self.locators.REGISTER_BUTTON)
    #Click button Huỷ đăng ký
    def click_button_cancel(self):
        self.click(self.locators.BUTTON_CANCEL)
    #Click button continute
    def click_button_continute(self):
        self.click(self.locators.BUTTON_CONTINUTE)
    def click_button_continute1(self):
        self.click(self.locators.BUTTON_CONTINUTE1)
    #Swipe banner ngang
    def swipe_banner(self, times=1, duration=1200, delay=0.5):
        try:
            banner = self.driver.find_element(
            By.ID, "vms.com.vn.mymobifone:id/rlSliderBannerService"
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
    #--Hàm scroll dọc
    def scroll_to_element1(self, text):
        return self.driver.find_element(
        AppiumBy.ANDROID_UIAUTOMATOR,
        f'new UiScrollable(new UiSelector().scrollable(true))'
        f'.scrollIntoView(new UiSelector().textContains("{text}"))'
    )
    #Click banner
    def click_banner(self):
        self.click(self.locators.BANNER)
    #Back lại bước vừa xong 
    def press_back(self):
        return super().press_back()
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
    #Swipe dịch vụ nổi bật
    def swipe_services(self, times=1, duration=1200, delay=0.5):
        try:
            banner = self.driver.find_element(
            By.ID, "vms.com.vn.mymobifone:id/rvUtils"
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
    #Click dịch vụ nổi bật
    def click_services_outstanding(self, index):
        locator = (By.XPATH, f'(//android.widget.ImageView[@resource-id="vms.com.vn.mymobifone:id/ivAvatarContact"])[{index}]')
        self.click(locator)
    #Click dịch vụ trong danh sách dịch vụ
    def click_services(self, index):
        locator = (By.XPATH, f'(//android.widget.ImageView[@resource-id="vms.com.vn.mymobifone:id/ivIcon"])[{index}]')
        self.click(locator)
    
    #CLick button đăng ký dịch vụ
    def click_button_register_services(self):
        self.click(self.locators.MOBIGAMES_REGISTER1)
    def click_by_text(self, text, index=1):
        try:
            xpath = f'(//android.widget.TextView[contains(@text,"{text}")])[{index}]'
        
            element = WebDriverWait(self.driver, 10).until(
                lambda d: d.find_element(AppiumBy.XPATH, xpath)
            )
            element.click()
        except Exception as e:
            raise Exception(f"Không tìm thấy element chứa text: {text}") from e








    #         ===== VERIFY =====
    def wait_for_result(self, keyword):
        self.wait_for_text(keyword)

    def is_result_displayed(self, keyword):
        return self.is_text_displayed(keyword)