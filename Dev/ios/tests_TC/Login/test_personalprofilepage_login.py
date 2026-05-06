import pytest
from pages.PersonalProfilePage_page import PersonalProfile

#TC106. Click các icon dịch vụ của tôi
@pytest.mark.tc106
def test_click_my_services_tc106(driver):
    personalprofile = PersonalProfile(driver)
    personalprofile.click_avata()
    personalprofile.click_by_image("ic_tttb")
    personalprofile.wait_for_result("Thông tin thuê bao")
    personalprofile.click_button_by_text("icBack")
    personalprofile.click_by_image("ic_lstt")
    personalprofile.wait_for_result("Lịch sử thanh toán")
    personalprofile.click_by_text1("arrow left")
    personalprofile.click_by_image("ic_dktt")
    personalprofile.wait_for_result("Đăng ký thông tin")
    personalprofile.click_by_text1("icBack")
    personalprofile.click_by_image("ic_tc")
    personalprofile.wait_for_result("hạn mức cước")
    personalprofile.click_button_by_text("icBack")
    personalprofile.click_by_image("ic_multisim")
    personalprofile.wait_for_result("Multi-SIM")
    personalprofile.click_button_by_text("icBack")
    personalprofile.click_by_image("ic_doiesim")
    personalprofile.wait_for_result("Chuyển đổi eSIM")
    personalprofile.click_button_by_text("icBack")
    personalprofile.click_by_image("ic_autopoay")
    personalprofile.wait_for_result("thanh toán")
    personalprofile.click_button_by_text("icBack")
    personalprofile.click_by_image("ic_cd")
    personalprofile.wait_for_result("Cài đặt")
    personalprofile.click_button_by_text("icBack")
    personalprofile.click_by_image("ic_kmqt")
    personalprofile.wait_for_result("Khuyến mãi")
    personalprofile.click_button_by_text("icBack")
    personalprofile.click_by_image("ic_ccgr")
    personalprofile.click_button_by_text("icBack")
    personalprofile.click_by_image("ic_hm")
    personalprofile.click_button_by_text("icBack")
    personalprofile.click_by_image("ic_qrcode")
    personalprofile.click_button_by_text("qrcode scan btn myqrcode nor")
    personalprofile.click_by_image("ic_cm")
    personalprofile.click_button_by_text("icBack")
    personalprofile.click_by_image("ic_C2C")
    personalprofile.click_button_by_text("icBack")
    personalprofile.click_by_image("ic_lsnt")
    personalprofile.click_button_by_text("arrow left")
    personalprofile.click_by_image("ic_data")
    personalprofile.click_button_by_text("arrow left")
    personalprofile.click_by_image("ic_ggch")
    personalprofile.click_button_by_text("icBack")
    assert personalprofile.is_result_displayed("Tiện ích của bạn")
#TC107. Click button refesh trong thông tin thuê bao
@pytest.mark.tc107
def test_click_button_refesh_tc107(driver):
    personalprofile = PersonalProfile(driver)
    personalprofile.click_avata()
    personalprofile.click_by_image("ic_tttb")
    personalprofile.click_button_by_text("icon refresh")
    assert personalprofile.is_result_displayed("Thông tin thuê bao")
#TC108. Click button Xem chi tiết
@pytest.mark.tc108
def test_click_button_detail(driver):
    personalprofile = PersonalProfile(driver)
    personalprofile.click_avata()
    personalprofile.click_by_image("ic_tttb")
    personalprofile.click_button_by_text("Xem chi tiết")
    personalprofile.wait_for_result("Xác thực thông tin")
    assert personalprofile.is_result_displayed("Xác thực thông tin")

#TC109. Liên kết với tài khoản google
@pytest.mark.tc109
def test_link_google_tc109(driver):
    personalprofile = PersonalProfile(driver)
    personalprofile.click_avata()
    personalprofile.click_by_image("ic_tttb")
    personalprofile.scroll_to_element2("Liên kết Google")
    personalprofile.click_by_text("Liên kết Google")
    personalprofile.wait_for_result("Xác thực thông tin")
    assert personalprofile.is_result_displayed("Xác thực thông tin")
