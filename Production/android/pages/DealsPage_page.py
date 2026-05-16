from pages.BasePage_page import BasePage
from pages.LocatorPage_page import LocatorPage
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import time


class DealsPage(BasePage):
    locators = LocatorPage()
    #Click icon Ưu đãi
    def click_icon_deals(self, index):
        locator = (By.XPATH, f'//android.widget.LinearLayout[@resource-id="vms.com.vn.mymobifone:id/bottomBar"]/android.widget.LinearLayout/android.widget.FrameLayout[{index}]')
        self.click(locator)
    #Search gói cước trên thanh tìm kiếm
    def search_package(self, keyword):
        self.click(self.locators.SEARCH_DEALS)
        self.click(self.locators.SEARCH_BOX1)
        self.send_keys(self.locators.SEARCH_INPUT, keyword)
    def click_button_login(self):
        self.click(self.locators.BUTTON_LOGIN)
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
    #Back lại bước vừa xong 
    def press_back(self):
        return super().press_back()
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
    #Mẹo tích điểm
    def click_save_point1(self):
        self.click(self.locators.SAVE_POINT)
    def click_list_save_point(self, index):
        locator = (By.XPATH, f'//androidx.recyclerview.widget.RecyclerView[@resource-id="vms.com.vn.mymobifone:id/rcvTipsMyPoint"]/android.widget.RelativeLayout[{index}]/android.widget.FrameLayout/android.widget.LinearLayout')
        self.click(locator)
    #Lịch sử điểm 
    def click_point_history(self):
        self.click(self.locators.POINT_HISTORY)
    def click_list_point_history(self, index):
        locator = (By.XPATH, f'//androidx.recyclerview.widget.RecyclerView[@resource-id="vms.com.vn.mymobifone:id/rvListHistoryModel"]/android.widget.LinearLayout[{index}]')
        self.click(locator)
    def click_by_text(self, text):
        try:
            xpath = f'//android.widget.TextView[contains(@text,"{text}")]'
        
            element = WebDriverWait(self.driver, 10).until(
                lambda d: d.find_element(AppiumBy.XPATH, xpath)
            )
            element.click()
        except Exception as e:
            raise Exception(f"Không tìm thấy element chứa text: {text}") from e
    
    def click_close(self):
        self.click(self.locators.CLOSE)
    def click_button_close(self):
        self.click(self.locators.BUTTON_CLOSE)    
    def click_save_point(self, index):
        locator = (By.ID, f'vms.com.vn.mymobifone:id/lnSavePoint_{index}')
        self.click(locator)
    def click_sell_point(self, index):
        locator = (By.ID, f'vms.com.vn.mymobifone:id/lnSellPoint_{index}')
        self.click(locator)
    #Lịch sử đơn hàng
    def click_cart_history(self):
        self.click(self.locators.CART_HISTORY)
    
    #Click button Xem tất cả
    def click_button_see_all(self):
        self.click(self.locators.BUTTON_SEE_ALL)
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
    #CLick Icon trong Ưu đãi MyPoint
    def click_icon_mypoint_deals(self, index):
        locator = (By.XPATH, f'(//android.widget.ImageView[@resource-id="vms.com.vn.mymobifone:id/ivAvatar"])[{index}]')
        self.click(locator)
    def click_button_exchange(self):
        self.click(self.locators.BUTTON_EXCHANGE)
    #Ưu đãi tích điểm
    def click_reward_point(self, index):
        locator = (By.XPATH, f'(//android.widget.ImageView[@resource-id="vms.com.vn.mymobifone:id/ivIcon"])[{index}]')
        self.click(locator)
    #CLick button Tất cả - Ưu đãi tích điểm
    def click_deals_list_all(self):
        self.click(self.locators.DEALS_LIST_ALL)
    #Click button Tất cả - Ưu đãi khác
    def click_deals_list_all_other(self):
        self.click(self.locators.DEALS_LIST_ALL_OTHER)
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
        
        
        
    #         ===== VERIFY =====
    def wait_for_result(self, keyword):
        self.wait_for_text(keyword)

    def is_result_displayed(self, keyword):
        return self.is_text_displayed(keyword)