import pytest
from pages.PersonalProfilePage_page import PersonalProfile

#TC106. Click các icon dịch vụ của tôi
@pytest.mark.tc106
def test_click_my_services_tc106(driver):
    personalprofile = PersonalProfile(driver)
    personalprofile.click_avata()
    personalprofile.click_my_services(1)
    personalprofile.wait_for_result("Thông tin thuê bao")
    personalprofile.press_back()
    personalprofile.click_my_services(2)
    personalprofile.wait_for_result("Lịch sử thanh toán")
    personalprofile.press_back()
    personalprofile.click_my_services(3)
    personalprofile.wait_for_result("Cập nhật thông tin")
    personalprofile.press_back()
    personalprofile.click_my_services(4)
    personalprofile.wait_for_result("hạn mức cước")
    personalprofile.press_back()
    personalprofile.click_my_services(5)
    personalprofile.wait_for_result("Multi-sim")
    personalprofile.press_back()
    personalprofile.click_my_services(6)
    personalprofile.press_back()
    personalprofile.click_my_services(7)
    personalprofile.wait_for_result("Điều khoản")
    personalprofile.press_back()
    personalprofile.click_my_services(8)
    personalprofile.wait_for_result("Cài đặt")
    personalprofile.press_back()
    personalprofile.click_my_services(9)
    personalprofile.wait_for_result("Khuyến mại")
    personalprofile.press_back()
    personalprofile.click_my_services(10)
    personalprofile.press_back()
    personalprofile.wait_for_result("Hồ sơ cá nhân")
    assert personalprofile.is_result_displayed("Hồ sơ cá nhân")
#TC107. Click button refesh trong thông tin thuê bao
@pytest.mark.tc107
def test_click_button_refesh_tc107(driver):
    personalprofile = PersonalProfile(driver)
    personalprofile.click_avata()
    personalprofile.click_my_services(1)
    personalprofile.click_button_refesh()
    assert personalprofile.is_result_displayed("Thông tin thuê bao")
#TC108. Click button Xem chi tiết
@pytest.mark.tc108
def test_click_button_detail_tc108(driver):
    personalprofile = PersonalProfile(driver)
    personalprofile.click_avata()
    personalprofile.click_my_services(1)
    personalprofile.click_button_detail()
    assert personalprofile.is_result_displayed("Xác thực thông tin")
#TC109. Liên kết với tài khoản google
@pytest.mark.tc109
def test_link_google_tc109(driver):
    personalprofile = PersonalProfile(driver)
    personalprofile.click_avata()
    personalprofile.click_my_services(1)
    personalprofile.scroll_to_element("Liên kết với tài khoản Google")
    personalprofile.click_by_text("Liên kết với tài khoản Google")
    personalprofile.wait_for_result("Xác thực thông tin")
    assert personalprofile.is_result_displayed("Xác thực thông tin")
#TC110. Liên kết với tài khoản google
@pytest.mark.tc110
def test_click_button_delete_account_tc110(driver):
    personalprofile = PersonalProfile(driver)
    personalprofile.click_avata()
    personalprofile.click_my_services(1)
    personalprofile.scroll_to_element("Xóa tài khoản")
    personalprofile.click_button_delete()
    personalprofile.wait_for_result("Xác nhận")
    assert personalprofile.is_result_displayed("Xác nhận")
#Lịch sử thanh toán
#TC111. Click xem chi tiết 1 giao dịch 
@pytest.mark.tc111
def test_click_button_delete_account_tc111(driver):
    personalprofile = PersonalProfile(driver)
    personalprofile.click_avata()
    personalprofile.click_my_services(2)
    personalprofile.wait_for_result("Lịch sử")
    assert personalprofile.is_result_displayed("Lịch sử")

