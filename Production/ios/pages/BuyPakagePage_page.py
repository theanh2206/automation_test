from pages.BasePage_page import BasePage
from pages.LocatorPage_page import LocatorPage
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.appiumby import AppiumBy
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import time


class BuyPakagePage(BasePage):
    locators = LocatorPage()
    #Click tab Mua gói
    def click_buy_pakage(self):
        self.click(self.locators.BUY_PAKAGE)
    def click_by_text(self, text, index=1):
        xpath = f'(//XCUIElementTypeStaticText[@name="{text}"])[{index}]'
        element = self.driver.find_element(AppiumBy.XPATH, xpath)
        element.click()
    def click_button_by_text(self, text, index=1):
        xpath = f'(//XCUIElementTypeButton[@name="{text}"])[{index}]'
    
        element = self.wait.until(
            EC.element_to_be_clickable(
                (AppiumBy.XPATH, xpath)
            )
        )
        element.click()
    def click_by_image(self, text, index=1):
        xpath = f'(//XCUIElementTypeImage[@name="{text}"])[{index}]'
        element = self.driver.find_element(AppiumBy.XPATH, xpath)
        element.click()
    #Ẩn bàn phím
    def hide_keyboard1(self):
        size = self.driver.get_window_size()
        self.driver.tap([
            (int(size['width'] * 0.9), int(size['height'] * 0.5))
        ])
    #Search gói cước trên thanh tìm kiếm
    def search_package(self, keyword):
        self.click(self.locators.SEARCH_BOX)
        self.send_keys(self.locators.SEARCH_INPUT, keyword)
    def search_package1(self, keyword):
        self.click(self.locators.SEARCH_BOX1)
        self.send_keys(self.locators.SEARCH_BOX1, keyword)
    #Click vào menu
    def click_menu(self):
        self.click(self.locators.MENU)   
    #Click button đăng ký D5
    def click_register_button(self):
        self.click(self.locators.REGISTER_BUTTON)
    #Click icon tạo gói cước cá nhân
    def click_personal_flex(self):
        self.click(self.locators.PERSONAL_FLEX)
    def click_time_flex(self):
        self.click(self.locators.TIME_FLEX)
    def click_icon_cvqt(self):
        self.click(self.locators.ICON_CVQT)
    def click_button_accept(self):
        self.click(self.locators.BUTTON_ACCEPT)
    # Chuyển vùng quốc tế
    #1. Click kiểm tra trước chuyến đi
    def click_check_trip(self):
        self.click(self.locators.CHECK_TRIP)
    def click_search_country(self):
        self.click(self.locators.SEARCH_COUNTRY)
    def send_key_country(self, keyword):
        self.send_keys(self.locators.SEARCH_COUNTRY1, keyword)
    #4. Click tên quốc gia trong tìm kiếm quốc gia
    def click_country(self, keyword):
        for _ in range(5):
            elements = self.driver.find_elements(
            AppiumBy.ANDROID_UIAUTOMATOR,
            f'new UiSelector().textContains("{keyword}")'
        )
            if elements:
                elements[0].click()
            return
        # swipe lên
        self.driver.swipe(500, 1500, 500, 500, 800)
        raise Exception(f"Không tìm thấy country: {keyword}")
    #5. Click các quốc gia phổ biến
    def click_popular_country1(self, index):
        elements = WebDriverWait(self.driver, 10).until(
            lambda d: d.find_elements(
                AppiumBy.XPATH,
            '//androidx.recyclerview.widget.RecyclerView[@resource-id="vms.com.vn.mymobifone:id/rvCountryPackages"]//android.widget.LinearLayout'
        )
    )
        if index > len(elements):
            raise Exception(f"Chỉ có {len(elements)} item, không có item {index}")
        elements[index - 1].click()
    def click_popular_country(self, index):
        locator = (By.XPATH, f'//XCUIElementTypeCollectionView/XCUIElementTypeCell[{index}]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeButton')
        self.click(locator)
    # Tặng/chia sẻ gói cước
    def gift_pakage(self, keyword):
        self.click(self.locators.PHONE_RECIEVE)
        self.send_keys(self.locators.PHONE_RECIEVE, keyword)
    # Tiện ích của bạn
    def click_icon(self, index):
        locator = (By.XPATH, f'(//android.widget.ImageView[@resource-id="vms.com.vn.mymobifone:id/ivIcon"])[{index}]')
        self.click(locator)
    #----------Hàm nhập OTP-----------
    def input_otp(self, otp_code):
        otp_inputs = self.wait.until(
            EC.presence_of_all_elements_located(
                (AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeTextField')
        )
    )
        for i, digit in enumerate(otp_code):
            otp_inputs[i].send_keys(digit)
    #Click button back
    def click_button_back(self):
        self.click(self.locators.BUTTON_BACK)
    #Click close
    def click_close(self):
        self.click(self.locators.CLOSE)
    # Hàm scroll tới phần tử cụ thể
    def scroll_to_element(self, text, max_scroll=6):
        for _ in range(max_scroll):
            elements = self.driver.find_elements(
                AppiumBy.ACCESSIBILITY_ID, text
        )
            if elements:
                return elements[0]
            self.driver.execute_script("mobile: swipe", {"direction": "up"})
        raise Exception(f"Không tìm thấy {text}")
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
    #Swipe banner ngang
    def swipe_banner(self, times=1, duration=1200, delay=0.5):
        try:
            banner = self.driver.find_element(
            By.ID, "vms.com.vn.mymobifone:id/rlSliderBannerHome"
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
    #         ===== VERIFY =====
    def wait_for_result(self, keyword):
        self.wait_for_text(keyword)

    def is_result_displayed(self, keyword):
        return self.is_text_displayed(keyword)