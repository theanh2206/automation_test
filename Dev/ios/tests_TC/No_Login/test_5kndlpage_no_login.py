import pytest
from pages.KndlPage_page import KndlPage

#TC157. Click vào button đăng nhập
@pytest.mark.tc157
def test_click_button_login_tc157(driver):
    kndlpage = KndlPage(driver)
    kndlpage.click_icon_kndl()
    kndlpage.click_button_by_text("Đăng nhập", 2)
    kndlpage.wait_for_result("Đăng nhập")
    assert kndlpage.is_result_displayed("Đăng nhập")
#TC158. Kiểm tra tab giới thiệu
@pytest.mark.tc158
def test_check_tab_introduce_tc158(driver):
    kndlpage = KndlPage(driver)
    kndlpage.click_button_by_text("KNDL")
    kndlpage.click_by_text("Giới thiệu")
    kndlpage.click_by_text("Tham gia chương trình")
    kndlpage.click_by_text("Tính điểm và tích lũy điểm")
    kndlpage.click_by_text("Xét hạng hội viên")
    kndlpage.click_by_text("Ưu đãi hội viên")
    kndlpage.click_by_text("Thọ Test")
    kndlpage.wait_for_result("Giới thiệu")
    assert kndlpage.is_result_displayed("Giới thiệu")
#TC159. Click button đổi quà
@pytest.mark.tc159
def test_click_button_exchange_tc159(driver):
    kndlpage = KndlPage(driver)
    kndlpage.click_icon_kndl()
    kndlpage.click_by_text("Đổi điểm")
    kndlpage.wait_for_result("Đăng nhập")
    assert kndlpage.is_result_displayed("Số điện thoại")
#TC160. Click button chi tiết
@pytest.mark.tc160
def test_click_button_detail_tc160(driver):
    kndlpage = KndlPage(driver)
    kndlpage.click_icon_kndl()
    kndlpage.click_by_text("Chi tiết")
    kndlpage.wait_for_result("Đăng nhập")
    assert kndlpage.is_result_displayed("Số điện thoại")
#TC161. Kiểm tra banner
@pytest.mark.tc161
def test_check_tab_introduce_tc161(driver):
    kndlpage = KndlPage(driver)
    kndlpage.click_icon_kndl()
    kndlpage.click_banner_kndl()
    kndlpage.wait_for_result("Thông tin ưu đãi")
    assert kndlpage.is_result_displayed("Thông tin ưu đãi")
#TC162. Kiểm tra danh sách ưu đãi
@pytest.mark.tc162
def test_list_deal_kndl_tc162(driver):
    kndlpage = KndlPage(driver)
    kndlpage.click_icon_kndl()
    kndlpage.click_by_text("Khuyến mại Hè 2024")
    kndlpage.click_by_text("GIÁO DỤC")
    kndlpage.click_by_text1("CHĂM SÓC SỨC KHỎE")
    kndlpage.click_by_text1("NHÀ HÀNG")
    kndlpage.click_by_text1("SỨC KHỎE - THẨM MỸ")
    kndlpage.click_by_text1("DU LỊCH - KHÁCH SẠN")
    kndlpage.click_by_text1("HÀNG TIÊU DÙNG")
    kndlpage.click_by_text1("HÀNG KHÔNG - VẬN CHUYỂN")
    kndlpage.click_by_text1("SÂN BAY CÔN ĐẢO")
    kndlpage.click_button_by_text("Đăng nhập")
    kndlpage.wait_for_result("Số điện thoại")
    assert kndlpage.is_result_displayed("Số điện thoại")