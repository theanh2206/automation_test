import pytest
from selenium.webdriver.support import expected_conditions as EC
from pages.BuyPakagePage_page import BuyPakagePage
from pages.BasePage_page import BasePage

#Tìm kiếm gói cước/ dịch vụ bất kỳ trên thanh tìm kiếm
#TC40. Tìm kiếm gói cước tồn tại trong db
@pytest.mark.tc40
def test_search_package_tc40(driver):
    buypakage = BuyPakagePage(driver)
    buypakage.click_buy_pakage()
    buypakage.search_package("D5")
    buypakage.wait_for_result("Gói Data ngày D5")
    assert buypakage.is_result_displayed("Gói Data ngày D5")
#TC41. Tìm kiếm gói cước không tồn tại trong db
@pytest.mark.tc41
def test_search_package_tc41(driver):
    buypakage = BuyPakagePage(driver)
    buypakage.click_buy_pakage()
    buypakage.search_package("Thế Anh")
    buypakage.wait_for_result("Không có dữ liệu")
    assert buypakage.is_result_displayed("Không có dữ liệu")
#TC43. Tìm kiếm dịch vụ tồn tại trong db
@pytest.mark.tc43
def test_search_services_tc43(driver):
    buypakage = BuyPakagePage(driver)
    buypakage.click_buy_pakage()
    buypakage.search_package("MobiGames")
    buypakage.wait_for_result("MobiGames")
    assert buypakage.is_result_displayed("MobiGames")
#TC44. Tìm kiếm gói cước không tồn tại trong db
@pytest.mark.tc44
def test_search_services_tc44(driver):
    buypakage = BuyPakagePage(driver)
    buypakage.click_buy_pakage()
    buypakage.search_package("Thế Anh")
    buypakage.wait_for_result("Không có dữ liệu")
    assert buypakage.is_result_displayed("Không có dữ liệu")
#TC45. Đăng ký gói cước ở thanh tìm kiếm
@pytest.mark.tc45
def test_register_pakage_search_tc45(driver):
    buypakage = BuyPakagePage(driver)
    buypakage.click_buy_pakage()
    buypakage.search_package("D5")
    buypakage.wait_for_result("D5")
    buypakage.click_by_text("Gói Data ngày D5")
    buypakage.click_by_text("Đăng ký ngay")
    buypakage.click_button_by_text("Tiếp tục")
    buypakage.click_button_by_text("Xác nhận thanh toán")
    buypakage.input_otp("000000")
    buypakage.wait_for_result("Đăng ký gói cước thành công")
    assert buypakage.is_result_displayed("Đăng ký gói cước thành công")
#TC46. Huỷ gói cước ở thanh tìm kiếm
@pytest.mark.tc46
def test_unregister_pakage_search_tc46(driver):
    buypakage = BuyPakagePage(driver)
    buypakage.click_buy_pakage()
    buypakage.search_package("D5")
    buypakage.wait_for_result("D5")
    buypakage.click_by_text("Gói Data ngày D5")
    buypakage.click_button_by_text("Huỷ")
    buypakage.click_button_by_text("Đồng ý")
    buypakage.input_otp("000000")
    buypakage.wait_for_result("Huỷ thành công")
    assert buypakage.is_result_displayed("Huỷ thành công")
#TC47. Tạo gói cước cá nhân
#1. Đăng ký bằng OTP
@pytest.mark.tc47
def test_create_pakage_OTP_tc47(driver):
    buypakage = BuyPakagePage(driver)
    buypakage.click_buy_pakage()
    buypakage.click_personal_flex()
    buypakage.wait_for_result("Tạo gói cước ")
    buypakage.click_button_by_text("Tạo gói cước ")
    buypakage.click_by_text("Huỷ")
    # buypakage.input_otp("000000")
    buypakage.wait_for_result("Đăng ký gói cước")
    assert buypakage.is_result_displayed("Đăng ký gói cước")
