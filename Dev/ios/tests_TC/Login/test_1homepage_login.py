import pytest
from selenium.webdriver.support import expected_conditions as EC
from pages.HomePage_page import HomePage

#TC01 - Tìm kiếm gói cước có trong DB
@pytest.mark.tc01
def test_search_package_tc01(driver):
    homepage = HomePage(driver)
    homepage.search_package("D5")
    homepage.wait_for_result("Gói Data ngày D5")
    assert homepage.is_result_displayed("Gói Data ngày D5")
#TC02 - Tìm kiếm gói cước không có trong DB
@pytest.mark.tc02
def test_search_package_tc02(driver):
    homepage = HomePage(driver)
    homepage.search_package("DDDDDDDDD")
    homepage.wait_for_result("Không có dữ liệu")
    assert homepage.is_result_displayed("Không có dữ liệu")
#TC03 - Tìm kiếm gói dịch vụ có trong DB
@pytest.mark.tc03
def test_search_package_tc03(driver):
    homepage = HomePage(driver)
    homepage.search_package("Game Data")
    homepage.wait_for_result("Game Data")
    assert homepage.is_result_displayed("Game Data")
#TC04 - Click Avata
@pytest.mark.tc04
def test_click_avata_tc04(driver):
    homepage = HomePage(driver)
    homepage.click_avata()
    homepage.wait_for_result("Hồ sơ cá nhân")
    assert homepage.is_result_displayed("Hồ sơ cá nhân")
#TC05 - Click notification
@pytest.mark.tc05
def test_click_notification_tc05(driver):
    homepage = HomePage(driver)
    homepage.click_notification()
    homepage.wait_for_result("Thông báo")
    assert homepage.is_result_displayed("Thông báo")
#TC06 - Click menu
@pytest.mark.tc06
def test_click_menu(driver):
    homepage = HomePage(driver)
    homepage.click_menu()
    homepage.wait_for_result("Thêm số điện thoại")
    assert homepage.is_result_displayed("Thêm số điện thoại")
#========THÔNG TIN SỬ DỤNG==========
#TC07 - Click thông tin sử dụng
@pytest.mark.tc07
def test_click_information_tc07(driver):
    homepage = HomePage(driver)
    homepage.click_infomation()
    homepage.wait_for_result("Thông tin sử dụng")
    assert homepage.is_result_displayed("Thông tin sử dụng")
#TC08 - Click icon Tra cứu thông thuê bao
@pytest.mark.tc08
def test_click_infor_subcriber_tc08(driver):
    homepage = HomePage(driver)
    homepage.click_infomation()
    homepage.click_infor_subcriber()
    homepage.wait_for_result("Thông tin thuê bao")
    assert homepage.is_result_displayed("Thông tin thuê bao")
#TC09 - Click icon Tra cứu thông tin cước
@pytest.mark.tc09
def test_click_infor_lookup_tc09(driver):
    homepage = HomePage(driver)
    homepage.click_infomation()
    homepage.click_infor_lookup()
    homepage.wait_for_result("Thông tin cước")
    assert homepage.is_result_displayed("Thông tin cước")
#TC10 - Click icon lịch sử nạp tiền
@pytest.mark.tc10
def test_click_deposite_history_tc10(driver):
    homepage = HomePage(driver)
    homepage.click_infomation()
    homepage.click_deposite_history()
    homepage.wait_for_result("Giao dịch trong tháng")
    assert homepage.is_result_displayed("Giao dịch trong tháng")
#TC11 - Click icon Lịch sử gói cước
@pytest.mark.tc11
def test_click_subcriber_history_tc11(driver):
    homepage = HomePage(driver)
    homepage.click_infomation()
    homepage.click_subcriber_history()
    homepage.wait_for_result("Lịch sử gói cước")
    assert homepage.is_result_displayed("Lịch sử gói cước")
