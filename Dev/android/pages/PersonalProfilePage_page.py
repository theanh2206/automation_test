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
    #Click các icon trong trang hồ sơ cá nhân
    def click_my_services(self, index):
        locator = (By.XPATH, f'(//android.widget.ImageView[@resource-id="vms.com.vn.mymobifone:id/ivIcon"])[{index}]')
        self.click(locator)
    #Click button refesh
    def click_button_refesh(self):
        self.click(self.locators.BUTTON_REFESH)
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
    
    #Click button detail
    def click_button_detail(self):
        self.click(self.locators.BUTTON_DETAIL1)
    def click_by_text(self, text):
        try:
            xpath = f'//android.widget.TextView[contains(@text,"{text}")]'
        
            element = WebDriverWait(self.driver, 10).until(
                lambda d: d.find_element(AppiumBy.XPATH, xpath)
            )
            element.click()
        except Exception as e:
            raise Exception(f"Không tìm thấy element chứa text: {text}") from e
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
    def select_date(self, month, year):
        month_el = self.driver.find_element(
            AppiumBy.XPATH,
        '(//android.widget.EditText[@resource-id="android:id/numberpicker_input"])[1]'
        )

        year_el = self.driver.find_element(
            AppiumBy.XPATH,
        '(//android.widget.EditText[@resource-id="android:id/numberpicker_input"])[2]'
        )

        # ===== SCROLL MONTH =====
        for _ in range(20):
            current_text = month_el.text.lower()  # ví dụ: "tháng 3"
        
            if f"tháng {month}" in current_text:
                break

            # extract số tháng hiện tại
            current_month = int(current_text.replace("tháng", "").strip())

            # chọn hướng swipe
            if current_month > month:
                direction = "down"
            else:
                direction = "up"

            self.swipe_on_element(month_el, direction)

        # ===== SCROLL YEAR =====
        for _ in range(20):
            current_year = int(year_el.text)

            if current_year == year:
                break

            # chọn hướng swipe
            if current_year > year:
                direction = "down"
            else:
                direction = "up"

            self.swipe_on_element(year_el, direction)
    #Click button OK        
    def click_button_ok(self):
        self.click(self.locators.BUTTON_OK)
    #Chọn tháng/năm
    def click_select_date(self):
        self.click(self.locators.SELECT_DATE)
    #Click button Delete
    def click_button_delete(self):
        self.click(self.locators.BUTTON_DELETE)
    #CLick button back/up/ fillter
    def click_button_back(self):
        self.click(self.locators.BUTTON_BACK)
    def click_button_up(self):
        self.click(self.locators.BUTTON_UP)
    def click_button_fillter(self):
        self.click(self.locators.BUTTON_FILLTER)
    def click_icon_bin(self):
        self.click(self.locators.ICON_BIN)
    #Click button cập nhật thông tin
    def click_button_update(self):
        self.click(self.locators.BUTTON_UPDATE)
    #Click chọn tháng mong muốn
    def select_month(self, index):
        locator = (By.XPATH, f'//androidx.recyclerview.widget.RecyclerView[@resource-id="vms.com.vn.mymobifone:id/rvMonths"]/android.widget.LinearLayout[{index}]')
        self.click(locator)
    def click_my_mobifone(self):
        locator = (By.XPATH, f'//android.widget.TextView[@content-desc="My MobiFone"]')
        self.click(locator)
    def click_default(self):
        locator = (By.XPATH, f'//android.widget.Button[@resource-id="android:id/button1"]')
        self.click(locator)
    def add_phone(self):
        self.click(self.locators.ADD_PHONE)
    #Click giao dịch trong tháng
    def click_history_pakage(self, index):
        locator = (By.XPATH, f'(//androidx.appcompat.widget.LinearLayoutCompat[@resource-id="vms.com.vn.mymobifone:id/linearLayoutCompat"])[{index}]')
        self.click(locator)
    def click_button_close(self):
        self.click(self.locators.CLOSE)
    #Click button đổi ngôn ngữ
    def click_switch_language(self):
        self.click(self.locators.SWITCH_LANGUAGE)
    def click_switch_notification(self):
        self.click(self.locators.SWITCH_NOTIFICATION)
    def click_smart_otp(self):
        self.click(self.locators.SMART_OTP)
    def click_switch_smart_otp(self):
        self.click(self.locators.SWITCH_SMART_OTP)
    def click_button_accept(self):
        self.click(self.locators.BUTTON_ACCEPT)
    def click_switch_spam(self):
        self.click(self.locators.SWITCH_SPAM)
    def click_switch_block(self):
        self.click(self.locators.SWITCH_BLOCK)
    def input_smart_otp(self, keyword):
        self.click(self.locators.INPUT_SMART_OTP)
        self.send_keys(self.locators.INPUT_SMART_OTP, keyword)
        self.click(self.locators.CONFIRM_SMART_OTP)
        self.send_keys(self.locators.CONFIRM_SMART_OTP, keyword)
    #Click button Confirm
    def click_buttom_confirm(self):
        self.click(self.locators.GIFT_CONFIRM)
    #Back lại bước vừa xong 
    def press_back(self):
        return super().press_back()
    
    #         ===== VERIFY =====
    def wait_for_result(self, keyword):
        self.wait_for_text(keyword)

    def is_result_displayed(self, keyword):
        return self.is_text_displayed(keyword)