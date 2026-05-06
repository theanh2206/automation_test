import pytest
from selenium.webdriver.support import expected_conditions as EC
from pages.DealsPage_page import DealsPage

#TC71. Tìm kiếm gói cước có trong DB
@pytest.mark.tc71
def test_search_package_tc71(driver):
    dealspage = DealsPage(driver)
    dealspage.click_icon_deals(3)
    dealspage.search_package("D5")
    dealspage.wait_for_result("D5")
    assert dealspage.is_result_displayed("D5")  
#TC72. Tìm kiếm gói cước không có trong DB
@pytest.mark.tc72
def test_search_package_tc72(driver):
    dealspage = DealsPage(driver)
    dealspage.click_icon_deals(3)
    dealspage.search_package("Thế Anh")
    dealspage.wait_for_result("Lịch sử")
    assert dealspage.is_result_displayed("Lịch sử")  
#TC73. Kiểm tra mẹo tích điểm/chi tiết mẹo tích điểm
@pytest.mark.tc73
def test_save_point_tc73(driver):
    dealspage = DealsPage(driver)
    dealspage.click_icon_deals(3)
    dealspage.click_save_point1()
    dealspage.click_list_save_point(1)
    dealspage.wait_for_result("Nạp tiền điện thoại tích điểm")
    dealspage.press_back()
    dealspage.click_list_save_point(2)
    dealspage.wait_for_result("Đăng ký gói cước tích điểm")
    dealspage.press_back()
    dealspage.click_list_save_point(3)
    dealspage.wait_for_result("Tích điểm khi mua sắm online")
    dealspage.press_back()
    dealspage.click_list_save_point(4)
    dealspage.wait_for_result("Chương trình khuyến mãi")
    dealspage.press_back()
    assert dealspage.is_result_displayed("Tích điểm cực dễ cùng MyPoint")  
#TC74. Kiểm tra lịch sử điểm
@pytest.mark.tc74
def test_point_history_tc74(driver):
    dealspage = DealsPage(driver)
    dealspage.click_icon_deals(3)
    dealspage.click_point_history()
    dealspage.click_list_point_history(1)
    dealspage.click_close()
    dealspage.click_by_text("Tiêu điểm")
    dealspage.click_list_point_history(1)
    dealspage.click_close()
    assert dealspage.is_result_displayed("Lịch sử điểm")  
#TC75. Kiểm tra lịch sử đơn hàng
@pytest.mark.tc75
def test_point_history_tc75(driver):
    dealspage = DealsPage(driver)
    dealspage.click_icon_deals(3)
    dealspage.click_cart_history()
    dealspage.click_by_text("Chờ xử lý")
    dealspage.click_by_text("Tạm duyệt")
    dealspage.click_by_text("Đã hoàn")
    dealspage.click_by_text("Đã hủy")
    assert dealspage.is_result_displayed("Không tìm thấy dữ liệu")  

#TC76. Click vào các icon trong tab tích điểm(Nạp thẻ, gói cước, mua sắm, khác)
@pytest.mark.tc76
def test_save_point_tc76(driver):
    dealspage = DealsPage(driver)
    dealspage.click_icon_deals(3)
    dealspage.click_by_text("Tích điểm")
    dealspage.click_save_point(1)
    dealspage.press_back()
    dealspage.click_save_point(3)
    dealspage.press_back()
    dealspage.click_save_point(2)
    assert dealspage.is_result_displayed("Cước tạm tính")
#TC77. Click vào các icon trong tab tiêu điểm(Data, thẻ nạp, voucher)
@pytest.mark.tc77
def test_sell_point_tc77(driver):
    dealspage = DealsPage(driver)
    dealspage.click_icon_deals(3)
    dealspage.click_by_text("Tiêu điểm")
    dealspage.click_sell_point(1)
    dealspage.press_back()
    dealspage.press_back()
    dealspage.click_sell_point(2)
    dealspage.press_back()
    dealspage.press_back()
    dealspage.click_sell_point(3)
    dealspage.wait_for_result("Ưu đãi MyPoint")
    assert dealspage.is_result_displayed("Ưu đãi MyPoint")

#TC78. Đổi điểm lấy quà
@pytest.mark.tc78
def test_tc78(driver):
    dealspage = DealsPage(driver)
    dealspage.click_icon_deals(3)
    dealspage.scroll_to_element("Xem thêm")
    dealspage.click_by_text("Xem thêm")
    dealspage.click_icon_mypoint_deals(1)
    dealspage.click_button_exchange()
    dealspage.input_otp("000000")#(Đổi bằng mã PIN thì chỉ cần truyền mã PIN vào là được)
    dealspage.wait_for_result("Đổi voucher thành công")
    assert dealspage.is_result_displayed("Đổi voucher thành công")
#TC79. Kiểm tra chi tiết voucher
@pytest.mark.tc79
def test_detail_voucher_tc79(driver):
    dealspage = DealsPage(driver)
    dealspage.click_icon_deals(3)
    dealspage.scroll_to_element1("Xem thêm")
    dealspage.click_by_text("Xem thêm")
    dealspage.click_icon_mypoint_deals(1)
    dealspage.wait_for_result("Điều kiện sử dụng")
    assert dealspage.is_result_displayed("Điều kiện sử dụng")