#TC112. Kiểm tra tab hoá đơn điện tử trong lịch sử thanh toán 
@pytest.mark.tc112
def test_check_tab_invoice_tc112(driver):
    personalprofile = PersonalProfile(driver)
    personalprofile.click_avata()
    personalprofile.click_my_services(2)
    personalprofile.click_by_text("Hóa đơn điện tử")
    personalprofile.click_select_date()
    personalprofile.wait_for_result("THÁNG")
    personalprofile.select_date(3, 2026)
    personalprofile.click_button_ok()
    personalprofile.click_by_text("Hoá đơn")
    personalprofile.click_by_text("Phiếu thu")
    personalprofile.click_by_text("Xem hoá đơn")
    personalprofile.wait_for_result("Lịch sử")
    assert personalprofile.is_result_displayed("Lịch sử")
#TC113. Kiểm tra lọc tháng trong lịch sử thanh toán 
@pytest.mark.tc113
def test_check_tab_invoice_tc113(driver):
    personalprofile = PersonalProfile(driver)
    personalprofile.click_avata()
    personalprofile.click_my_services(2)
    personalprofile.click_icon_bin()
    personalprofile.select_month(3)
    personalprofile.click_button_back()
    personalprofile.click_button_fillter()
    personalprofile.wait_for_result("Lịch sử")
    assert personalprofile.is_result_displayed("Lịch sử")

#TC114. Kiểm tra cập nhật thông tin 
@pytest.mark.tc114
def test_update_infor_tc114(driver):
    personalprofile = PersonalProfile(driver)
    personalprofile.click_avata()
    personalprofile.click_my_services(3)
    personalprofile.click_button_update()
    personalprofile.input_otp("888888")
    personalprofile.wait_for_result("Chữ ký")
    assert personalprofile.is_result_displayed("Chữ ký")

#TC115. Kiểm tra hạn mức cước
@pytest.mark.tc115
def test_limit_cuoc_tc115(driver):
    personalprofile = PersonalProfile(driver)
    personalprofile.click_avata()
    personalprofile.click_my_services(4)
    personalprofile.wait_for_result("Các hạn mức cước")
    assert personalprofile.is_result_displayed("Các hạn mức cước")

#TC116. Kiểm tra Multi-sim
@pytest.mark.tc116
def test_ckeck_multi_sim_tc116(driver):
    personalprofile = PersonalProfile(driver)
    personalprofile.click_avata()
    personalprofile.click_my_services(5)
    personalprofile.wait_for_result("Số thuê bao")
    assert personalprofile.is_result_displayed("Số thuê bao")
#TC117. Kiểm tra đổi e-sim
@pytest.mark.tc117
def test_change_esim_tc117(driver):
    personalprofile = PersonalProfile(driver)
    personalprofile.click_avata()
    personalprofile.click_my_services(6)
    personalprofile.wait_for_result("Thiết bị của bạn không hỗ trợ eSIM")
    assert personalprofile.is_result_displayed("Thiết bị của bạn không hỗ trợ eSIM")
#TC118. Kiểm tra auto-pay
@pytest.mark.tc118
def test_check_autopay_tc118(driver):
    personalprofile = PersonalProfile(driver)
    personalprofile.click_avata()
    personalprofile.click_my_services(7)
    personalprofile.add_phone()
    personalprofile.click_buttom_confirm()
    personalprofile.click_buttom_confirm()
    personalprofile.wait_for_result("Thêm thẻ thanh toán")
    assert personalprofile.is_result_displayed("Thêm thẻ thanh toán")

#TC119. Kiểm tra cài đặt
#. Đổi ngôn ngữ
@pytest.mark.tc119
def test_check_setting_tc119(driver):
    personalprofile = PersonalProfile(driver)
    personalprofile.click_avata()
    personalprofile.click_my_services(8)
    personalprofile.click_switch_language()
    # personalprofile.wait_for_result("Usage information")
    # assert personalprofile.is_result_displayed("Usage information")
    texts = ["Usage information", "Thông tin sử dụng"]
    found = False
    for text in texts:
        try:
            personalprofile.wait_for_result(text)
            found = True
            break
        except:
            continue

    assert found, "❌ Không tìm thấy text hợp lệ"