#2. Đăng ký bằng mã pin
# @pytest.mark.tc47_1
# def test_create_pakage_PIN(driver):
#     buypakage = BuyPakagePage(driver)
#     buypakage.click_buy_pakage()
#     buypakage.click_personal_flex()
#     buypakage.click_button_create_pakage()
#     buypakage.click_payment_confirm()
#     buypakage.input_otp("0000")
#     buypakage.click_button_accept()
#     buypakage.wait_for_result("Đăng ký gói cước thành công")
#     assert buypakage.is_result_displayed("Đăng ký gói cước thành công")
#3. Huỷ gói cước cá nhân
# @pytest.mark.tc47_2
# def test_cancel_pakage_PIN(driver):
#     buypakage = BuyPakagePage(driver)
#     buypakage.click_buy_pakage()
#     buypakage.click_personal_flex()
#     buypakage.click_button_create_pakage()
#     buypakage.click_button_cancel()
#     buypakage.click_button_continute()
#     buypakage.input_otp("888888")
#     buypakage.click_button_accept()
#     buypakage.wait_for_result("Huỷ gói cước thành công")
#     assert buypakage.is_result_displayed("Huỷ gói cước thành công")

#TC48. Tạo gói cước linh hoạt thời gian
#1. Đăng ký bằng OTP
@pytest.mark.tc48
def test_create_pakage_flex_OTP_tc48(driver):
    buypakage = BuyPakagePage(driver)
    buypakage.click_buy_pakage()
    buypakage.click_time_flex()
    buypakage.click_button_by_text("Đăng ký", 3)
    buypakage.click_button_by_text("Đăng ký ngay")
    buypakage.click_button_by_text("Xác nhận thanh toán")
    buypakage.input_otp("000000")
    buypakage.wait_for_result("Đăng ký gói cước thành công")
    assert buypakage.is_result_displayed("Đăng ký gói cước thành công")
#2. Đăng ký bằng mã PIN
# @pytest.mark.tc48_1
# def test_create_pakage_flex_PIN(driver):
#     buypakage = BuyPakagePage(driver)
#     buypakage.click_buy_pakage()
#     buypakage.click_time_flex()
#     buypakage.click_register_button2()
#     buypakage.click_payment_confirm()
#     buypakage.input_otp("0000")
#     buypakage.click_button_accept()
#     buypakage.wait_for_result("Đăng ký gói cước thành công")
#     assert buypakage.is_result_displayed("Đăng ký gói cước thành công")
#3. Huỷ gói cước linh hoạt
# @pytest.mark.tc48_2
# def test_cancel_pakage_flex(driver):
#     buypakage = BuyPakagePage(driver)
#     buypakage.click_buy_pakage()
#     buypakage.click_time_flex()
#     buypakage.click_register_button2()
#     buypakage.click_button_cancel()
#     buypakage.click_button_continute()
#     buypakage.input_otp("888888")
#     buypakage.wait_for_result("Huỷ gói cước thành công")
#     assert buypakage.is_result_displayed("Huỷ gói cước thành công")
    
#TC49. Tìm kiếm gói bằng gói cước/quốc gia
@pytest.mark.tc49
def test_find_pakage_tc49(driver):
    buypakage = BuyPakagePage(driver)
    buypakage.click_buy_pakage()
    buypakage.click_icon_cvqt()
    buypakage.click_search_country()
    buypakage.send_key_country("Japan")
    buypakage.wait_for_result("Nhật Bản")
    buypakage.click_by_text("Japan (Nhật Bản)")
    buypakage.click_by_text("Áp dụng")
    buypakage.wait_for_result("Tạo gói cước data roaming linh hoạt")
    assert buypakage.is_result_displayed("Tạo gói cước data roaming linh hoạt")
    
#TC50. Click kiểm tra cước chuyến đi
@pytest.mark.tc50
def test_click_check_tc50(driver):
    buypakage = BuyPakagePage(driver)
    buypakage.click_buy_pakage()
    buypakage.click_icon_cvqt()
    buypakage.click_check_trip()
    buypakage.wait_for_result("Bật dịch vụ CVQT")
    assert buypakage.is_result_displayed("Bật dịch vụ CVQT")
    
