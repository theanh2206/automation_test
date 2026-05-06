from appium.webdriver.common.appiumby import AppiumBy
from pages.BasePage_page import BasePage
from pages.LocatorPage_page import LocatorPage
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time


class HomePage(BasePage):
    locators = LocatorPage()
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
    # Hàm tìm kiếm gói cước
    def search_package(self, keyword):
        self.click(self.locators.SEARCH_BOX)
        self.send_keys(self.locators.SEARCH_INPUT, keyword)
    # Hàm click mua gói
    def click_recharge(self):
        self.click(self.locators.RECHARGE)
    #Click butto tất cả tiện ích
    def click_view_all_utils(self):
        self.click(self.locators.VIEW_ALL_UTILS)
    #Click Mobigame
    #----Register
    def click_mobigames_detail(self):
        self.click(self.locators.MOBIGAMES_DETAIL)
    def click_mobigames_register1(self):
        self.click(self.locators.MOBIGAMES_REGISTER1)
    def click_mobigames_register2(self):
        self.click(self.locators.MOBIGAMES_REGISTER2)
    #----Unregister
    def click_mobigames_unregister(self):
        self.click(self.locators.MOBIGAME_UNREGISTER)
    
    #Click button Back
    def click_button_back(self):
        self.click(self.locators.BUTTON_BACK)
    #Click button Xem tất cả
    def click_button_see_all(self):
        self.click(self.locators.BUTTON_SEE_ALL)
    #Click icon avata
    def click_avata(self):
        self.click(self.locators.AVATA)    
    #Click icon Thông báo
    def click_notification(self):
        self.click(self.locators.NOTIFICATION)
    #Click banner
    def click_banner(self):
        self.click(self.locators.BANNER)
    #Click vào menu
    def click_menu(self):
        self.click(self.locators.MENU)    
    #Click thông tin sử dung   
    def click_infomation(self):
        self.click(self.locators.INFORMATION)
    #Click thông tin thuê bao    
    def click_infor_subcriber(self): 
        self.click(self.locators.INFOR_SUBCRIBER)
    #Click Tra cứu thông tin cước
    def click_infor_lookup(self):
        self.click(self.locators.INFOR_LOOKUP)
    #CLick icon Lịch sử nạp tiền
    def click_deposite_history(self):
        self.click(self.locators.DEPOSITE_HISTORY)
    #CLick icon lịch sử gói cước
    def click_subcriber_history(self):
        self.click(self.locators.SUBCRIBER_HISTORY)
    #Click button Mua thêm trong thông tin sử dụng
    def click_button_buy_pakage(self):
        self.click(self.locators.BUTTON_BUY_PAKAGE)
    #Click button Đăng ký thẻ KNDL
    def click_button_register_KNDL(self):
        self.click(self.locators.BUTTON_REGISTER_KNDL)
    #Click card KNDL (SĐT đã đăng ký KNDL)
    def click_card_kndl(self):
        self.click(self.locators.KNDL)
    #Click thẻ gói cước D5
    def click_card_D5(self):
        self.click(self.locators.DETAIL_D5)
    #Click button đăng ký D5
    def click_register_d5(self):
        self.click(self.locators.REGISTER_BUTTON)
    #Click button Huỷ đăng ký
    def click_button_cancel(self):
        self.click(self.locators.BUTTON_CANCEL)
    #Click button continute
    def click_button_continute(self):
        self.click(self.locators.BUTTON_CONTINUTE)
    #-----Gói cước của bạn-------
    def click_button_extend(self):
        self.click(self.locators.BUTTON_EXTEND)
    def click_button_cancel_extend(self):
        self.click(self.locators.BUTTON_CANCEL_EXTEND)
    def click_detail_my_pakage(self):
        self.click(self.locators.DETAIL_MY_PAKAGE)    
    def click_button_confirm_cancel_extend(self):
        self.click(self.locators.BUTTON_CONFIRM_CANCEL_EXTEND)
    def click_button_confirm_extend(self):
        self.click(self.locators.BUTTON_CONFIRM_EXTEND)
    #---Hẹn roaming ------
    def click_button_reschedule(self):
        self.click(self.locators.BUTTON_RESHEDULE)
    def click_button_cancel_schedule(self):
        self.click(self.locators.BUTTON_CANCEL_SCHEDULE)
    def click_button_submit(self):
        self.click(self.locators.BUTTON_SUBMIT)
    def et_time(self, keword):
        self.click(self.locators.ET_TIME)
        self.send_keys(self.locators.ET_TIME, keword)
    #Thông tin sử dụng/Tiện ích nổi bật
    def click_kndl1(self):
        self.click(self.locators.KNDL1)
    def click_cvqt(self):
        self.click(self.locators.CVQT)    
    def click_vtc83(self):
        self.click(self.locators.VTC83)
    def click_khs(self):
        self.click(self.locators.KHS)
    def click_button_back_left(self):
        self.click(self.locators.BUTTON_BACK_LEFT)
        
    # Tiện ích của bạn
    def click_icon(self, index):
        locator = (By.XPATH, f'(//android.widget.ImageView[@resource-id="vms.com.vn.mymobifone:id/ivIcon"])[{index}]')
        self.click(locator)
    def click_btn_cancel(self):
        self.click(self.locators.BTN_CANCEL)
    #Click dịch vụ nổi bật
    def click_avata_contact(self, index):
        locator = (By.XPATH, f'(//android.widget.ImageView[@resource-id="vms.com.vn.mymobifone:id/ivAvatarContact"])[{index}]')
        self.click(locator)
    def click_button_detail(self, index):
        locator = (By.XPATH, f'//android.widget.TextView[@resource-id="vms.com.vn.mymobifone:id/tvDetail"][{index}]')
        self.click(locator)
    def click_by_text(self, text, index=1):
        try:
            xpath = f'//android.widget.TextView[contains(@text,"{text}")][{index}]'
            element = WebDriverWait(self.driver, 10).until(
                lambda d: d.find_element(AppiumBy.XPATH, xpath)
            )
            element.click()
        except Exception as e:
            raise Exception(f"Không tìm thấy element chứa text: {text}") from e
    #Click by button     
    def click_button_by_resource_id(self, resource_id):
        try:
            xpath = f'//android.widget.Button[@resource-id="{resource_id}"]'
            element = WebDriverWait(self.driver, 10).until(
                lambda d: d.find_element(AppiumBy.XPATH, xpath)
        )
            element.click()
        except Exception as e:
            raise Exception(f"Không tìm thấy button với resource-id: {resource_id}") from e
    #Click by image   
    def click_image_by_resource_id(self, resource_id):
        try:
            xpath = f'//android.widget.ImageView[@resource-id="{resource_id}"]'
            element = WebDriverWait(self.driver, 10).until(
                lambda d: d.find_element(AppiumBy.XPATH, xpath)
        )
            element.click()
        except Exception as e:
            raise Exception(f"Không tìm thấy button với resource-id: {resource_id}") from e
    #Click by text resource
    def click_textview_by_resource_id(self, resource_id):
        try:
            xpath = f'//android.widget.TextView[@resource-id="{resource_id}"]'
            element = WebDriverWait(self.driver, 10).until(
                lambda d: d.find_element(AppiumBy.XPATH, xpath)
        )
            element.click()
        except Exception as e:
            raise Exception(f"Không tìm thấy button với resource-id: {resource_id}") from e
    # Đổi số điện thoại con
    def click_change_number(self):
        self.click(self.locators.CHANGE_NUMBER)
    def click_new_number(self):
        self.click(self.locators.NEW_NUMBER)
    def add_phone(self, keyword):
        self.click(self.locators.ADD_PHONE)
        self.send_keys(self.locators.INPUT_PHONE, keyword)
    def click_button_accept(self):
        self.click(self.locators.BUTTON_ACCEPT)
    def click_button_login(self):
        self.click(self.locators.BUTTON_LOGIN)
    #Click button đổi ngôn ngữ
    def click_switch_language(self):
        self.click(self.locators.SWITCH_LANGUAGE)
    #Close menu
    def close_menu(self):
        self.tap_outside()
    def press_back(self):
        return super().press_back()
    #Check popup Huỷ gói cước thành công
    def is_check_popup_unregister(self, timeout=10):
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(
                (AppiumBy.ID, "vms.com.vn.mymobifone:id/tvMsg")
            )
        )
            return True
        except:
            return False

#         ===== VERIFY =====
    def wait_for_result(self, keyword):
        self.wait_for_text(keyword)

    def is_result_displayed(self, keyword):
        return self.is_text_displayed(keyword)