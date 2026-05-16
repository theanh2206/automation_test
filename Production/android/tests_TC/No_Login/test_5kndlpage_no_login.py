import pytest
from pages.KndlPage_page import KndlPage

#TC157. Click vào button đăng nhập
@pytest.mark.tc157
def test_click_button_login_tc157(driver):
    kndlpage = KndlPage(driver)
    kndlpage.click_icon_kndl(5)
    kndlpage.click_button_login()
    kndlpage.wait_for_result("Đăng nhập")
    assert kndlpage.is_result_displayed("Đăng nhập")
#TC158. Kiểm tra tab giới thiệu
@pytest.mark.tc158
def test_check_tab_introduce_tc158(driver):
    kndlpage = KndlPage(driver)
    kndlpage.click_icon_kndl(5)
    kndlpage.click_by_text("Giới thiệu")
    kndlpage.click_by_text("TÍNH ĐIỂM VÀ TÍCH LŨY ĐIỂM")
    kndlpage.click_by_text("XÉT HẠNG HỘI VIÊN")
    kndlpage.click_by_text("ĐỔI THƯỞNG")
    kndlpage.click_by_text("ƯU ĐÃI HỘI VIÊN")
    kndlpage.click_by_text("THẺ HỘI VIÊN")
    kndlpage.wait_for_result("Giới thiệu")
    assert kndlpage.is_result_displayed("Giới thiệu")
#TC159. Click button đổi quà
@pytest.mark.tc159
def test_click_button_exchange_tc159(driver):
    kndlpage = KndlPage(driver)
    kndlpage.click_icon_kndl(5)
    kndlpage.click_by_text("Đổi quà")
    kndlpage.wait_for_result("Đăng nhập")
    assert kndlpage.is_result_displayed("Đăng nhập")
#TC160. Click button chi tiết
@pytest.mark.tc160
def test_click_button_detail_tc160(driver):
    kndlpage = KndlPage(driver)
    kndlpage.click_icon_kndl(5)
    kndlpage.click_by_text("Chi tiết")
    kndlpage.wait_for_result("Đăng nhập")
    assert kndlpage.is_result_displayed("Đăng nhập")
#TC161. Kiểm tra banner
@pytest.mark.tc161
def test_check_tab_introduce_tc161(driver):
    kndlpage = KndlPage(driver)
    kndlpage.click_icon_kndl(5)
    kndlpage.click_banner()
    kndlpage.wait_for_result("Điểm quy đổi")
    assert kndlpage.is_result_displayed("Điểm quy đổi")
#TC162. Kiểm tra danh sách ưu đãi
@pytest.mark.tc162
def test_list_deal_kndl_tc162(driver):
    kndlpage = KndlPage(driver)
    kndlpage.click_icon_kndl(5)
    # kndlpage.scroll_to_element("Thể Thao")
    kndlpage.click_by_text("Du lịch - Khách sạn")
    kndlpage.click_by_text("HÀNG KHÔNG - VẬN CHUYỂN")
    kndlpage.click_by_text("THỂ THAO")
    kndlpage.click_by_text("SỨC KHOẺ - THẨM MỸ")
    kndlpage.click_by_text("HÀNG TIÊU DÙNG")
    kndlpage.click_by_text("VUI CHƠI GIẢI TRÍ")
    kndlpage.click_by_text("VTVCAB")
    kndlpage.click_button_by_resource_id("vms.com.vn.mymobifone:id/btAccept")
    kndlpage.wait_for_result("Đăng nhập")
    assert kndlpage.is_result_displayed("Đăng nhập")