#TC51. Click gói cước quốc tế phổ biến
@pytest.mark.tc51
def test_popular_country_tc51(driver):
    buypakage = BuyPakagePage(driver)
    buypakage.click_buy_pakage()
    buypakage.click_icon_cvqt()
    buypakage.click_popular_country(1)
    buypakage.click_close()
    buypakage.click_popular_country(2)
    buypakage.click_close()
    buypakage.click_popular_country(3)
    buypakage.click_close()
    buypakage.click_popular_country(4)
    buypakage.click_close()
    buypakage.click_popular_country(5)
    buypakage.click_close()
    buypakage.click_popular_country(6)
    buypakage.click_close()
    buypakage.wait_for_result("Gói cước quốc tế phổ biến")
    assert buypakage.is_result_displayed("Gói cước quốc tế phổ biến")
    
#TC52. Đăng ký tạo gói cước data roaming linh hoạt
#1. Đăng ký gói roaming
@pytest.mark.tc52
def test_create_pakage_roaming_tc52(driver):
    buypakage = BuyPakagePage(driver)
    buypakage.click_buy_pakage()
    buypakage.click_icon_cvqt()
    buypakage.click_by_text("Tạo gói cước data roaming linh hoạt")
    buypakage.scroll_to_element2("Chi tiết")
    buypakage.click_button_by_text("Đăng ký")
    buypakage.click_button_by_text("Đăng ký ngay")
    buypakage.click_button_by_text("Xác nhận thanh toán")
    buypakage.input_otp("000000")
    buypakage.wait_for_result("Đăng ký gói cước thành công")
    assert buypakage.is_result_displayed("Đăng ký gói cước thành công")
#2. Đăng ký gói xung đột
@pytest.mark.tc52_1
def test_create_pakage_roaming_tc52_1(driver):
    buypakage = BuyPakagePage(driver)
    buypakage.click_buy_pakage()
    buypakage.click_icon_cvqt()
    buypakage.click_by_text("Tạo gói cước data roaming linh hoạt")
    buypakage.scroll_to_element2("Chi tiết")
    buypakage.click_button_by_text("Đăng ký")
    buypakage.click_button_by_text("Đăng ký ngay")
    buypakage.click_button_by_text("Xác nhận thanh toán")
    buypakage.input_otp("000000")
    buypakage.wait_for_result("Đăng ký gói cước thất bại")
    assert buypakage.is_result_displayed("Đăng ký gói cước thất bại")
    
#TC53. Huỷ gói cước data roaming linh hoạt
@pytest.mark.tc53
def test_cancel_pakage_roaming_tc53(driver):
    buypakage = BuyPakagePage(driver)
    buypakage.click_buy_pakage()
    buypakage.click_icon_cvqt()
    buypakage.click_by_text("Tạo gói cước data roaming linh hoạt")
    buypakage.scroll_to_element2("Chi tiết")
    buypakage.click_button_by_text("Đăng ký")
    buypakage.click_button_by_text("Huỷ")
    buypakage.click_button_by_text("Đồng ý")
    buypakage.input_otp("000000")
    buypakage.wait_for_result("Huỷ thành công")
    assert buypakage.is_result_displayed("Huỷ thành công")

#TC54. Click hướng dẫn sử dụng dịch vụ
@pytest.mark.tc54
def test_click_guide_by_text_tc54(driver):
    buypakage = BuyPakagePage(driver)
    buypakage.click_buy_pakage()
    buypakage.click_icon_cvqt()
    buypakage.scroll_to_element("Lưu ý")
    buypakage.click_by_text("Hướng dẫn đăng ký")
    buypakage.click_by_text("Hướng dẫn đăng ký")
    buypakage.click_by_text("Hướng dẫn sử dụng Data, Thoại, SMS")
    buypakage.click_by_text("Hướng dẫn sử dụng Data, Thoại, SMS")
    buypakage.click_by_text("Hướng dẫn sử dụng Thoại & SMS tại quốc gia tắt 2G/3G")
    buypakage.click_by_text("Hướng dẫn sử dụng Thoại & SMS tại quốc gia tắt 2G/3G")
    buypakage.click_by_text("Lưu ý")
    buypakage.click_by_text("Lưu ý")
    buypakage.wait_for_result("Hướng dẫn sử dụng dịch vụ")
    assert buypakage.is_result_displayed("Hướng dẫn sử dụng dịch vụ")
