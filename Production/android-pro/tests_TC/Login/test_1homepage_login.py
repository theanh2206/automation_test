import pytest
from selenium.webdriver.support import expected_conditions as EC
from pages.HomePage_page import HomePage

#TC01 - Tìm kiếm gói cước có trong DB
@pytest.mark.tc01
def test_search_package_D5_tc01(driver):
    homepage = HomePage(driver)
    homepage.search_package("D5")
    homepage.wait_for_result("D5")
    assert homepage.is_result_displayed("D5")    
#TC02 - Tìm kiếm gói cước không có trong DB
@pytest.mark.tc02
def test_search_package_tc02(driver):
    homepage = HomePage(driver)
    homepage.search_package("DDDDDDDDD")
    homepage.wait_for_result("DDDDDDDDD")
    assert homepage.is_result_displayed("Lịch sử tìm kiếm")
#TC03 - Tìm kiếm gói dịch vụ có trong DB
@pytest.mark.tc03
def test_search_package_DV_tc03(driver):
    homepage = HomePage(driver)
    homepage.search_package("MobiGames")
    homepage.wait_for_result("MobiGames")
    assert homepage.is_result_displayed("MobiGames")
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
def test_click_menu_tc06(driver):
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
    homepage.scroll_to_element("Mua thêm")
    homepage.click_button_buy_pakage()
    homepage.wait_for_result("Tất cả gói cước")
    assert homepage.is_result_displayed("Tất cả gói cước")
# #TC13 - Click thẻ kết nối dài lâu( Khi chưa đăng ký thẻ)
# @pytest.mark.tc13
# def test_click_button_kndl_tc13(driver):
#     homepage = HomePage(driver)
#     homepage.click_infomation()
#     homepage.scroll_to_element("Thẻ kết nối dài lâu")
#     homepage.click_button_register_KNDL()
#     homepage.wait_for_result("Xác nhận OTP")
#     assert homepage.is_result_displayed("Xác nhận OTP")

#TC13 - Click thẻ kết nối dài lâu( Khi đã đăng ký thẻ)
@pytest.mark.tc13_1
def test_click_card_kndl_tc13_1(driver):
    homepage = HomePage(driver)
    homepage.click_infomation()
    homepage.scroll_to_element("Thẻ Kết Nối Dài Lâu")
    homepage.click_card_kndl()
    homepage.wait_for_result("Kết nối dài lâu")
    assert homepage.is_result_displayed("Kết nối dài lâu")
#TC13_1 Click các icon tiện ích
@pytest.mark.tc13_2
def test_click_utilities_tc13_2(driver):
    homepage = HomePage(driver)
    homepage.click_infomation()
    homepage.scroll_to_element1("Chặn cuộc gọi rác")
    homepage.click_by_text("Đổi Esim")
    homepage.press_back()
    homepage.click_by_text("Chuyển vùng quốc tế")
    homepage.press_back()
    homepage.click_by_text("5G")
    homepage.press_back()
    homepage.click_by_text("Kích hoạt sim")
    homepage.press_back()
    homepage.click_by_text("Chặn cuộc gọi rác")
    homepage.press_back()
    homepage.click_by_text("Data Lock")
    homepage.press_back()
    homepage.wait_for_result("Tiện ích nổi bật")
    assert homepage.is_result_displayed("Tiện ích nổi bật")

#===ĐĂNG KÝ/HUỶ GÓI CƯỚC/DỊCH VỤ===========
#TC14 - Đăng ký gói cước thành công
@pytest.mark.tc14
def test_register_tc14(driver):
    homepage = HomePage(driver)
    homepage.search_package("D5")
    homepage.wait_for_result("D5")
    homepage.press_back()
    homepage.click_by_text("Chi tiết")
    homepage.click_textview_by_resource_id("vms.com.vn.mymobifone:id/tvRegister") 
    # homepage.click_by_text("Tiếp tục")
    homepage.click_by_text("Xác nhận thanh toán")
    homepage.input_otp("000000")
    homepage.wait_for_result("Đăng ký gói cước thành công")
    assert homepage.is_result_displayed("Đăng ký gói cước thành công")   