#TC12 - Click button Mua thêm trong thông tin sử dụng
@pytest.mark.tc12
def test_click_buy_pakage_tc12(driver):
    homepage = HomePage(driver)
    homepage.click_infomation()
    homepage.wait_for_result("Cước tạm tính")
    homepage.scroll_to_element2("Mua thêm")
    homepage.click_button_by_text("Mua thêm")   
    homepage.wait_for_result("Tất cả gói cước")
    assert homepage.is_result_displayed("Tất cả gói cước")
#TC13 - Click thẻ kết nối dài lâu( Khi chưa đăng ký thẻ)
# @pytest.mark.tc13
# def test_click_button_kndl(driver):
#     homepage = HomePage(driver)
#     homepage.click_infomation()
#     homepage.scroll_to_element2("Thẻ kết nối dài lâu")
#     homepage.click_button_register_KNDL()
#     homepage.wait_for_result("Xác nhận OTP")
#     assert homepage.is_result_displayed("Xác nhận OTP")

#TC13 - Click thẻ kết nối dài lâu( Khi đã đăng ký thẻ)
@pytest.mark.tc13_1
def test_click_card_kndl_tc13_1(driver):
    homepage = HomePage(driver)
    homepage.click_infomation()
    homepage.wait_for_result("Cước tạm tính")
    homepage.scroll_to_element2("Thẻ kết nối dài lâu")
    homepage.click_card_kndl()
    homepage.wait_for_result("Kết nối dài lâu")
    assert homepage.is_result_displayed("Kết nối dài lâu")
#TC13_2. Click các icon tiện ích
@pytest.mark.tc13_2
def test_click_utilities_tc13_2(driver):
    homepage = HomePage(driver)
    homepage.click_infomation()
    homepage.scroll_to_element2("Kích hoạt sim")
    homepage.click_icon_utilities(1)
    homepage.click_button_back()
    homepage.click_icon_utilities(2)
    homepage.click_button_by_text("Huỷ")
    homepage.click_icon_utilities(4)
    homepage.click_button_close1()
    homepage.click_icon_utilities(5)
    homepage.click_button_close1()
    homepage.click_icon_utilities(6)
    homepage.click_button_back1()
    homepage.click_icon_utilities(8)
    homepage.click_button_back1()
    homepage.click_icon_utilities(3)
    homepage.wait_for_result("Chọn chu kỳ gói")
    assert homepage.is_result_displayed("Chọn chu kỳ gói")

#===ĐĂNG KÝ/HUỶ GÓI CƯỚC/DỊCH VỤ===========
#TC14 - Đăng ký gói cước thành công
@pytest.mark.tc14
def test_register_D5_tc14(driver):
    homepage = HomePage(driver)
    homepage.search_package("D7")
    homepage.wait_for_result("D7")
    homepage.click_by_text("Gói Data ngày D7")
    homepage.click_button_by_text("Đăng ký ngay")
    homepage.click_button_by_text("Tiếp tục")
    homepage.click_button_by_text("Xác nhận thanh toán")
    homepage.input_otp("000000")
    homepage.wait_for_result("Đăng ký gói cước thành công")
    assert homepage.is_result_displayed("Đăng ký gói cước thành công")   
#TC15 - Huỷ gói cước thành công
@pytest.mark.tc15
def test_unregister_tc15(driver):
    homepage = HomePage(driver)
    homepage.search_package("D7")
    homepage.wait_for_result("D7")
    homepage.click_by_text("Gói Data ngày D7")
    homepage.click_button_by_text("Huỷ")
    homepage.click_button_by_text("Đồng ý")
    homepage.input_otp("000000")
    homepage.wait_for_result("Huỷ thành công")
    assert homepage.is_result_displayed("Huỷ thành công")
#TC16 - Đăng ký gói dịch vụ
@pytest.mark.tc16
def test_mobigames_register_tc16(driver):
    homepage = HomePage(driver)
    homepage.search_package("MobiGames")
    homepage.wait_for_result("MobiGames")
    homepage.click_by_text("MobiGames", 3)
    homepage.click_button_by_text("btn signed", 1)
    homepage.click_button_by_text("Đăng ký")
    homepage.input_otp("000000")
    homepage.wait_for_result("Đăng ký dịch vụ")
    assert homepage.is_result_displayed("Yêu cầu thành công")
    
