from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

    # ===== PLATFORM =====
    def is_android(self):
        return self.driver.capabilities['platformName'].lower() == 'android'

    def is_ios(self):
        return self.driver.capabilities['platformName'].lower() == 'ios'

    # ===== LOCATOR BUILDER =====
    def get_text_locator(self, text):
        if self.is_android():
            return (
                AppiumBy.ANDROID_UIAUTOMATOR,
                f'new UiSelector().textContains("{text}")'
            )
        else:
            return (
                AppiumBy.IOS_PREDICATE,
                f'label CONTAINS "{text}"'
            )

    # ===== COMMON ACTION =====
    def click(self, locator):
        element = self.wait.until(EC.visibility_of_element_located(locator))
        element.click()

    def send_keys(self, locator, text):
        element = self.wait.until(EC.visibility_of_element_located(locator))
        element.clear()
        element.send_keys(text)

    def find(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))

    def find_all(self, locator):
        return self.driver.find_elements(*locator)
    
    def tap_outside(self):
        size = self.driver.get_window_size()

        x = int(size["width"] * 0.85)
        y = int(size["height"] * 0.3)

        self.driver.tap([(x, y)])
    def press_back(self):
        self.driver.back()
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
    # ===== WAIT =====
    def wait_for_element(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))

    def wait_for_text(self, text):
        locator = self.get_text_locator(text)
        return self.wait.until(EC.presence_of_element_located(locator))

    # ===== VERIFY =====
    def is_element_displayed(self, locator):
        return len(self.find_all(locator)) > 0

    def is_text_displayed(self, text):
        locator = self.get_text_locator(text)
        return len(self.find_all(locator)) > 0
    
    