#TC15 - Huỷ gói cước thành công
@pytest.mark.tc15
def test_unregister_tc15(driver):
    homepage = HomePage(driver)
    homepage.search_package("D5")
    homepage.wait_for_result("D5")
    homepage.press_back()
    homepage.click_by_text("Chi tiết")
    homepage.click_button_cancel()
    homepage.click_button_continute()
    homepage.input_otp("000000")
    homepage.wait_for_result("Hủy gói cước thành công")
    assert homepage.is_result_displayed("Hủy gói cước thành công")

#TC16 - Đăng ký gói dịch vụ
@pytest.mark.tc16
def test_mobigames_register_tc16(driver):
    homepage = HomePage(driver)
    homepage.search_package("Funring")
    homepage.wait_for_result("Funring")
    homepage.click_by_text("Funring")
    homepage.click_by_text("Đăng ký")
    homepage.click_button_by_resource_id("vms.com.vn.mymobifone:id/btContinue")
    homepage.input_otp("000000")
    homepage.wait_for_result("Đăng ký dịch vụ")
    assert homepage.is_result_displayed("Yêu cầu thành công")
    
#TC17 - Huỷ đăng ký gói dịch vụ
@pytest.mark.tc17
def test_mobigames_unregister_tc17(driver):
    homepage = HomePage(driver)
    homepage.search_package("Funring")
    homepage.wait_for_result("Funring")
    homepage.click_by_text("Funring")
    homepage.click_by_text("Hủy")
    homepage.click_button_by_resource_id("vms.com.vn.mymobifone:id/btContinue")
    homepage.input_otp("000000") 
    homepage.wait_for_result("Hủy gói dịch vụ")
    assert homepage.is_result_displayed("Hủy gói dịch vụ thành công")
#=====GÓI CƯỚC CỦA BẠN=========()
#TC18 - Huỷ gói cước
@pytest.mark.tc18
def test_unregister_my_pakage_tc18(driver):
    homepage = HomePage(driver)
    homepage.click_infomation()
    homepage.scroll_to_element1("Gói cước của bạn")
    homepage.click_textview_by_resource_id("vms.com.vn.mymobifone:id/tvPackageName")
    homepage.click_textview_by_resource_id("vms.com.vn.mymobifone:id/tvCancelPackage")
    homepage.click_button_by_resource_id("vms.com.vn.mymobifone:id/btContinue")
    homepage.input_otp("000000")
    homepage.wait_for_result("Hủy gói cước thành công")
    assert homepage.is_result_displayed("Hủy gói cước thành công")
#TC19 - Gia hạn gói cước
@pytest.mark.tc19
def test_extend_pakage_tc19(driver):
    homepage = HomePage(driver)
    homepage.click_infomation()
    homepage.scroll_to_element("Gói cước của bạn")
    homepage.click_detail_my_pakage()
    homepage.click_button_extend()
    homepage.click_button_confirm_extend()
    homepage.input_otp("000000")
    homepage.wait_for_result("Gia hạn gói cước thành công")
    assert homepage.is_result_displayed("Gia hạn gói cước thành công")
#TC20 - Huỷ gia hạn tự động gói cước
@pytest.mark.tc20
def test_unextend_pakage_tc20(driver):
    homepage = HomePage(driver)
    homepage.click_infomation()
    homepage.scroll_to_element("Thẻ kết nối dài lâu")
    homepage.click_detail_my_pakage()
    homepage.click_button_cancel_extend()
    homepage.click_button_confirm_cancel_extend()
    homepage.input_otp("000000")
    homepage.wait_for_result("Hủy gia hạn gói cước thành công")
    assert homepage.is_result_displayed("Hủy gia hạn gói cước thành công")

#== Hẹn roaming ======
#TC21 - Đổi lịch hẹn roaming
@pytest.mark.tc21
def test_reschedule_tc21(driver):
    homepage = HomePage(driver)
    homepage.click_infomation()
    homepage.scroll_to_element1("Đổi lịch hẹn")
    homepage.click_button_reschedule()
    homepage.et_time("22062026")
    homepage.click_button_submit()
    homepage.input_otp("000000")
    homepage.wait_for_result("Đổi lịch hẹn thành công")
    assert homepage.is_result_displayed("Đổi lịch hẹn thành công")

#TC22 - Huỷ lịch hẹn roaming
@pytest.mark.tc22
def test_cancel_shedule_tc22(driver):
    homepage = HomePage(driver)
    homepage.click_infomation()
    homepage.scroll_to_element1("Đổi lịch hẹn")
    homepage.click_button_cancel_schedule()
    homepage.click_button_submit()
    homepage.input_otp("000000")
    homepage.wait_for_result("Hủy lịch hẹn thành công")
    assert homepage.is_result_displayed("Hủy lịch hẹn thành công")