#TC110. Click xoá tài khoản
@pytest.mark.tc110
def test_click_button_delete_account_tc110(driver):
    personalprofile = PersonalProfile(driver)
    personalprofile.click_avata()
    personalprofile.click_by_image("ic_tttb")
    personalprofile.scroll_to_element2("Xoá tài khoản")
    personalprofile.click_by_text("Xoá tài khoản")
    personalprofile.wait_for_result("Đồng ý")
    assert personalprofile.is_result_displayed("Đồng ý")
#Lịch sử thanh toán
#TC111. Click xem chi tiết 1 giao dịch 
@pytest.mark.tc111
def test_click_button_delete_account_tc111(driver):
    personalprofile = PersonalProfile(driver)
    personalprofile.click_avata()
    personalprofile.click_by_image("ic_lstt")
    personalprofile.wait_for_result("Lịch sử")
    assert personalprofile.is_result_displayed("Lịch sử")

#TC112. Kiểm tra tab hoá đơn điện tử trong lịch sử thanh toán 
@pytest.mark.tc112
def test_check_tab_invoice_tc112(driver):
    personalprofile = PersonalProfile(driver)
    personalprofile.click_avata()
    personalprofile.click_by_image("ic_lstt")
    personalprofile.click_by_text("Hoá đơn điện tử")
    # personalprofile.click_by_image("calendar")
    # personalprofile.select_date(22, 3, 2025)
    # personalprofile.click_button_ok()
    personalprofile.click_by_text("Xem hoá đơn")
    personalprofile.click_by_text("Xem hoá đơn")
    personalprofile.wait_for_result("Lịch sử")
    assert personalprofile.is_result_displayed("Lịch sử")
#TC113. Kiểm tra lọc tháng trong lịch sử thanh toán 
@pytest.mark.tc113
def test_check_tab_invoice_tc113(driver):
    personalprofile = PersonalProfile(driver)
    personalprofile.click_avata()
    personalprofile.click_by_image("ic_lstt")
    personalprofile.click_button_by_text("calendar")
    personalprofile.click_button_by_text("Lọc")
    personalprofile.wait_for_result("Giao dịch trong tháng")
    assert personalprofile.is_result_displayed("Giao dịch trong tháng")

#TC114. Kiểm tra cập nhật thông tin 
@pytest.mark.tc114
def test_update_infor_tc114(driver):
    personalprofile = PersonalProfile(driver)
    personalprofile.click_avata()
    personalprofile.click_by_image("ic_dktt")
    personalprofile.wait_for_result("chuẩn hóa thông tin")
    assert personalprofile.is_result_displayed("chuẩn hóa thông tin")

#TC115. Kiểm tra hạn mức cước
@pytest.mark.tc115
def test_limit_cuoc_tc115(driver):
    personalprofile = PersonalProfile(driver)
    personalprofile.click_avata()
    personalprofile.click_by_image("ic_tc")
    personalprofile.wait_for_result("Các hạn mức cước")
    assert personalprofile.is_result_displayed("Các hạn mức cước")

#TC116. Kiểm tra Multi-sim
@pytest.mark.tc116
def test_ckeck_multi_sim_tc116(driver):
    personalprofile = PersonalProfile(driver)
    personalprofile.click_avata()
    personalprofile.click_by_image("ic_multisim")
    personalprofile.wait_for_result("Số thuê bao")
    assert personalprofile.is_result_displayed("Số thuê bao")
#TC117. Kiểm tra đổi e-sim
@pytest.mark.tc117
def test_change_esim_tc117(driver):
    personalprofile = PersonalProfile(driver)
    personalprofile.click_avata()
    personalprofile.click_by_image("ic_doiesim")
    personalprofile.wait_for_result("Chuyển đổi eSIM")
    assert personalprofile.is_result_displayed("Chuyển đổi eSIM")
#TC118. Kiểm tra auto-pay
@pytest.mark.tc118
def test_check_autopay_tc118(driver):
    personalprofile = PersonalProfile(driver)
    personalprofile.click_avata()
    personalprofile.click_by_image("ic_autopoay")
    personalprofile.click_by_text("Thêm thuê bao")
    personalprofile.click_by_text("THÊM")
    personalprofile.wait_for_result("Thêm thẻ thanh toán")
    assert personalprofile.is_result_displayed("Thêm thẻ thanh toán")

