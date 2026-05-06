from pages.BasePage_page import BasePage
from pages.LocatorPage_page import LocatorPage
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.appiumby import AppiumBy
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import time

class PersonalProfile(BasePage):
    locators = LocatorPage()
    #Click avata
    def click_avata(self):
        self.click(self.locators.AVATA)  
    
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
    #Hàm swipe
    def swipe_on_element(self, element, direction="up"):
        location = element.location
        size = element.size
        center_x = location['x'] + size['width'] // 2
        start_y = location['y'] + int(size['height'] * 0.9)
        end_y = location['y'] + int(size['height'] * 0.1)
        if direction == "up":
            self.driver.swipe(center_x, start_y, center_x, end_y, 300)
        else:
            self.driver.swipe(center_x, end_y, center_x, start_y, 300)
    #Hàm chọn tháng/năm
    def select_date(self, day, month, year):
        wheels = self.driver.find_elements(
            AppiumBy.IOS_CLASS_CHAIN,
            "**/XCUIElementTypePickerWheel"
        )
        day_wheel = wheels[0]
        month_wheel = wheels[1]
        year_wheel = wheels[2]
        # Day
        self.scroll_picker_wheel(day_wheel, str(day))
        # Month (format chuẩn iOS của bạn)
        self.scroll_picker_wheel(month_wheel, f"tháng {month}")
        # Year
        self.scroll_picker_wheel(year_wheel, str(year))
    #CLick button back/up/ fillter
    def click_button_back(self):
        self.click(self.locators.BUTTON_BACK)
    #Click chọn tháng mong muốn
    def select_month(self, index):
        locator = (By.XPATH, f'//androidx.recyclerview.widget.RecyclerView[@resource-id="vms.com.vn.mymobifone:id/rvMonths"]/android.widget.LinearLayout[{index}]')
        self.click(locator)
    #Back lại bước vừa xong 
    def press_back(self):
        return super().press_back()
    #Click bật tắt thông báo
    def click_on_switch_notification(self):
        self.click(self.locators.ON_SWITCH_NOTIFICATION)
    def click_off_switch_notification(self):
        self.click(self.locators.OFF_SWITCH_NOTIFICATION)
    def click_switch_smart_otp(self):
        self.click(self.locators.SWITCH_SMART_OTP)
    def click_on_switch_spam(self):
        self.click(self.locators.ON_SWITCH_SPAM)
    def click_on_switch_block(self):
        self.click(self.locators.ON_SWITCH_BLOCK)
    def click_off_switch_spam(self):
        self.click(self.locators.OFF_SWITCH_SPAM)
    def click_off_switch_block(self):
        self.click(self.locators.OFF_SWITCH_BLOCK)
    def input_smart_otp(self, keyword):
        self.click(self.locators.INPUT_SMART_OTP)
        self.send_keys(self.locators.INPUT_SMART_OTP, keyword)
        self.click(self.locators.CONFIRM_SMART_OTP)
        self.send_keys(self.locators.CONFIRM_SMART_OTP, keyword)
    #         ===== VERIFY =====
    def wait_for_result(self, keyword):
        self.wait_for_text(keyword)
    def is_result_displayed(self, keyword):
        return self.is_text_displayed(keyword)