#TC17 - Huỷ đăng ký gói dịch vụ
@pytest.mark.tc17
def test_mobigames_unregister_tc17(driver):
    homepage = HomePage(driver)
    homepage.search_package("MobiGames")
    homepage.wait_for_result("MobiGames")
    homepage.click_by_text("MobiGames", 3)
    homepage.click_button_by_text("btn huy", 1)
    homepage.click_button_by_text("Đồng ý")
    homepage.input_otp("000000")
    homepage.wait_for_result("Huỷ dịch vụ")
    assert homepage.is_result_displayed("Gửi yêu cầu huỷ thành công")
#=====GÓI CƯỚC CỦA BẠN=========()
#TC18 - Huỷ gói cước
@pytest.mark.tc18
def test_unregister_my_pakage_tc18(driver):
    homepage = HomePage(driver)
    homepage.click_infomation()
    homepage.scroll_to_element2("Gia hạn gói cước")
    homepage.click_by_text("Data")   
    homepage.click_button_by_text("Huỷ gói cước")   
    homepage.click_button_by_text("Đồng ý")   
    homepage.input_otp("000000")
    homepage.wait_for_result("Huỷ gói cước thành công")
    assert homepage.is_result_displayed("Huỷ gói cước thành công")
#TC19 - Gia hạn gói cước
@pytest.mark.tc19
def test_extend_pakage_tc19(driver):
    homepage = HomePage(driver)
    homepage.click_infomation()
    homepage.scroll_to_element2("Gia hạn gói cước")
    homepage.click_by_text("Data")   
    homepage.click_button_by_text("Gia hạn gói cước", 2)   
    homepage.click_button_by_text("Đồng ý")
    homepage.input_otp("000000")
    homepage.wait_for_result("Gia hạn gói cước thành công")
    assert homepage.is_result_displayed("Gia hạn gói cước thành công")
#TC20 - Huỷ gia hạn tự động gói cước
@pytest.mark.tc20
def test_unextend_pakage_tc20(driver):
    homepage = HomePage(driver)
    homepage.click_infomation()
    homepage.scroll_to_element2("Gia hạn gói cước")
    homepage.click_by_text("Data")
    homepage.click_button_by_text("Hủy tự động gia hạn")
    homepage.click_button_by_text("Xác nhận")
    homepage.input_otp("000000")
    homepage.wait_for_result("Huỷ gia hạn gói cước thành công")
    assert homepage.is_result_displayed("Huỷ gia hạn gói cước thành công")
    
#== Hẹn roaming ======
#TC21 - Đổi lịch hẹn roaming
@pytest.mark.tc21
def test_reschedule(driver):
    homepage = HomePage(driver)
    homepage.click_infomation()
    homepage.scroll_to_element2("Đổi lịch hẹn")
    homepage.click_button_reschedule()
    homepage.et_time("22062026")
    homepage.click_button_submit()
    homepage.input_otp("000000")
    homepage.wait_for_result("Đổi lịch hẹn thành công")
    assert homepage.is_result_displayed("Đổi lịch hẹn thành công")
#TC22 - Huỷ lịch hẹn roaming
@pytest.mark.tc22
def test_cancel_shedule(driver):
    homepage = HomePage(driver)
    homepage.click_infomation()
    homepage.scroll_to_element2("Đổi lịch hẹn")
    homepage.click_button_cancel_schedule()
    homepage.click_button_submit()
    homepage.input_otp("000000")
    homepage.wait_for_result("Huỷ lịch hẹn thành công")
    assert homepage.is_result_displayed("Huỷ lịch hẹn thành công")
#TC23 - Click Mua gói
@pytest.mark.tc23
def test_buy_pakage_tc23(driver):
    homepage = HomePage(driver)
    homepage.click_by_text("Mua gói")
    homepage.wait_for_result("Tất cả gói cước")
    assert homepage.is_result_displayed("Tất cả gói cước")
