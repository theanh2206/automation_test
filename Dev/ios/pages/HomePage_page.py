from email.mime import text
from operator import index

from appium.webdriver.common.appiumby import AppiumBy
from pages.BasePage_page import BasePage
from pages.LocatorPage_page import LocatorPage
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput
from selenium.webdriver.common.actions import interaction
from selenium.common.exceptions import NoSuchElementException
import time


class HomePage(BasePage):
    locators = LocatorPage()
    #Click guide by text
    def click_by_text(self, text, index=1):
        xpath = f'//XCUIElementTypeStaticText[@name="{text}"][{index}]'
        element = self.driver.find_element(AppiumBy.XPATH, xpath)
        element.click()
    def click_by_text1(self, text, index):
        els = WebDriverWait(self.driver, 10).until(
            lambda d: d.find_elements(
                "-ios predicate string",
                f"name == '{text}'"
        )
    )
        if len(els) > index:
            els[index].click()
        else:
            raise Exception(f"Không tìm thấy phần tử thứ {index+1} với text: {text}")
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
    # Hàm scroll tới phần tử cụ thể
    def scroll_to_element1(self, text, max_scroll=6):
        for i in range(max_scroll):
            print(f"🔍 Lần {i+1}: tìm '{text}'")

            elements = self.driver.find_elements(
                AppiumBy.IOS_PREDICATE,
                f'name CONTAINS[c] "{text}" OR label CONTAINS[c] "{text}" OR value CONTAINS[c] "{text}"'
            )

            if elements:
                return elements[0]

            try:
                scroll_view = self.driver.find_element(
                    AppiumBy.IOS_CLASS_CHAIN,
                    '**/XCUIElementTypeScrollView'
                )
                self.driver.execute_script(
                    "mobile: scroll",
                    {
                        "element": scroll_view.id,
                        "direction": "down"
                    }
                )
            except Exception as e:
                print("⚠️ Không tìm thấy scroll view:", e)
            time.sleep(1)
        raise Exception(f"❌ Không tìm thấy: {text}")
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
    
    def close_side_menu_ios(self):
        size = self.driver.get_window_size()
        self.driver.tap([
            (int(size['width'] * 0.9), int(size['height'] * 0.5))
        ])
    #Swipe banner ngang
    def swipe_banner(self, times=1, delay=0.5):
        try:
            banner = self.driver.find_element(
                AppiumBy.IOS_CLASS_CHAIN,
                '**/XCUIElementTypeCollectionView'
            )
            indicator = self.driver.find_element(
                AppiumBy.IOS_CLASS_CHAIN,
                '**/XCUIElementTypePageIndicator'
            )
        except:
            raise Exception
        prev_value = indicator.get_attribute("value")
        for i in range(times):
            print(f"👉 Swipe lần {i+1}")
            self.driver.execute_script("mobile: swipe", {
                "element": banner.id,
                "direction": "left"
            })
            time.sleep(delay)
            current_value = indicator.get_attribute("value")
            # 👉 Nếu swipe mà không đổi → stop sớm
            if current_value == prev_value:
                break
            prev_value = current_value
    #----------Hàm nhập OTP-----------
    def input_otp(self, otp_code):
        otp_inputs = self.wait.until(
            EC.presence_of_all_elements_located(
                (AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeTextField')
        )
    )
        for i, digit in enumerate(otp_code):
            otp_inputs[i].send_keys(digit)
    # Hàm scroll tới phần tử cụ thể
    def scroll_to_element3(self, text, max_scroll=6):
        for _ in range(max_scroll):
            elements = self.driver.find_elements(
                AppiumBy.ACCESSIBILITY_ID, text
        )
            if elements:
                return elements[0]

            self.driver.execute_script("mobile: swipe", {"direction": "up"})

        raise Exception(f"Không tìm thấy {text}")
    # Hàm tìm kiếm gói cước
    def search_package(self, keyword):
        self.click(self.locators.SEARCH_BOX)
        self.send_keys(self.locators.SEARCH_INPUT, keyword)
    #Click tiện ích nổi bật
    def click_icon_utilities(self, index):
        locator = (By.XPATH, f'//XCUIElementTypeScrollView/XCUIElementTypeOther[7]/XCUIElementTypeCollectionView/XCUIElementTypeCell[{index}]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeImage')
        self.click(locator)
    def click_icon_utilities1(self, index):
        locator = (By.XPATH, f'//XCUIElementTypeScrollView/XCUIElementTypeOther[2]/XCUIElementTypeOther[1]/XCUIElementTypeCollectionView/XCUIElementTypeCell[{index}]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeImage')
        self.click(locator)
    def click_button_close1(self):
        self.click(self.locators.BUTTON_CLOSE1) 
    def click_button_back1(self):
        self.click(self.locators.BUTTON_BACK1)
    #Click button Back
    def click_button_back(self):
        self.click(self.locators.BUTTON_BACK)
    #Click icon avata
    def click_avata(self):
        self.click(self.locators.AVATA)    
    #Click icon Thông báo
    def click_notification(self):
        self.click(self.locators.NOTIFICATION)
    #Click banner
    def click_banner(self):
        self.click(self.locators.BANNER)
    def click_banner2(self):
        self.click(self.locators.BANNER2)
    def click_banner3(self):
        self.click(self.locators.BANNER3)
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
    #Click card KNDL (SĐT đã đăng ký KNDL)
    def click_card_kndl(self):
        self.click(self.locators.KNDL)
    def click_card_kndl1(self):
        self.click(self.locators.KNDL1)
    #Click button đăng ký D5
    def click_register_d5(self):
        self.click(self.locators.REGISTER_BUTTON)
    def add_phone(self, keyword):
        self.send_keys(self.locators.INPUT_PHONE, keyword)
    def click_button_accept(self):
        self.click(self.locators.BUTTON_ACCEPT)
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