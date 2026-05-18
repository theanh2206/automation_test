import pytest
from selenium.webdriver.support import expected_conditions as EC
from pages.BuyPakagePage_page import BuyPakagePage

#TC138. Click button đăng nhập
@pytest.mark.tc138
def test_click_button_login_tc138(driver):
    buypakage = BuyPakagePage(driver)
    buypakage.click_buy_pakage()
    buypakage.click_button_by_resource_id("vms.com.vn.mymobifone:id/btLogin")
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
    buypakage.click_category_by_index(1)
    buypakage.click_category_by_index(2)
    buypakage.click_category_by_index(3)
    # buypakage.click_category_by_index(4)
    buypakage.wait_for_result("Đăng nhập")
    assert buypakage.is_result_displayed("Đăng nhập")
#TC141. Click chọn chu kỳ gói cước
@pytest.mark.tc141
def test_click_cycle_tc141(driver):
    buypakage = BuyPakagePage(driver)
    buypakage.click_buy_pakage()
    buypakage.click_radio_button_days()
    buypakage.click_radio_button_months()
    buypakage.click_radio_button_all()
    buypakage.wait_for_result("Xem tất cả")
    assert buypakage.is_result_displayed("Xem tất cả")
#TC142. Lọc gói cước theo giá
@pytest.mark.tc142
def test_click_sort_price_tc142(driver):
    buypakage = BuyPakagePage(driver)
    buypakage.click_buy_pakage()
    buypakage.click_category_by_index(2)
    buypakage.wait_for_result("Data")
    buypakage.click_button_by_resource_image("vms.com.vn.mymobifone:id/ivSortingPrice")
    buypakage.wait_for_result("D5")
    buypakage.click_button_by_resource_image("vms.com.vn.mymobifone:id/ivSortingPrice")
    buypakage.wait_for_result("12SMAX")
    assert buypakage.is_result_displayed("12SMAX")
#TC143. Lọc gói cước dung lượng
@pytest.mark.tc143
def test_click_sort_data_tc143(driver):
    buypakage = BuyPakagePage(driver)
    buypakage.click_buy_pakage()
    buypakage.wait_for_result("Data")
    buypakage.click_category_by_index(2)
    buypakage.click_sort_data()
    buypakage.click_sort_data()
    buypakage.wait_for_result("D5")
    buypakage.click_sort_data()
    buypakage.wait_for_result("6SMAX")
    assert buypakage.is_result_displayed("6SMAX")
#TC144. Kiểm tra màn hình tất cả gói cước
@pytest.mark.tc144
def test_check_view_all_pakage_tc144(driver):
    buypakage = BuyPakagePage(driver)
    buypakage.click_buy_pakage()
    buypakage.click_by_text("Xem tất cả")
    buypakage.search_package1("D5")
    buypakage.wait_for_result("D5")
    buypakage.press_back()
    buypakage.click_by_text("Chi tiết")
    buypakage.click_text_by_resource_id("vms.com.vn.mymobifone:id/tvRegister")
    buypakage.wait_for_result("Đăng nhập")
    assert buypakage.is_result_displayed("Đăng nhập")
    