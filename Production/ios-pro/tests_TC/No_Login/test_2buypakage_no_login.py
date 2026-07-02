import pytest
from selenium.webdriver.support import expected_conditions as EC
from pages.BuyPakagePage_page import BuyPakagePage

#TC138. Click button đăng nhập
@pytest.mark.tc138
def test_click_button_login_tc138(driver):
    buypakage = BuyPakagePage(driver)
    buypakage.click_buy_pakage()
    buypakage.click_button_by_text("Đăng nhập", 2)
    buypakage.wait_for_result("Đăng nhập")
    assert buypakage.is_result_displayed("Đăng nhập")
#TC139. Click button đăng nhập
@pytest.mark.tc139
def test_click_button_login_tc139(driver):
    buypakage = BuyPakagePage(driver)
    buypakage.click_buy_pakage()
    buypakage.click_menu()
    buypakage.wait_for_result("Đăng nhập")
    assert buypakage.is_result_displayed("Đăng nhập")
#TC140. Click danh mục nhóm gói
@pytest.mark.tc140
def test_click_categories_tc140(driver):
    buypakage = BuyPakagePage(driver)
    buypakage.click_buy_pakage()
    buypakage.wait_for_result("HOT")
    buypakage.click_by_text("Data")
    buypakage.click_by_text("Combo")
    buypakage.click_by_text("Mạng xã hội")
    buypakage.click_by_text("Chuyển vùng quốc tế")
    buypakage.click_by_text("Gói bổ sung")
    buypakage.wait_for_result("Đăng nhập")
    assert buypakage.is_result_displayed("Đăng nhập")
#TC141. Click chọn chu kỳ gói cước
@pytest.mark.tc141
def test_click_cycle_tc141(driver):
    buypakage = BuyPakagePage(driver)
    buypakage.click_buy_pakage()
    buypakage.wait_for_result("HOT")
    buypakage.click_by_text("Gói ngày")
    buypakage.click_by_text("Gói tháng")
    buypakage.click_by_text("Tất cả")
    buypakage.wait_for_result("Đăng nhập")
    assert buypakage.is_result_displayed("Đăng nhập")
#TC142. Lọc gói cước theo giá
@pytest.mark.tc142
def test_click_sort_price_tc142(driver):
    buypakage = BuyPakagePage(driver)
    buypakage.click_buy_pakage()
    # buypakage.click_by_text("Data_2025")
    # buypakage.click_by_text("Giá")
    buypakage.wait_for_result("D5")
    buypakage.click_by_text("Giá")
    buypakage.wait_for_result("Đăng nhập")
    buypakage.click_by_text("Giá")
    assert buypakage.is_result_displayed("Đăng nhập")
#TC143. Lọc gói cước dung lượng
@pytest.mark.tc143
def test_click_sort_data_tc143(driver):
    buypakage = BuyPakagePage(driver)
    buypakage.click_buy_pakage()
    # buypakage.click_by_text("Data_2025")
    buypakage.click_by_text("Dung lượng")
    buypakage.wait_for_result("Đăng nhập")
    buypakage.click_by_text("Dung lượng")
    assert buypakage.is_result_displayed("Đăng nhập")
#TC144. Kiểm tra màn hình tất cả gói cước
@pytest.mark.tc144
def test_check_view_all_pakage_tc144(driver):
    buypakage = BuyPakagePage(driver)
    buypakage.click_buy_pakage()
    buypakage.click_by_text("Xem tất cả")
    buypakage.search_package1("D5")
    buypakage.click_button_by_text("Done")
    buypakage.click_button_by_text("Chi tiết")
    buypakage.click_by_text("Đăng ký ngay")
    buypakage.wait_for_result("Đăng nhập")
    assert buypakage.is_result_displayed("Đăng nhập")
    