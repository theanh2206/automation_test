import pytest
from selenium.webdriver.support import expected_conditions as EC
from pages.HomePage_page import HomePage

#TC130. CLick button đăng nhập
@pytest.mark.tc130
def test_click_button_login_tc130(driver):
    homepage = HomePage(driver)
    homepage.click_button_login()
    homepage.wait_for_result("Đăng nhập")
    assert homepage.is_result_displayed("Đăng nhập")
#TC131. Click vào sidebar
@pytest.mark.tc131
def test_click_sidebar_tc131(driver):
    homepage = HomePage(driver)
    homepage.click_menu()
    homepage.wait_for_result("Đăng nhập")
    assert homepage.is_result_displayed("Đăng nhập")
#TC132. Click vào button chuyển ngôn ngữ
@pytest.mark.tc132
def test_click_swipe_language_tc132(driver):
    homepage = HomePage(driver)
    homepage.click_switch_language()
    homepage.wait_for_result("Login")
    homepage.click_switch_language()
    texts = ["Login", "Đăng nhập"]
    found = False
    for text in texts:
        try:
            homepage.wait_for_result(text)
            found = True
            break
        except:
            continue

    assert found, "❌ Không tìm thấy text hợp lệ"
#TC133. Click vào tiện ích ở ngoài màn trang chủ
@pytest.mark.tc133
def test_click_icon_utilities_tc133(driver):
    homepage = HomePage(driver)
    homepage.click_by_text("Chuẩn hoá thông tin")
    homepage.press_back()
    homepage.click_by_text("Hòa mạng")
    homepage.press_back()
    homepage.click_by_text("Kích hoạt sim")
    homepage.press_back()
    homepage.click_by_text("Zalo miniApp")
    homepage.wait_for_result("Đăng nhập")
    assert homepage.is_result_displayed("Đăng nhập")
#TC134. Click vào tiện ích ở màn tất cả tiện ích
@pytest.mark.tc134
def test_click_icon_utilities_tc134(driver):
    homepage = HomePage(driver)
    homepage.click_by_text("Xem tất cả")
    homepage.click_by_text("Thanh Toán")
    homepage.press_back()
    homepage.click_by_text("Kích hoạt sim")
    homepage.press_back()
    homepage.click_by_text("Chuẩn hoá thông tin")
    homepage.press_back()
    homepage.click_by_text("Hòa mạng")
    homepage.press_back()
    homepage.click_by_text("Chuyển mạng giữ số")
    homepage.press_back()
    homepage.scroll_to_element1("Dịch vụ khác")
    homepage.click_by_text("MobiFone CA")
    homepage.press_back()
    homepage.click_by_text("Mua SIM")
    homepage.press_back()
    homepage.click_by_text("Zalo miniApp")
    homepage.wait_for_result("Đăng nhập")
    assert homepage.is_result_displayed("Đăng nhập")
#TC135. Click vào từng dịch vụ nổi bật
@pytest.mark.tc135
def test_click_avata_contact_tc135(driver):
    homepage = HomePage(driver)
    homepage.scroll_to_element1("Dịch vụ nổi bật")
    homepage.click_avata_contact(1)
    homepage.wait_for_result("Chi tiết dịch vụ")
    homepage.press_back()
    homepage.click_avata_contact(2)
    homepage.wait_for_result("Chi tiết dịch vụ")
    homepage.press_back()
    homepage.click_avata_contact(3)
    homepage.wait_for_result("Chi tiết dịch vụ")
    homepage.press_back()
    homepage.click_avata_contact(4)
    homepage.wait_for_result("Chi tiết dịch vụ")
    homepage.press_back()
    homepage.wait_for_result("Dịch vụ nổi bật")
    assert homepage.is_result_displayed("Dịch vụ nổi bật")
#TC136. Click gói cước hấp dẫn
@pytest.mark.tc136
def test_click_avata_contact_tc136(driver):
    homepage = HomePage(driver)
    homepage.click_by_text("Chi tiết")
    homepage.press_back()
    homepage.click_by_text("Xem tất cả", 2)
    homepage.press_back()
    homepage.wait_for_result("Gói cước hấp dẫn")
    assert homepage.is_result_displayed("Gói cước hấp dẫn")
#TC137. Click tiện ích hỗ trợ trợ khách hàng
@pytest.mark.tc137
def test_click_customer_support_tc137(driver):
    homepage = HomePage(driver)
    homepage.scroll_to_element1("Hỗ trợ khách hàng")
    homepage.click_by_text("Chuẩn hoá thông tin")
    homepage.press_back()
    homepage.click_by_text("Hòa mạng")
    homepage.press_back()
    homepage.click_by_text("Chuyển mạng giữ số")
    homepage.press_back()
    homepage.click_by_text("Zalo miniApp")
    homepage.press_back()
    homepage.click_by_text("Xem tất cả")
    homepage.wait_for_result("Đăng nhập")
    assert homepage.is_result_displayed("Đăng nhập")
    