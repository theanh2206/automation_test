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
    #CLick button Tất cả - Ưu đãi tích điểm
    def click_deals_list_all(self):
        self.click(self.locators.DEALS_LIST_ALL)
    #Click button Tất cả - Ưu đãi khác
    def click_deals_list_all_other(self):
        self.click(self.locators.DEALS_LIST_ALL_OTHER)
    #Search gói cước trên thanh tìm kiếm
    def search_package(self, keyword):
        self.click(self.locators.SEARCH_DEALS)
        self.send_keys(self.locators.SEARCH_INPUT, keyword)
    #Click vào menu
    def click_menu(self):
        self.click(self.locators.MENU)   
    #Click button đăng ký D5
    def click_register_d5(self):
        self.click(self.locators.REGISTER_BUTTON)
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
    def click_save_point(self):
        self.click(self.locators.SAVE_POINT)
    def click_list_save_point(self, index):
        locator = (By.XPATH, f'//XCUIElementTypeTable/XCUIElementTypeCell[{index}]')
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
          
    def click_sell_point(self, index):
        locator = (By.ID, f'vms.com.vn.mymobifone:id/lnSellPoint_{index}')
        self.click(locator)
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
    #CLick Icon trong Ưu đãi MyPoint
    def click_icon_mypoint_deals(self, index):
        locator = (By.XPATH, f'(//android.widget.ImageView[@resource-id="vms.com.vn.mymobifone:id/ivAvatar"])[{index}]')
        self.click(locator)
    #Ưu đãi tích điểm
    def click_reward_point(self, index):
        locator = (By.XPATH, f'//XCUIElementTypeWindow/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeScrollView/XCUIElementTypeOther/XCUIElementTypeOther[3]/XCUIElementTypeOther/XCUIElementTypeScrollView/XCUIElementTypeOther[1]/XCUIElementTypeScrollView/XCUIElementTypeOther/XCUIElementTypeCollectionView/XCUIElementTypeCell[{index}]/XCUIElementTypeOther/XCUIElementTypeImage')
        self.click(locator)
    def click_reward_point1(self, index):
        locator = (By.XPATH, f'//XCUIElementTypeWindow/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeScrollView/XCUIElementTypeOther[1]/XCUIElementTypeScrollView/XCUIElementTypeOther/XCUIElementTypeCollectionView/XCUIElementTypeCell[{index}]/XCUIElementTypeOther/XCUIElementTypeImage')
        self.click(locator)
    def click_reward_point3(self, index):
        locator = (By.XPATH, f'//XCUIElementTypeWindow/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeScrollView/XCUIElementTypeOther/XCUIElementTypeOther[4]/XCUIElementTypeScrollView/XCUIElementTypeOther/XCUIElementTypeCollectionView/XCUIElementTypeCell[{index}]/XCUIElementTypeOther/XCUIElementTypeImage')
        self.click(locator)
    def click_reward_point4(self, index):
        locator = (By.XPATH, f'//XCUIElementTypeWindow/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeScrollView/XCUIElementTypeOther[1]/XCUIElementTypeScrollView/XCUIElementTypeOther/XCUIElementTypeCollectionView/XCUIElementTypeCell[{index}]/XCUIElementTypeOther/XCUIElementTypeImage')
        self.click(locator)
    #CLick button Tất cả - Ưu đãi tích điểm
    def click_deals_list_all(self):
        self.click(self.locators.DEALS_LIST_ALL)
    #Click button Tất cả - Ưu đãi khác
    def click_deals_list_all_other(self):
        self.click(self.locators.DEALS_LIST_ALL_OTHER)    
    #         ===== VERIFY =====
    def wait_for_result(self, keyword):
        self.wait_for_text(keyword)

    def is_result_displayed(self, keyword):
        return self.is_text_displayed(keyword)