#TC24 - Click Thanh toán
@pytest.mark.tc24
def test_recharge_tc24(driver):
    homepage = HomePage(driver)
    homepage.click_by_text("Thanh toán")
    homepage.wait_for_result("Thanh toán")
    assert homepage.is_result_displayed("Thanh toán")
#TC25 - Đổi số điện thoại con
@pytest.mark.tc25 
def test_change_number_tc25(driver):
    homepage = HomePage(driver)
    homepage.click_menu()
    homepage.click_by_text("Thêm số điện thoại")
    homepage.add_phone("0931791607")
    homepage.click_button_by_text("TIẾP TỤC")
    homepage.input_otp("888888")
    homepage.click_button_by_text("icon close")
    homepage.close_side_menu_ios()
    homepage.click_by_image("drop_down")
    homepage.click_by_text("0931791607")
    homepage.wait_for_result("0931791607")
    assert homepage.is_result_displayed("0931791607")
#TC26 - Click tiện ích ở ngoài màn trang chủ
@pytest.mark.tc26 
def test_click_utilities_tc26(driver):
    homepage = HomePage(driver)
    homepage.click_icon_utilities1(1)
    homepage.click_button_by_text("arrow left roaming")
    homepage.click_icon_utilities1(2)
    homepage.click_button_by_text("icBack")
    homepage.click_icon_utilities1(3)
    homepage.click_button_by_text("close ekyc")
    homepage.click_icon_utilities1(4)
    homepage.wait_for_text("Thông báo")
    assert homepage.is_result_displayed("Thông báo")
#TC27, TC28 - Click tiện ích ở màn Tất cả tiện ích
@pytest.mark.tc27
def test_click_utilities_tc27(driver):
    homepage = HomePage(driver)
    homepage.click_by_text("Xem tất cả")
    homepage.click_by_text("Chương trình 2-9")
    homepage.click_button_by_text("close ekyc")
    homepage.click_by_text("Hoa hồng C2C")
    homepage.click_button_by_text("close dt")
    homepage.click_by_text("Gói cước dài kỳ")
    homepage.click_button_by_text("close dt")
    homepage.click_by_text("MobiBiz")
    # homepage.click_button_by_text("icBack")
    homepage.click_by_text("Chuyển mạng giữ số")
    homepage.click_button_by_text("icBack")
    homepage.click_by_text("Mở tài khoản Nam Á Bank")
    homepage.click_button_by_text("close ekyc")
    homepage.click_by_text("Ưu đãi 8 tháng 3")
    homepage.click_button_by_text("close dt")
    homepage.wait_for_text("Khuyến mại và Quà tặng")
    assert homepage.is_result_displayed("Khuyến mại và Quà tặng")
#Mục viễn thông
@pytest.mark.tc28
def test_click_utilities_tc28(driver):
    homepage = HomePage(driver)
    homepage.click_by_text("Xem tất cả")
    homepage.scroll_to_element2("Chặn cuộc gọi rác")
    # homepage.click_by_text("Chuyển vùng quốc")
    # homepage.click_button_by_text("arrow left roaming")
    # homepage.click_by_text("Chuẩn hoá thông tin")
    # homepage.click_button_by_text("icBack")
    # homepage.click_by_text("8 tháng 3")
    # homepage.click_button_by_text("icBack")
    # homepage.click_by_text("CHTT")
    homepage.click_by_text("Đổi Esim")
    homepage.click_button_by_text("icBack")
    homepage.click_by_text("Cập nhật địa chỉ")
    homepage.click_by_text("Đóng")
    homepage.click_by_text("Hướng dẫn CVQT")
    homepage.click_button_by_text("close ekyc")
    homepage.click_by_text("Lịch sử esim")
    homepage.click_button_by_text("icBack")
    homepage.click_by_text("Chặn cuộc gọi rác")
    homepage.click_button_by_text("close ekyc")
    homepage.wait_for_text("Hỗ trợ khách hàng")
    assert homepage.is_result_displayed("Tất cả tiện ích")
    
