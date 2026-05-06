from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

options = webdriver.ChromeOptions()

options.add_argument("--disable-features=BlockInsecurePrivateNetworkRequests")
options.add_argument("--disable-notifications")
options.add_argument("--disable-infobars")

driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()),
    options=options
)
try:
    wait = WebDriverWait(driver, 20)
    # 1. Mở website
    driver.get("http://160.25.81.212:5173/")
    
    # 2. Truyền username
    username_input = wait.until(
        EC.presence_of_element_located((By.XPATH, "//label[contains(text(),'Tài khoản')]"))
    )
    time.sleep(2)
    username_input.send_keys("admin")

    # 3. Truyền password
    password_input = wait.until(
        EC.presence_of_element_located((By.XPATH, "//input[@type='password']"))
    )
    time.sleep(2)
    password_input.send_keys("host")

    # 4. Click button đăng nhập
    btn_login = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Đăng nhập')]"))
    )
    btn_login.click()
    
    elements = wait.until(lambda d: d.find_elements(
    By.XPATH,
    "//button[contains(text(),'Đăng xuất')]"
    ))
    
    time.sleep(5)
    #5. Tiếp nhận khách
    text = "Tiếp nhận khách"

    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, f'//*[text()="{text}"]'))
    ).click()
    
    
    
    
    
    # 5. Bắt key đăng nhập thành công
    
    elements = wait.until(lambda d: d.find_elements(
    By.XPATH,
    "//button[contains(text(),'Đăng xuất')]"
    ))

    if len(elements) > 0:
        print("✅ LOGIN SUCCESS")
    else:
        print("❌ LOGIN FAILED")
    time.sleep(2)

finally:
    driver.quit()