#TC23 - Click Mua gói
@pytest.mark.tc23
def test_buy_pakage_tc23(driver):
    homepage = HomePage(driver)
    homepage.click_button_buy_pakage()
    homepage.wait_for_result("Tất cả gói cước")
    assert homepage.is_result_displayed("Tất cả gói cước")

#TC24 - Click Thanh toán
@pytest.mark.tc24
def test_recharge_tc24(driver):
    homepage = HomePage(driver)
    homepage.click_recharge()
    homepage.wait_for_result("Thanh toán")
    assert homepage.is_result_displayed("Thanh toán")
    
#TC25 - Đổi số điện thoại con
@pytest.mark.tc25 
def test_change_number_tc25(driver):
    homepage = HomePage(driver)
    homepage.click_menu()
    homepage.add_phone("0762203039")
    # homepage.press_back()
    homepage.click_button_accept()
    homepage.input_otp("888888")
    homepage.close_menu()
    homepage.click_change_number()
    homepage.click_new_number()
    homepage.wait_for_result("0762203039")
    assert homepage.is_result_displayed("0762203039")

#TC26 - Click tiện ích ở ngoài màn trang chủ
@pytest.mark.tc26 
def test_click_utilities_tc26(driver):
    homepage = HomePage(driver)
    homepage.click_icon(1)
    homepage.press_back()
    homepage.click_icon(2)
    homepage.press_back()
    homepage.click_icon(3)
    homepage.press_back()
    homepage.click_icon(4)
    homepage.press_back()
    homepage.wait_for_text("Tiện ích của bạn")
    assert homepage.is_result_displayed("Tiện ích của bạn")
#TC27, TC28 - Click tiện ích ở màn Tất cả tiện ích
@pytest.mark.tc27
def test_click_utilities_tc27(driver):
    homepage = HomePage(driver)
    homepage.click_view_all_utils()
    homepage.click_by_text("Khuyến mãi và quà tặng")
    homepage.press_back()
    homepage.click_by_text("Tri ân Nữ khách hàng cao cấp")
    homepage.press_back()
    homepage.click_by_text("Thanh Toán")
    homepage.press_back()
    homepage.click_by_text("Hỗ trợ nạp thẻ")
    homepage.press_back()
    homepage.click_by_text("Lịch sử gói cước")
    homepage.press_back()
    homepage.wait_for_text("Khuyến mại và Quà tặng")
    assert homepage.is_result_displayed("Khuyến mại và Quà tặng")
#Mục viễn thông
@pytest.mark.tc28
def test_click_utilities_tc28(driver):
    homepage = HomePage(driver)
    homepage.click_view_all_utils()
    homepage.scroll_to_element("Viễn thông")
    homepage.wait_for_text("Viễn thông")
    homepage.click_by_text("Đổi Esim")
    homepage.press_back()
    homepage.click_by_text("Chuyển vùng quốc tế")
    homepage.press_back()
    homepage.click_by_text("5G")
    homepage.press_back()
    homepage.click_by_text("Kích hoạt sim")
    homepage.press_back()
    homepage.click_by_text("Chặn cuộc gọi rác")
    homepage.press_back()
    homepage.click_by_text("Data Lock")
    homepage.press_back()
    homepage.wait_for_text("Tất cả tiện ích")
    assert homepage.is_result_displayed("Tất cả tiện ích")
#Kết nối dài lâu
#TC29 - Click thẻ KNDL
@pytest.mark.tc29
def test_click_card_kndl_tc29(driver):
    homepage = HomePage(driver)
    homepage.scroll_to_element1("Thẻ Kết Nối Dài Lâu")
    homepage.click_card_kndl()
    homepage.wait_for_result("Kết nối dài lâu")
    assert homepage.is_result_displayed("Kết nối dài lâu")
#TC30 - Click dịch vụ nổi bật
@pytest.mark.tc30
def test_click_services_tc30(driver):
    homepage = HomePage(driver)
    homepage.scroll_to_element1("Vietlott SMS")
    homepage.click_by_text("Vietlott SMS")
    homepage.press_back()
    homepage.wait_for_result("Chi tiết dịch vụ")
    assert homepage.is_result_displayed("Chi tiết dịch vụ")    