#TC55. Click các câu hỏi thường gặp
@pytest.mark.tc55
def test_click_question_by_text_tc55(driver):
    buypakage = BuyPakagePage(driver)
    buypakage.click_buy_pakage()
    buypakage.click_icon_cvqt()
    buypakage.scroll_to_element("Xem thêm")
    buypakage.click_by_text("test quyền cvqt")
    buypakage.click_by_text("test quyền cvqt")
    buypakage.click_by_text("Hôm nay bạn cảm thấy thế nào ?")
    buypakage.click_by_text("Hôm nay bạn cảm thấy thế nào ?")
    buypakage.click_by_text("Dịch vụ Call barring có thể sử dụng qua mấy hình thức?")
    buypakage.click_by_text("Dịch vụ Call barring có thể sử dụng qua mấy hình thức?")
    buypakage.wait_for_result("Các câu hỏi thường gặp")
    assert buypakage.is_result_displayed("Các câu hỏi thường gặp")
    
#Đăng ký/huỷ gói cước
#TC56. Đăng ký gói cước 
#1. Đăng ký bằng OTP
# @pytest.mark.tc56
# def test_register_pakage(driver):
#     buypakage = BuyPakagePage(driver)
#     buypakage.click_buy_pakage()
#     buypakage.click_register_d5()
#     buypakage.click_button_continute1()
#     buypakage.click_payment_confirm()
#     buypakage.input_otp("888888")
#     buypakage.wait_for_result("Đăng ký gói cước thành công")
#     assert buypakage.is_result_displayed("Đăng ký gói cước thành công")
#2. Đăng ký bằng mã pin
# @pytest.mark.tc56_1
# def test_register_pakage_PIN(driver):
#     buypakage = BuyPakagePage(driver)
#     buypakage.click_buy_pakage()
#     buypakage.click_register_d5()
#     buypakage.click_button_continute1()
#     buypakage.click_payment_confirm()
#     buypakage.input_otp("8888")
#     buypakage.wait_for_result("Đăng ký gói cước thành công")
#     assert buypakage.is_result_displayed("Đăng ký gói cước thành công")    

    
#TC57. Huỷ gói cước
#1. Huỷ bằng OTP
# @pytest.mark.tc57
# def test_unregister_pakage(driver):
#     buypakage = BuyPakagePage(driver)
#     buypakage.click_buy_pakage()
#     buypakage.click_button_cancel()
#     buypakage.click_button_continute1()
#     buypakage.input_otp("888888")
#     buypakage.wait_for_result("Huỷ gói cước thành công")
#     assert buypakage.is_result_displayed("Huỷ gói cước thành công")
#2. Huỷ bằng mã PIN
# @pytest.mark.tc57_1
# def test_unregister_pakage_PIN(driver):
#     buypakage = BuyPakagePage(driver)
#     buypakage.click_buy_pakage()
#     buypakage.click_button_cancel()
#     buypakage.click_button_continute1()
#     buypakage.input_otp("8888")
#     buypakage.wait_for_result("Huỷ gói cước thành công")
#     assert buypakage.is_result_displayed("Huỷ gói cước thành công")

#TC58. Click các nhóm danh mục 
@pytest.mark.tc58
def test_click_list_categories_tc58(driver):
    buypakage = BuyPakagePage(driver)
    buypakage.click_buy_pakage()
    buypakage.wait_for_result("Hot_2025")
    buypakage.click_by_text("Hot_2025")
    buypakage.click_by_text("Data_2025")
    buypakage.click_by_text("Combo_2025")
    buypakage.click_by_text("MangXH_2025")
    buypakage.click_by_text("Miễn phí MXH")
    # buypakage.click_by_text("Goi_bo sung_2025")
    buypakage.click_by_text("Gói chuyển vùng quốc tế")
    buypakage.wait_for_result("RS")
    assert buypakage.is_result_displayed("RS")

