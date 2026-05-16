import pytest
from pages.KndlPage_page import KndlPage

#TC93. Kiểm tra tab giới thiệu
@pytest.mark.tc93
def test_check_tab_introduce_tc93(driver):
    kndlpage = KndlPage(driver)
    kndlpage.click_icon_kndl(5)
    kndlpage.click_by_text("Giới thiệu")
    kndlpage.click_by_text("TÍNH ĐIỂM VÀ TÍCH LŨY ĐIỂM")
    kndlpage.click_by_text("XÉT HẠNG HỘI VIÊN")
    kndlpage.click_by_text("ĐỔI THƯỞNG")
    kndlpage.click_by_text("ƯU ĐÃI HỘI VIÊN")
    kndlpage.click_by_text("THỌ TEST")
    kndlpage.wait_for_result("Giới thiệu")
    assert kndlpage.is_result_displayed("Giới thiệu")
    
#TC94. Đổi điểm cước di động
@pytest.mark.tc94
def test_change_point_tc94(driver):
    kndlpage = KndlPage(driver)
    kndlpage.click_icon_kndl(5)
    kndlpage.click_by_text("Đổi quà")
    kndlpage.click_add_pakage()
    kndlpage.click_exchange_point()
    kndlpage.click_buttom_confirm()
    kndlpage.input_otp("000000")
    kndlpage.wait_for_result("Thành công")
    assert kndlpage.is_result_displayed("Thành công")

#TC95. Đổi gói combo
@pytest.mark.tc95
def test_change_combo_pakage_tc95(driver):
    kndlpage = KndlPage(driver)
    kndlpage.click_icon_kndl(5)
    kndlpage.click_by_text("Đổi quà")
    kndlpage.click_by_text("Đổi gói combo")
    kndlpage.click_add_pakage()
    kndlpage.click_exchange_point()
    kndlpage.click_buttom_confirm()
    kndlpage.input_otp("000000")
    kndlpage.wait_for_result("Thành công")
    assert kndlpage.is_result_displayed("Thành công")
#TC96. Đổi gói thoại
@pytest.mark.tc96
def test_change_voice_pakage_tc96(driver):
    kndlpage = KndlPage(driver)
    kndlpage.click_icon_kndl(5)
    kndlpage.click_by_text("Đổi quà")
    kndlpage.click_by_text("Gói thoại")
    kndlpage.click_add_pakage()
    kndlpage.click_exchange_point()
    kndlpage.click_buttom_confirm()
    kndlpage.input_otp("000000")
    kndlpage.wait_for_result("Thành công")
    assert kndlpage.is_result_displayed("Thành công")
#TC97. Đổi quà tặng
@pytest.mark.tc97
def test_change_gift_pakage_tc97(driver):
    kndlpage = KndlPage(driver)
    kndlpage.click_icon_kndl(5)
    kndlpage.click_by_text("Đổi quà")
    kndlpage.click_by_text("Gói thoại")
    kndlpage.click_by_text("Quà tặng")
    kndlpage.click_button_exchange()
    kndlpage.click_add_pakage()
    kndlpage.click_buy_now()
    kndlpage.click_buttom_confirm()
    kndlpage.input_otp("000000")
    kndlpage.wait_for_result("Thành công")
    assert kndlpage.is_result_displayed("Thành công")
#TC98. Đổi data code
@pytest.mark.tc98
def test_change_data_code_tc98(driver):
    kndlpage = KndlPage(driver)
    kndlpage.click_icon_kndl(5)
    kndlpage.click_by_text("Đổi quà")
    kndlpage.click_by_text("Gói thoại")
    kndlpage.click_by_text("Quà tặng")
    kndlpage.click_by_text("Datacode")
    kndlpage.click_by_text("Đổi ngay")
    kndlpage.click_button_accept()
    kndlpage.click_buttom_confirm()
    kndlpage.input_otp("000000")
    kndlpage.wait_for_result("Thành công")
    assert kndlpage.is_result_displayed("Thành công")