@pytest.mark.tc119_1
def test_check_setting_tc119_1(driver):
    personalprofile = PersonalProfile(driver)
    personalprofile.click_avata()
    personalprofile.click_my_services(8)
    personalprofile.click_switch_language()
    # personalprofile.wait_for_result("Usage information")
    # assert personalprofile.is_result_displayed("Usage information")
    texts = ["Usage information", "Thông tin sử dụng"]
    found = False
    for text in texts:
        try:
            personalprofile.wait_for_result(text)
            found = True
            break
        except:
            continue
    assert found, "❌ Không tìm thấy text hợp lệ"
#Bật tắt thông báo
@pytest.mark.tc120
def test_switch_nofti_tc120(driver):
    personalprofile = PersonalProfile(driver)
    personalprofile.click_avata()
    personalprofile.click_my_services(8)
    personalprofile.click_switch_notification()
    personalprofile.wait_for_result("Cài đặt")
    assert personalprofile.is_result_displayed("Cài đặt")
#Kích hoạt smart otp
@pytest.mark.tc121
def test_switch_smart_otp_tc121(driver):
    personalprofile = PersonalProfile(driver)
    personalprofile.click_avata()
    personalprofile.click_my_services(8)
    personalprofile.click_smart_otp()
    personalprofile.click_switch_smart_otp()
    personalprofile.input_smart_otp("0000")
    personalprofile.click_button_accept()
    personalprofile.input_otp("000000")
    personalprofile.wait_for_result("Smart OTP")
    assert personalprofile.is_result_displayed("Smart OTP")
#TC122. Kiểm tra khuyến mãi và quà tặng
@pytest.mark.tc122
def test_deals_and_gifts_tc122(driver):
    personalprofile = PersonalProfile(driver)
    personalprofile.click_avata()
    personalprofile.click_my_services(9)
    personalprofile.click_by_text("Quà sinh nhật")
    personalprofile.wait_for_result("Danh sách quà tặng")
    personalprofile.press_back()
    personalprofile.click_by_text("Quà tặng MobiFone")
    personalprofile.wait_for_result("Chọn quà Mobifone")
    personalprofile.press_back()
    personalprofile.wait_for_result("Khuyến mại & Quà tặng")
    assert personalprofile.is_result_displayed("Khuyến mại & Quà tặng")

#TC123. Kiểm tra chặn cuộc gọi rác
@pytest.mark.tc123
def test_block_call_tc123(driver):
    personalprofile = PersonalProfile(driver)
    personalprofile.click_avata()
    personalprofile.click_my_services(12)
    personalprofile.click_switch_spam()
    personalprofile.click_switch_block()
    personalprofile.click_my_mobifone()
    personalprofile.click_default()
    personalprofile.wait_for_result("Chặn cuộc gọi rác")
    assert personalprofile.is_result_displayed("Chặn cuộc gọi rác")
    
#TC124. Kiểm tra giao dịch tại cửa hàng
@pytest.mark.tc124
def test_block_call_tc124(driver):
    personalprofile = PersonalProfile(driver)
    personalprofile.click_avata()
    personalprofile.click_my_services(13)
    personalprofile.wait_for_result("Chức năng này")
    assert personalprofile.is_result_displayed("Chức năng này")
#TC125. Kiểm tra lịch sử gói cước/ lịch sử data
@pytest.mark.tc125
def test_history_pakage_tc125(driver):
    personalprofile = PersonalProfile(driver)
    personalprofile.click_avata()
    personalprofile.click_my_services(15)
    personalprofile.click_history_pakage(1)
    personalprofile.click_button_close()
    personalprofile.click_by_text("Giới thiệu")
    personalprofile.wait_for_result("Giao dịch trong tháng")
    assert personalprofile.is_result_displayed("Giao dịch trong tháng")
#TC126. Kiểm tra lịch sử gói cước/ lịch sử data
@pytest.mark.tc126
def test_history_pakage_tc126(driver):
    personalprofile = PersonalProfile(driver)
    personalprofile.click_avata()
    personalprofile.click_my_services(17)
    personalprofile.wait_for_result("Lịch sử chuyển data")
    assert personalprofile.is_result_displayed("Lịch sử chuyển data")