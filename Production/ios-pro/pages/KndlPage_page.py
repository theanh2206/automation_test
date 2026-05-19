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
    def click_icon_kndl(self):
        locator = (By.XPATH, f'//XCUIElementTypeButton[@name="KNDL"]')
        self.click(locator)
    #Click guide by text
    def click_by_text(self, text, index=1):
        xpath = f'//XCUIElementTypeStaticText[@name="{text}"][{index}]'
        element = self.driver.find_element(AppiumBy.XPATH, xpath)
        element.click()
    def click_by_text1(self, text):
        el = WebDriverWait(self.driver, 10).until(
            lambda d: d.find_element(
            "-ios predicate string",
                f"name == '{text}'"
            )
        )
        el.click()
    def click_button_by_text(self, text, index=1, times = 1):
        xpath = f'(//XCUIElementTypeButton[@name="{text}"])[{index}]'
        element = self.wait.until(
            EC.element_to_be_clickable(
                (AppiumBy.XPATH, xpath)
            )
        )
        for i in range(times):
            print(f"👉 Click lần {i+1}")
            element.click()
    def click_by_image(self, text, index=1):
        xpath = f'(//XCUIElementTypeImage[@name="{text}"])[{index}]'
        element = self.driver.find_element(AppiumBy.XPATH, xpath)
        element.click()
    #----------Hàm nhập OTP-----------
    def input_otp(self, otp):
        for i, digit in enumerate(otp):
            for _ in range(3):
                try:
                    self.driver.find_elements(
                        "-ios class chain",
                        "**/XCUIElementTypeTextField"
                    )[i].send_keys(digit)
                    break
                except:
                    time.sleep(0.5)
    #--Hàm scroll dọc
    def scroll_to_element2(self, text, max_scroll=6):
        for i in range(max_scroll):
            print(f"🔍 Lần {i+1}: tìm '{text}'")
            elements = self.driver.find_elements(
                AppiumBy.IOS_PREDICATE,
                f'name CONTAINS[c] "{text}" OR label CONTAINS[c] "{text}"'
            )
            if elements:
                element = elements[0]
                if element.is_displayed():
                    print("✅ Đã hiển thị trên màn hình")
                    return element
                else:
                    print("⚠️ Tìm thấy nhưng chưa visible → scroll tiếp")
            print("👉 Swipe...")
            self.driver.execute_script("mobile: swipe", {"direction": "up"})
            time.sleep(1)
        raise Exception(f"❌ Không tìm thấy: {text}")
    def click_button_accept(self):
        self.click(self.locators.BUTTON_ACCEPT)
    #Swipe banner ngang
    def swipe_banner(self, times=1, duration=1200, delay=0.5):
        try:
            banner = self.driver.find_element(
            "-ios class chain",
            "**/XCUIElementTypeImage"
        )
        except NoSuchElementException:
            raise Exception("❌ Không tìm thấy banner")
        location = banner.location
        size = banner.size
        start_x = int(location['x'] + size['width'] * 0.9)
        end_x = int(location['x'] + size['width'] * 0.1)
        y = int(location['y'] + size['height'] / 2)
        for i in range(times):
            print(f"👉 Swipe lần {i+1}")
            self.driver.execute_script("mobile: dragFromToForDuration", {
                "duration": 0.2,
                "fromX": start_x,
                "fromY": y,
                "toX": end_x,
                "toY": y
            })
            time.sleep(delay)
    #Click banner
    def click_banner(self):
        self.click(self.locators.BANNER)
    def click_banner_kndl(self):
        self.click(self.locators.BANNER_KNDL)
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