#TC59. Kiểm tra chọn từng chu kỳ gói
@pytest.mark.tc59
def test_click_radio_button_cycle_tc59(driver):
    buypakage = BuyPakagePage(driver)
    buypakage.click_buy_pakage()
    buypakage.wait_for_result("Hot_2025")
    buypakage.click_by_text("Gói ngày")
    buypakage.click_by_text("Gói tháng")
    buypakage.click_by_text("Tất cả")
    buypakage.wait_for_result("D10")
    assert buypakage.is_result_displayed("D10")
#TC60. Lọc gói cước theo giá
@pytest.mark.tc60
def test_click_sort_price_tc60(driver):
    buypakage = BuyPakagePage(driver)
    buypakage.click_buy_pakage()
    # buypakage.click_by_text("Data_2025")
    buypakage.click_by_text("Giá")
    buypakage.wait_for_result("Bán chạy nhất")
    buypakage.click_by_text("Giá")
    buypakage.wait_for_result("Ưa chuộng nhất")
    assert buypakage.is_result_displayed("Ưa chuộng nhất")
#TC61. Lọc gói cước dung lượng
@pytest.mark.tc61
def test_click_sort_data_tc61(driver):
    buypakage = BuyPakagePage(driver)
    buypakage.click_buy_pakage()
    # buypakage.click_by_text("Data_2025")
    buypakage.click_by_text("Dung lượng")
    buypakage.wait_for_result("Bán chạy nhất")
    buypakage.click_by_text("Giá")
    buypakage.wait_for_result("Ưa chuộng nhất")
    assert buypakage.is_result_displayed("Ưa chuộng nhất")

#Màn hình tất cả gói cước
#TC62. Tìm kiếm gói cước tồn tại 
@pytest.mark.tc62
def test_search_pakage_tc62(driver):
    buypakage = BuyPakagePage(driver)
    buypakage.click_buy_pakage()
    buypakage.click_by_text("Xem tất cả")
    buypakage.search_package1("D5")
    buypakage.wait_for_result("D5")
    assert buypakage.is_result_displayed("5.000đ")
#TC63. Tìm kiếm gói cước không tồn tại 
@pytest.mark.tc63
def test_search_pakage_tc63(driver):
    buypakage = BuyPakagePage(driver)
    buypakage.click_buy_pakage()
    buypakage.click_by_text("Xem tất cả")
    buypakage.search_package1("Thế Anh")
    buypakage.wait_for_result("Không tìm thấy gói cước phù hợp với kết quả tìm kiếm")
    assert buypakage.is_result_displayed("Không tìm thấy gói cước phù hợp với kết quả tìm kiếm")
#TC64. Đăng ký gói cước bằng OTP
@pytest.mark.tc64
def test_register_pakage_tc64(driver):
    buypakage = BuyPakagePage(driver)
    buypakage.click_buy_pakage()
    buypakage.click_by_text("Xem tất cả")
    buypakage.search_package1("D5")
    buypakage.click_button_by_text("Done")
    buypakage.click_button_by_text("Chi tiết")
    buypakage.click_by_text("Đăng ký ngay")
    buypakage.click_button_by_text("Tiếp tục")
    buypakage.click_button_by_text("Xác nhận thanh toán")
    buypakage.input_otp("000000")
    buypakage.wait_for_result("Đăng ký gói cước thành công")
    assert buypakage.is_result_displayed("Đăng ký gói cước thành công")

#TC65 Huỷ gói cước bằng OTP
@pytest.mark.tc65
def test_register_pakage(driver):
    buypakage = BuyPakagePage(driver)
    buypakage.click_buy_pakage()
    buypakage.click_by_text("Xem tất cả")
    buypakage.search_package1("D5")
    buypakage.click_button_by_text("Done")
    buypakage.click_button_by_text("Chi tiết")
    buypakage.click_button_by_text("Huỷ")
    buypakage.click_button_by_text("Đồng ý")
    buypakage.input_otp("888888")
    buypakage.wait_for_result("Đăng ký gói cước thành công")
    assert buypakage.is_result_displayed("Đăng ký gói cước thành công")