@pytest.mark.tc31
def test_click_services_tc31(driver):
    homepage = HomePage(driver)
    homepage.scroll_to_element1("Vietlott SMS")
    homepage.click_by_text("MobiSafe")
    homepage.wait_for_result("Chi tiết dịch vụ")
    assert homepage.is_result_displayed("Chi tiết dịch vụ")
@pytest.mark.tc32
def test_click_services_tc32(driver):
    homepage = HomePage(driver)
    homepage.scroll_to_element1("Vietlott SMS")
    homepage.click_by_text("MobiPA")
    homepage.wait_for_result("Chi tiết dịch vụ")
    assert homepage.is_result_displayed("Chi tiết dịch vụ")   
@pytest.mark.tc33
def test_click_servicestc33(driver):
    homepage = HomePage(driver)
    homepage.scroll_to_element1("Vietlott SMS")
    homepage.click_by_text("MobiGames")
    homepage.wait_for_result("Chi tiết dịch vụ")
    assert homepage.is_result_displayed("Chi tiết dịch vụ")
#Hỗ trợ khách hàng
@pytest.mark.tc34
def test_click_customer_support_tc34(driver):
    homepage = HomePage(driver)
    homepage.scroll_to_element1("Thông báo")
    homepage.click_by_text("Chuẩn hoá thông tin")
    homepage.wait_for_result("Chuẩn hoá thông tin")
    assert homepage.is_result_displayed("Chuẩn hoá thông tin")
@pytest.mark.tc35
def test_click_customer_support_tc35(driver):
    homepage = HomePage(driver)
    homepage.scroll_to_element1("Thông báo")
    homepage.click_by_text("Hòa mạng")
    homepage.wait_for_result("Hòa mạng")
    assert homepage.is_result_displayed("Hòa mạng")
@pytest.mark.tc36
def test_click_customer_support_tc36(driver):
    homepage = HomePage(driver)
    homepage.scroll_to_element1("Thông báo")
    homepage.click_by_text("Phản ánh khách hàng")
    homepage.wait_for_result("MobiFone")
    assert homepage.is_result_displayed("MobiFone")
@pytest.mark.tc37
def test_click_customer_support_tc37(driver):
    homepage = HomePage(driver)
    homepage.scroll_to_element1("Thông báo")
    homepage.click_by_text("Zalo miniApp")
    homepage.wait_for_result("Đăng nhập")
    assert homepage.is_result_displayed("Đăng nhập")
#TC38 - Click vào từng banner
@pytest.mark.tc38
def test_click_banner_tc38(driver):
    homepage = HomePage(driver)
    homepage.scroll_to_element1("Hỗ trợ khách hàng")
    homepage.click_banner()
    homepage.wait_for_result("KHÁM PHÁ")
    assert homepage.is_result_displayed("KHÁM PHÁ")
@pytest.mark.tc39
def test_click_banner_tc39(driver):
    homepage = HomePage(driver)
    homepage.scroll_to_element1("Hỗ trợ khách hàng")
    homepage.swipe_banner(1)
    homepage.click_banner()
    homepage.wait_for_result("Mobifone")
    assert homepage.is_result_displayed("Mobifone")
@pytest.mark.tc39_1   
def test_click_banner_tc39_1(driver):
    homepage = HomePage(driver)
    homepage.scroll_to_element1("Hỗ trợ khách hàng")
    homepage.swipe_banner(2)
    homepage.click_banner()
    homepage.wait_for_result("Chi tiết dịch vụ")
    assert homepage.is_result_displayed("Chi tiết dịch vụ")
@pytest.mark.tc39_3   
def test_click_banner_tc39_3(driver):
    homepage = HomePage(driver)
    homepage.scroll_to_element1("Hỗ trợ khách hàng")
    homepage.swipe_banner(3)
    homepage.click_banner()
    homepage.wait_for_result("Hỗ trợ khách hàng")
    assert homepage.is_result_displayed("Hỗ trợ khách hàng")
@pytest.mark.tc39_4
def test_click_banner_tc39_4(driver):
    homepage = HomePage(driver)
    homepage.scroll_to_element1("Hỗ trợ khách hàng")
    homepage.swipe_banner(4)
    homepage.click_banner()
    homepage.wait_for_result("Hỗ trợ khách hàng")
    assert homepage.is_result_displayed("Hỗ trợ khách hàng")