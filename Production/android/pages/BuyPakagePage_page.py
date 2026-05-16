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
    def click_button_by_resource_id(self, resource_id):
        try:
            xpath = f'//android.widget.Button[@resource-id="{resource_id}"]'
            element = WebDriverWait(self.driver, 10).until(
                lambda d: d.find_element(AppiumBy.XPATH, xpath)
        )
            element.click()
        except Exception as e:
            raise Exception(f"Không tìm thấy button với resource-id: {resource_id}") from e
    def click_text_by_resource_id(self, resource_id):
        try:
            xpath = f'//android.widget.TextView[@resource-id="{resource_id}"]'
            element = WebDriverWait(self.driver, 10).until(
                lambda d: d.find_element(AppiumBy.XPATH, xpath)
        )
            element.click()
        except Exception as e:
            raise Exception(f"Không tìm thấy text với resource-id: {resource_id}") from e
    def click_by_text(self, text, index=1):
        try:
            xpath = f'//android.widget.TextView[contains(@text,"{text}")][{index}]'
            element = WebDriverWait(self.driver, 10).until(
                lambda d: d.find_element(AppiumBy.XPATH, xpath)
            )
            element.click()
        except Exception as e:
            raise Exception(f"Không tìm thấy element chứa text: {text}") from e
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
    #Click icon tạo gói cước cá nhân
    def click_personal_flex(self):
        self.click(self.locators.PERSONAL_FLEX)
    def click_time_flex(self):
        self.click(self.locators.TIME_FLEX)
    def click_icon_cvqt(self):
        self.click(self.locators.ICON_CVQT)
    def click_button_create_pakage(self):
        self.click(self.locators.BUTTON_CREATE_PAKAGE)
    def click_payment_confirm(self):
        self.click(self.locators.PAYMENT_CONFIRM)
    def click_button_accept(self):
        self.click(self.locators.BUTTON_ACCEPT)
    def click_register_button2(self):
        self.click(self.locators.REGISTER_BUTTON2)
        
    # Chuyển vùng quốc tế
    #1. Click kiểm tra trước chuyến đi
    def click_check_trip(self):
        self.click(self.locators.CHECK_TRIP)
    #2. Search gói cước/ quốc gia
    def click_search_by_key(self, keyword):
        self.click(self.locators.SEARCH_BY_KEY)
        self.send_keys(self.locators.SEARCH_BY_KEY, keyword)
    def click_search_country(self):
        self.click(self.locators.SEARCH_COUNTRY)
    def send_key_country(self, keyword):
        self.send_keys(self.locators.SEARCH_COUNTRY1, keyword)
    #3. Click button áp dụng
    def click_button_apply(self):
        self.click(self.locators.BUTTON_APPLY)
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
    def click_popular_country(self, index):
        elements = WebDriverWait(self.driver, 10).until(
            lambda d: d.find_elements(
                AppiumBy.XPATH,
            '//androidx.recyclerview.widget.RecyclerView[@resource-id="vms.com.vn.mymobifone:id/rvCountryPackages"]//android.widget.LinearLayout'
        )
    )

        if index > len(elements):
            raise Exception(f"Chỉ có {len(elements)} item, không có item {index}")

        elements[index - 1].click()
    #6. Click gói cước tạo data roaming linh hoạt
    def click_pakage_roaming(self):
        self.click(self.locators.PAKAGE_ROAMING)
    #7. Click tạo gói cước data roaming 
    def click_create_pakage_roaming(self):
        self.click(self.locators.CREATE_PAKAGE_ROAMING)
    #Liên hệ tư vấn
    def click_contact_consulting(self):
        self.click(self.locators.BUTTON_CONTACT_CONSULTING)
    def send_phone_number(self, keyword):
        self.click(self.locators.PHONE_NUMBER)
        self.send_keys(self.locators.PHONE_NUMBER, keyword)
    def select_day_contact(self, index):
        self.click(self.locators.DAY_CONTACT)
        self.wait_for_result("Xác nhận")
        try:
            xpath = f'//androidx.recyclerview.widget.RecyclerView[@resource-id="vms.com.vn.mymobifone:id/rvDays"]/android.widget.RelativeLayout[{index}]'
        
            element = self.driver.find_element(AppiumBy.XPATH, xpath)
            element.click()
        except Exception as e:
            raise Exception(f"Không tìm thấy ngày tại vị trí: {index}") from e
        self.click(self.locators.BUTTON_SUBMIT)
    def select_time_contact(self):
        self.click(self.locators.TIME_CONTACT)
        self.click(self.locators.SELECT_TIME)
    def click_button_book(self):
        self.click(self.locators.BOOK)
    # Tặng/chia sẻ gói cước
    def gift_pakage(self, keyword):
        self.click(self.locators.GIFT)
        self.send_keys(self.locators.PHONE_RECIEVE, keyword)
        self.hide_keyboard()
        self.click(self.locators.GIFT_CONFIRM)
    def share_pakage(self):
        self.click(self.locators.ICON_SHARE)
        self.click(self.locators.BUTTON_SHARE)
    # Tiện ích của bạn
    def click_icon(self, index):
        locator = (By.XPATH, f'(//android.widget.ImageView[@resource-id="vms.com.vn.mymobifone:id/ivIcon"])[{index}]')
        self.click(locator)
    #CLick button chi tiết gói cước
    def click_detail_pakage(self):
        self.click(self.locators.DETAIL_D5)
    #CLick button hẹn roaming
    def click_schedule_roaming(self):
        self.click(self.locators.BUTTON_SCHEDULE_ROAMING)
    def click_button_submit(self):
        self.click(self.locators.BUTTON_SUBMIT)
    def et_time(self, keword):
        self.click(self.locators.ET_TIME)
        self.send_keys(self.locators.ET_TIME, keword)
    #Click button detail pakage
    def click_button_detail(self, index):
        locator = (By.XPATH, f'//android.widget.TextView[@resource-id="vms.com.vn.mymobifone:id/tvDetail"][{index}]')
        self.click(locator)
    def click_button_login(self):
        self.click(self.locators.BUTTON_LOGIN)
    # Click hướng dẫn sử dụng
    def click_guide_by_text(self, text):
        xpath = f'//android.widget.TextView[@resource-id="vms.com.vn.mymobifone:id/tvQuestion" and @text="{text}"]'
    
        element = WebDriverWait(self.driver, 10).until(
            lambda d: d.find_element(AppiumBy.XPATH, xpath)
            )
        element.click()
        
    def click_btn_cancel(self):
        self.click(self.locators.BTN_CANCEL) 
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
    #Back lại bước vừa xong 
    def press_back(self):
        return super().press_back()
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
    #--------------Hàm scroll ngang
    def scroll_horizontal_utils(self, direction="left", times=1):
        carousel = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((
            By.XPATH,
            '//androidx.recyclerview.widget.RecyclerView[@resource-id="vms.com.vn.mymobifone:id/rvUtils"]'
            ))
        )

        for _ in range(times):
            loc = carousel.location
            size = carousel.size

            self.driver.execute_script("mobile: swipeGesture", {
                "left": loc["x"],
                "top": loc["y"],
                "width": size["width"],
                "height": size["height"],
                "direction": direction,
                "percent": 0.8
            })
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
    #Swipe danh mục các nhóm gói
    def swipe_categories(self):
        element = self.driver.find_element(
            AppiumBy.ID,"vms.com.vn.mymobifone:id/rvListCategories")

        location = element.location
        size = element.size
        start_x = int(location['x'] + size['width'] * 0.9)
        end_x = int(location['x'] + size['width'] * 0.1)
        y = int(location['y'] + size['height'] / 2)

        self.driver.swipe(start_x, y, end_x, y, 500)
        
    #Click categories
    def click_category_by_index(self, index):
        try:
            xpath = f'(//android.widget.LinearLayout[@resource-id="vms.com.vn.mymobifone:id/lineRoot"])[{index}]'
        
            element = self.driver.find_element(AppiumBy.XPATH, xpath)
            element.click()
        except Exception as e:
            raise Exception(f"Không tìm thấy category tại vị trí: {index}") from e
    
    def click_button_by_resource_image(self, resource_id):
        try:
            xpath = f'//android.widget.ImageView[@resource-id="{resource_id}"]'
            element = WebDriverWait(self.driver, 10).until(
                lambda d: d.find_element(AppiumBy.XPATH, xpath)
        )
            element.click()
        except Exception as e:
            raise Exception(f"Không tìm thấy button với resource-id: {resource_id}") from e
    #Kiểm tra click chọn từng chu kỳ 
    def click_radio_button_all(self):
        self.click(self.locators.RADIO_BUTTON_ALL)
    def click_radio_button_days(self):
        self.click(self.locators.RADIO_BUTTON_DAYS)
    def click_radio_button_months(self):
        self.click(self.locators.RADIO_BUTTON_MONTHS)
    def click_sort_price(self):
        self.click(self.locators.SORT_PRICE)
    def click_sort_data(self):
        self.click(self.locators.SORT_DATA)
    #Màn tất cả gói cước
    #Click tất cả gói cước
    def click_view_all_pakage(self):
        self.click(self.locators.VIEW_ALL_PAKAGE)
    #Ẩn bàn phím
    def hide_keyboard(self):
        try:
            self.driver.hide_keyboard()
        except:
            try:
                self.driver.back()
            except:
                try:
                    self.driver.tap([(100, 100)])
                except:
                    pass
   
    #         ===== VERIFY =====
    def wait_for_result(self, keyword):
        self.wait_for_text(keyword)

    def is_result_displayed(self, keyword):
        return self.is_text_displayed(keyword)