#TC80. Kiểm tra click ưu đãi tích điểm ở màn hình ngoài
@pytest.mark.tc80
def test_click_deals_point_out_tc80(driver):
    dealspage = DealsPage(driver)
    dealspage.click_icon_deals(3)
    dealspage.scroll_to_element1("Ưu đãi tích điểm")
    dealspage.click_reward_point(1)
    dealspage.click_button_close()
    dealspage.click_by_text("Thương mại điện tử")
    dealspage.click_reward_point(1)
    dealspage.click_button_close()
    dealspage.click_reward_point(2)
    dealspage.click_button_close()
    dealspage.click_by_text("Giáo dục")
    dealspage.click_reward_point(1)
    dealspage.click_button_close()
    dealspage.click_by_text("Làm đẹp")
    dealspage.click_reward_point(1)
    dealspage.click_button_close()
    dealspage.click_reward_point(2)
    dealspage.click_button_close()
    dealspage.click_by_text("Mẹ và bé")
    dealspage.click_reward_point(1)
    dealspage.click_button_close()
    dealspage.click_reward_point(2)
    dealspage.click_button_close()
    dealspage.wait_for_result("Ưu đãi tích điểm")
    assert dealspage.is_result_displayed("Ưu đãi tích điểm")
#TC81. Kiểm tra click ưu đãi tích điểm ở màn hình tất cả ưu đãi 
@pytest.mark.tc81
def test_click_deals_point_in_tc81(driver):
    dealspage = DealsPage(driver)
    dealspage.click_icon_deals(3)
    dealspage.scroll_to_element1("Ưu đãi tích điểm")
    dealspage.click_deals_list_all()
    dealspage.click_reward_point(1)
    dealspage.click_button_close()
    dealspage.click_by_text("Thương mại điện tử")
    dealspage.click_reward_point(1)
    dealspage.click_button_close()
    dealspage.click_reward_point(2)
    dealspage.click_button_close()
    dealspage.click_by_text("Giáo dục")
    dealspage.click_reward_point(1)
    dealspage.click_button_close()
    dealspage.click_by_text("Làm đẹp")
    dealspage.click_reward_point(1)
    dealspage.click_button_close()
    dealspage.click_reward_point(2)
    dealspage.click_button_close()
    dealspage.click_by_text("Mẹ và bé")
    dealspage.click_reward_point(1)
    dealspage.click_button_close()
    dealspage.click_reward_point(2)
    dealspage.click_button_close()
    dealspage.wait_for_result("Ưu đãi tích điểm")
    assert dealspage.is_result_displayed("Ưu đãi tích điểm")
#TC82. Kiểm tra click ưu đãi khác ở màn hình ngoài
@pytest.mark.tc82
def test_click_deals_point_other_out_tc82(driver):
    dealspage = DealsPage(driver)
    dealspage.click_icon_deals(3)
    dealspage.scroll_to_element1("Tài chính - Ngân hàng")
    dealspage.click_reward_point(2)
    dealspage.click_button_close()
    dealspage.click_reward_point(3)
    dealspage.click_button_close()
    dealspage.click_by_text("Giáo dục")
    dealspage.click_reward_point(2)
    dealspage.click_button_close()
    dealspage.click_by_text("Mua sắm - Giải trí")
    dealspage.click_reward_point(2)
    dealspage.click_button_close()
    dealspage.click_reward_point(3)
    dealspage.click_button_close()
    dealspage.click_reward_point(4)
    dealspage.click_button_close()
    dealspage.click_reward_point(5)
    dealspage.click_button_close()
    dealspage.wait_for_result("Ưu đãi khác")
    assert dealspage.is_result_displayed("Ưu đãi khác")
#TC83. Kiểm tra click ưu đãi khác ở màn hình tất cả ưu đãi khác
@pytest.mark.tc83
def test_click_deals_point_other_in_tc83(driver):
    dealspage = DealsPage(driver)
    dealspage.click_icon_deals(3)
    dealspage.scroll_to_element1("Tài chính - Ngân hàng")
    dealspage.click_deals_list_all_other()
    dealspage.click_reward_point(1)
    dealspage.click_button_close()
    dealspage.click_reward_point(2)
    dealspage.click_button_close()
    dealspage.click_by_text("Giáo dục")
    dealspage.click_reward_point(1)
    dealspage.click_button_close()
    dealspage.click_by_text("Mua sắm - Giải trí")
    dealspage.click_reward_point(1)
    dealspage.click_button_close()
    dealspage.click_reward_point(2)
    dealspage.click_button_close()
    dealspage.click_reward_point(3)
    dealspage.click_button_close()
    dealspage.click_reward_point(4)
    dealspage.click_button_close()
    dealspage.wait_for_result("Ưu đãi khác")
    assert dealspage.is_result_displayed("Ưu đãi khác")