#Kết nối dài lâu
#TC29 - Click thẻ KNDL
@pytest.mark.tc29
def test_click_card_kndl_tc29(driver):
    homepage = HomePage(driver)
    homepage.wait_for_result("Gói cước hấp dẫn")
    homepage.scroll_to_element2("Dịch vụ nổi bật")
    homepage.click_card_kndl()
    homepage.wait_for_result("Kết nối dài lâu")
    assert homepage.is_result_displayed("Kết nối dài lâu")
#TC30 - Click dịch vụ nổi bật
@pytest.mark.tc30
def test_click_services_tc30(driver):
    homepage = HomePage(driver)
    homepage.scroll_to_element2("ON2")
    homepage.click_by_text("ON2")
    homepage.click_button_by_text("icBack")
    homepage.scroll_to_element2("ON2")
    homepage.click_by_text("MobiGames")
    homepage.click_button_by_text("icBack")
    homepage.scroll_to_element2("ON2")
    homepage.click_by_text("Ltest VieON data 4")
    homepage.click_button_by_text("icBack")
    homepage.scroll_to_element2("ON2")
    homepage.click_by_text("Ltest VieON data")
    homepage.wait_for_result("Chi tiết dịch vụ")
    assert homepage.is_result_displayed("Chi tiết dịch vụ")
#Hỗ trợ khách hàng
@pytest.mark.tc31
def test_click_customer_support_tc31(driver):
    homepage = HomePage(driver)
    homepage.scroll_to_element1("Gói cước")
    homepage.click_by_text("Kích hoạt sim")
    homepage.click_button_by_text("icBack")
    homepage.click_by_text("Mua eSIM du lịch quốc tế")
    homepage.click_by_text("Thông tin thuê bao")
    homepage.click_button_by_text("close dt")
    homepage.click_by_text("Gói cước")
    homepage.wait_for_result("Chọn chu kỳ gói")
    assert homepage.is_result_displayed("Chọn chu kỳ gói")
#TC32 - Click vào từng banner
@pytest.mark.tc32
def test_click_banner_tc32(driver):
    homepage = HomePage(driver)
    homepage.scroll_to_element2("ON2")
    homepage.click_banner()
    homepage.wait_for_result("NHẬP SỐ ĐIỆN THOẠI")
    assert homepage.is_result_displayed("NHẬP SỐ ĐIỆN THOẠI")
@pytest.mark.tc32_1   
def test_click_banner_tc32_1(driver):
    homepage = HomePage(driver)
    homepage.scroll_to_element2("Hỗ trợ khách hàng")
    homepage.click_banner2()
    homepage.wait_for_result("Thông báo")
    assert homepage.is_result_displayed("Thông báo")
# @pytest.mark.tc32_2   
# def test_click_banner2(driver):
#     homepage = HomePage(driver)
#     homepage.scroll_to_element("Hỗ trợ khách hàng")
#     homepage.swipe_banner(2)
#     homepage.click_banner()
#     homepage.wait_for_result("Thông báo")
#     assert homepage.is_result_displayed("Thông báo")
# @pytest.mark.tc32_3   
# def test_click_banner3(driver):
#     homepage = HomePage(driver)
#     homepage.scroll_to_element("Hỗ trợ khách hàng")
#     homepage.swipe_banner(3)
#     homepage.click_banner()
#     homepage.wait_for_result("khuyenmai")
#     assert homepage.is_result_displayed("khuyenmai")
# @pytest.mark.tc32_4   
# def test_click_banner4(driver):
#     homepage = HomePage(driver)
#     homepage.scroll_to_element("Hỗ trợ khách hàng")
#     homepage.swipe_banner(4)
#     homepage.click_banner()
#     homepage.wait_for_result("Gói Data ngày D5")
#     assert homepage.is_result_displayed("Gói Data ngày D5")