#TC119. Kiểm tra cài đặt
#. Đổi ngôn ngữ
@pytest.mark.tc119
def test_check_setting_tc119(driver):
    personalprofile = PersonalProfile(driver)
    personalprofile.click_avata()
    personalprofile.click_by_image("ic_cd")
    personalprofile.click_button_by_text("language vi")
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
    personalprofile.click_by_image("ic_cd")
    personalprofile.click_button_by_text("language vi")
    # personalprofile.wait_for_result("Usage information")
    # assert personalprofile.is_result_displayed("Usage information")
    texts = ["Thông tin sử dụng", "Usage information"]
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
    personalprofile.click_by_image("ic_cd")
    personalprofile.click_on_switch_notification()
    personalprofile.click_off_switch_notification()
    personalprofile.wait_for_result("Cài đặt")
    assert personalprofile.is_result_displayed("Cài đặt")
#Kích hoạt smart otp
@pytest.mark.tc121
def test_switch_smart_otp_tc121(driver):
    personalprofile = PersonalProfile(driver)
    personalprofile.click_avata()
    personalprofile.click_by_image("ic_cd")
    personalprofile.click_by_text("Smart OTP")
    personalprofile.click_switch_smart_otp()
    personalprofile.input_smart_otp("0000")
    personalprofile.click_button_by_text("Done")
    personalprofile.click_button_by_text("Xác nhận")
    personalprofile.input_otp("000000")
    personalprofile.wait_for_result("Smart OTP")
    assert personalprofile.is_result_displayed("Smart OTP")
#TC122. Kiểm tra khuyến mãi và quà tặng
@pytest.mark.tc122
def test_deals_and_gifts_tc122(driver):
    personalprofile = PersonalProfile(driver)
    personalprofile.click_avata()
    personalprofile.click_by_image("ic_kmqt")
    personalprofile.click_by_text("Quà sinh nhật")
    personalprofile.wait_for_result("Danh sách quà tặng")
    personalprofile.click_button_by_text("icBack")
    personalprofile.click_by_text("Quà tặng MobiFone")
    personalprofile.wait_for_result("Quà tặng MobiFone")
    personalprofile.click_by_text1("icBack")
    personalprofile.wait_for_result("Khuyến mãi và quà tặng")
    assert personalprofile.is_result_displayed("Khuyến mãi và quà tặng")

#TC123. Kiểm tra on/off chặn cuộc gọi rác
@pytest.mark.tc123
def test_block_call_tc123(driver):
    personalprofile = PersonalProfile(driver)
    personalprofile.click_avata()
    personalprofile.click_by_image("ic_ccgr")
    personalprofile.click_on_switch_spam()
    personalprofile.click_on_switch_block()
    personalprofile.click_off_switch_spam()
    personalprofile.click_off_switch_block()
    personalprofile.wait_for_result("Chặn cuộc gọi rác")
    assert personalprofile.is_result_displayed("Chặn cuộc gọi rác")
    
#TC124. Kiểm tra giao dịch tại cửa hàng
@pytest.mark.tc124
def test_block_call_tc124(driver):
    personalprofile = PersonalProfile(driver)
    personalprofile.click_avata()
    personalprofile.click_by_image("ic_ggch")
    personalprofile.wait_for_result("Chức năng này")
    assert personalprofile.is_result_displayed("Chức năng này")
#TC125. Kiểm tra lịch sử gói cước
@pytest.mark.tc125
def test_history_pakage_tc125(driver):
    personalprofile = PersonalProfile(driver)
    personalprofile.click_avata()
    personalprofile.click_by_image("ic_lsnt")
    personalprofile.click_button_by_text("Chi tiết", 1)
    personalprofile.click_by_image("icon_close")
    personalprofile.click_by_text("Giới thiệu")
    personalprofile.wait_for_result("Giao dịch trong tháng")
    assert personalprofile.is_result_displayed("Giao dịch trong tháng")
#TC126. Kiểm tra lịch sử lịch sử data
@pytest.mark.tc126
def test_history_pakage_tc126(driver):
    personalprofile = PersonalProfile(driver)
    personalprofile.click_avata()
    personalprofile.click_by_image("ic_data")
    personalprofile.wait_for_result("Lịch sử chuyển data")
    assert personalprofile.is_result_displayed("Lịch sử chuyển data")