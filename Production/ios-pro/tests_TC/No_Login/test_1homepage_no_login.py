import pytest
from selenium.webdriver.support import expected_conditions as EC
from pages.HomePage_page import HomePage

#TC130. CLick button đăng nhập
@pytest.mark.tc130
def test_click_button_login_tc130(driver):
    homepage = HomePage(driver)
    homepage.click_button_by_text("Đăng nhập", 2)
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
    homepage.click_button_by_text("language vi")
    homepage.wait_for_result("Login")
    homepage.click_button_by_text("language vi")
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
    homepage.click_button_by_text("icBack")
    homepage.click_by_text("Hòa mạng")
    homepage.click_button_by_text("icBack")
    homepage.click_by_text("Kích hoạt sim")
    homepage.click_button_by_text("icBack")
    homepage.scroll_left(times=1)
    homepage.wait_for_result("Thanh Toán")
    homepage.click_by_text("Thanh Toán")
    homepage.click_button_by_text("icBack")
    homepage.click_by_text("Mua SIM")
    homepage.click_button_by_text("icBack")
    homepage.scroll_left(times=1)
    homepage.click_by_text("MobiFone CA")
    homepage.wait_for_result("MobiFone CA")
    homepage.click_button_by_text("icBack")
    homepage.click_by_text("Tích điểm nhận quà")
    assert homepage.is_result_displayed("Liên kết ngay")
# TC134. Click các button xem tất cả
@pytest.mark.tc134
def test_click_icon_utilities_tc134(driver):
    homepage = HomePage(driver)
    homepage.click_by_text("Xem tất cả")
    homepage.click_button_by_text("icBack")
    homepage.scroll_to_element2("Dịch vụ nổi bật")
    homepage.click_by_text1("Xem tất cả", 2)
    homepage.click_button_by_text("icBack")
    homepage.scroll_to_element2("Hỗ trợ khách hàng")
    homepage.click_by_text1("Xem tất cả", 3)
    homepage.click_button_by_text("icBack")
    homepage.wait_for_result("Hỗ trợ khách hàng")
    assert homepage.is_result_displayed("Hỗ trợ khách hàng")
# TC135. Click vào từng dịch vụ nổi bật
@pytest.mark.tc135
def test_click_avata_contact_tc135(driver):
    homepage = HomePage(driver)
    homepage.scroll_to_element2("Vietlott SMS")
    homepage.click_by_text("Vietlott SMS")
    homepage.click_button_by_text("icBack")
    homepage.scroll_to_element2("Vietlott SMS")
    homepage.click_by_text("MobiSafe")
    homepage.click_button_by_text("icBack")
    homepage.scroll_to_element2("Vietlott SMS")
    homepage.click_by_text("MobiPA")
    homepage.click_button_by_text("icBack")
    homepage.scroll_to_element2("Vietlott SMS")
    homepage.click_by_text("MobiGames")
    homepage.wait_for_result("Chi tiết dịch vụ")
    assert homepage.is_result_displayed("Chi tiết dịch vụ")
#TC136. Click gói cước hấp dẫn
@pytest.mark.tc136
def test_click_avata_contact_tc136(driver):
    homepage = HomePage(driver)
    homepage.click_button_by_text("Chi tiết")
    homepage.click_button_by_text("icBack")
    homepage.click_by_text("Xem tất cả")
    homepage.click_button_by_text("icBack")
    homepage.wait_for_result("Gói cước hấp dẫn")
    assert homepage.is_result_displayed("Gói cước hấp dẫn")
#TC137. Click tiện ích hỗ trợ trợ khách hàng
@pytest.mark.tc137
def test_click_customer_support_tc137(driver):
    homepage = HomePage(driver)
    homepage.scroll_to_element2("Chuẩn hoá thông tin")
    homepage.click_by_text("Chuẩn hoá thông tin")
    homepage.click_button_by_text("icBack")
    homepage.click_by_text("Hòa mạng")
    homepage.click_button_by_text("icBack")
    homepage.click_by_text("Chuyển mạng giữ số")
    homepage.click_by_text("Đăng ký")
    homepage.click_button_by_text("icBack")
    homepage.click_by_text("Tra cứu khả năng chuyển mạng")
    homepage.click_button_by_text("icBack")
    homepage.click_by_text("Tra cứu trạng thái yêu cầu")
    homepage.click_button_by_text("icBack")
    homepage.click_by_text("Thông tin gói cước cam kết")
    homepage.click_button_by_text("icBack")
    homepage.click_button_by_text("icBack")
    homepage.wait_for_result("Hỗ trợ khách hàng")
    assert homepage.is_result_displayed("Hỗ trợ khách hàng")
    