#TC99. VETC - Bông sen vàng
@pytest.mark.tc99
def test_change_VETC_tc99(driver):
    kndlpage = KndlPage(driver)
    kndlpage.click_icon_kndl(5)
    kndlpage.click_by_text("Đổi quà")
    kndlpage.click_by_text("Gói thoại")
    kndlpage.click_by_text("Quà tặng")
    kndlpage.click_by_text("Datacode")
    kndlpage.click_by_text("Bông sen vàng")
    kndlpage.click_by_text("VETC")
    kndlpage.click_by_text("Đổi ngay")
    kndlpage.click_kndl_confirm()
    kndlpage.input_otp("000000")
    kndlpage.wait_for_result("Đổi điểm thành công")
    assert kndlpage.is_result_displayed("Đổi điểm thành công")
#TC100. CLick button reload
@pytest.mark.tc100
def test_click_button_reload_tc100(driver):
    kndlpage = KndlPage(driver)
    kndlpage.click_icon_kndl(5)
    kndlpage.click_by_text("Chi tiết")
    kndlpage.click_button_refesh()
    kndlpage.wait_for_result("Thông tin hội viên")
    assert kndlpage.is_result_displayed("Thông tin hội viên")
#TC101. CLick button Xem thêm 
@pytest.mark.tc101
def test_button_seemore_tc101(driver):
    kndlpage = KndlPage(driver)
    kndlpage.click_icon_kndl(5)
    kndlpage.click_by_text("Chi tiết")
    kndlpage.click_button_seemore()
    kndlpage.wait_for_result("Giới thiệu")
    assert kndlpage.is_result_displayed("Giới thiệu")
#TC102. Click button Đăng ký ngay - Kết nối dài lâu bông sen vàng
@pytest.mark.tc102
def test_button_register_tc102(driver):
    kndlpage = KndlPage(driver)
    kndlpage.click_icon_kndl(5)
    kndlpage.click_by_text("Chi tiết")
    kndlpage.scroll_to_element("Đăng ký ngay")
    kndlpage.click_by_text("Đăng ký ngay")
    kndlpage.wait_for_result("Bông Sen Vàng")
    assert kndlpage.is_result_displayed("Bông Sen Vàng")
#TC103. Swipe banner/click kết nối dài lâu ngang
@pytest.mark.tc103
def test_swipe_banner_tc103(driver):
    kndlpage = KndlPage(driver)
    kndlpage.click_icon_kndl(5)
    kndlpage.swipe_banner(2)
    kndlpage.click_banner()
    kndlpage.wait_for_result("Thông tin")
    assert kndlpage.is_result_displayed("Thông tin")
#TC104. Kiểm tra lịch sử ưu đãi
@pytest.mark.tc104
def test_check_history_tc104(driver):
    kndlpage = KndlPage(driver)
    kndlpage.click_icon_kndl(5)
    kndlpage.click_by_text("Lịch sử ưu đãi")
    kndlpage.wait_for_result("Lịch sử ưu đãi")
    assert kndlpage.is_result_displayed("Lịch sử ưu đãi")
#TC105. Kiểm tra danh sách ưu đãi
@pytest.mark.tc105
def test_list_deal_kndl_tc105(driver):
    kndlpage = KndlPage(driver)
    kndlpage.click_icon_kndl(5)
    kndlpage.search_list_deal_kndl("Sân bay")
    kndlpage.click_by_text("SÂN BAY CÔN ĐẢO")
    kndlpage.click_button_accept()
    kndlpage.wait_for_result("Xác nhận thông tin")
    kndlpage.input_email("anh.vu11@mobifon.vn")
    kndlpage.press_back()
    kndlpage.click_kndl_confirm()
    kndlpage.wait_for_result("Xác nhận sử dụng ưu đãi")
    assert kndlpage.is_result_displayed("Xác nhận sử dụng ưu đãi")