#TC66 Hẹn roaming 
@pytest.mark.tc66
def test_book_roaming_tc66(driver):
    buypakage = BuyPakagePage(driver)
    buypakage.click_buy_pakage()
    buypakage.click_by_text("Xem tất cả")
    buypakage.scroll_to_element2("Chi tiết")
    buypakage.click_button_by_text("Chi tiết")
    buypakage.click_by_text("Hẹn roaming")
    buypakage.click_button_by_text("calendar")
    buypakage.click_by_image("chevron-right")
    buypakage.click_button_by_text("1")
    buypakage.click_button_by_text("Xác nhận")
    buypakage.click_by_text("Đồng ý")
    buypakage.input_otp("000000")
    buypakage.wait_for_result("Hẹn đăng ký thành công")
    assert buypakage.is_result_displayed("Hẹn đăng ký thành công")

#TC67. Hẹn roaming 
@pytest.mark.tc67
def test_book_roaming_tc67(driver):
    buypakage = BuyPakagePage(driver)
    buypakage.click_buy_pakage()
    buypakage.click_by_text("Xem tất cả")
    buypakage.scroll_to_element2("Chi tiết")
    buypakage.click_button_by_text("Chi tiết")
    buypakage.click_by_text("Liên hệ tư vấn")
    buypakage.click_button_by_text("icon arrow down")
    buypakage.click_button_by_text("15:00 - 17:00")
    buypakage.click_by_text("Đặt lịch")
    buypakage.wait_for_result("Đặt lịch liên hệ tư vấn thành công")
    assert buypakage.is_result_displayed("Đặt lịch liên hệ tư vấn thành công")
    
#TC68. Tặng gói cước 
@pytest.mark.tc68
def test_gift_pakage_tc68(driver):
    buypakage = BuyPakagePage(driver)
    buypakage.click_buy_pakage()
    buypakage.click_by_text("Xem tất cả")
    buypakage.click_button_by_text("Chi tiết")
    buypakage.click_button_by_text("icon gift 1")
    buypakage.gift_pakage("0931791607")
    buypakage.click_button_by_text("Done")
    buypakage.click_register_button()
    buypakage.input_otp("888888")
    buypakage.wait_for_result("Tặng gói cước")
    assert buypakage.is_result_displayed("Tặng gói cước")
    
#TC69. Chia sẻ gói cước
@pytest.mark.tc69
def test_share_pakage_tc69(driver):
    buypakage = BuyPakagePage(driver)
    buypakage.click_buy_pakage()
    buypakage.click_by_text("Xem tất cả")
    buypakage.click_button_by_text("Chi tiết")
    buypakage.click_button_by_text("icon share")
    buypakage.click_by_text("Chia sẻ link giới thiệu")
    buypakage.wait_for_result("Sao chép")
    assert buypakage.is_result_displayed("Sao chép")
#TC70. Click vào từng tiện ích
@pytest.mark.tc70
def test_click_utilities_tc70(driver):
    buypakage = BuyPakagePage(driver)
    buypakage.click_buy_pakage()
    buypakage.scroll_to_element2("Tiện ích")
    buypakage.click_by_text("TNEX Finance")
    buypakage.click_button_by_text("icBack")
    buypakage.click_by_text("Thông tin sử dụng")
    buypakage.click_button_by_text("icBack")
    buypakage.click_by_text("Gói cước")
    buypakage.scroll_to_element2("Tiện ích")
    buypakage.wait_for_text("Mở Thẻ tín dụng HDBank")
    buypakage.click_by_text("Mở Thẻ tín dụng HDBank")
    buypakage.wait_for_text("Tính Năng Mới")
    assert buypakage.is_result_displayed("Tính Năng Mới")