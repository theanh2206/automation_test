import pytest
from selenium.webdriver.support import expected_conditions as EC
from pages.DealsPage_page import DealsPage

#TC71. Tìm kiếm gói cước có trong DB
@pytest.mark.tc71
def test_search_package_tc71(driver):
    dealspage = DealsPage(driver)
    dealspage.click_button_by_text("Ưu đãi")
    dealspage.search_package("D5")
    dealspage.wait_for_result("Gói Data ngày D5")
    assert dealspage.is_result_displayed("Gói Data ngày D5")  
#TC72. Tìm kiếm gói cước không có trong DB
@pytest.mark.tc72
def test_search_package_tc72(driver):
    dealspage = DealsPage(driver)
    dealspage.click_button_by_text("Ưu đãi")
    dealspage.search_package("Thế Anh")
    dealspage.wait_for_result("Không có dữ liệu")
    assert dealspage.is_result_displayed("Không có dữ liệu")  
#TC73. Kiểm tra mẹo tích điểm/chi tiết mẹo tích điểm
@pytest.mark.tc73
def test_save_point_tc73(driver):
    dealspage = DealsPage(driver)
    dealspage.click_button_by_text("Ưu đãi")
    dealspage.wait_for_result("Mẹo tích điểm")
    dealspage.click_save_point()
    dealspage.click_list_save_point(2)
    dealspage.wait_for_result("Đăng ký gói cước tích điểm")
    dealspage.click_button_by_text("icBack")
    dealspage.click_list_save_point(3)
    dealspage.wait_for_result("Tích điểm khi mua sắm online")
    dealspage.click_button_by_text("icBack")
    dealspage.click_list_save_point(4)
    dealspage.wait_for_result("Chương trình khuyến mãi")
    dealspage.click_button_by_text("icBack")
    dealspage.click_list_save_point(1)
    dealspage.wait_for_result("Nạp tiền điện thoại tích điểm")
    dealspage.click_button_by_text("icBack")
    assert dealspage.is_result_displayed("Tích điểm cực dễ cùng MyPoint")  
#TC74. Kiểm tra lịch sử điểm
@pytest.mark.tc74
def test_point_history_tc74(driver):
    dealspage = DealsPage(driver)
    dealspage.click_button_by_text("Ưu đãi")
    dealspage.click_by_image("money-time")
    dealspage.click_by_text1("Rút lại điểm đã bị hết hạn")
    dealspage.click_by_text1("Đóng")
    dealspage.click_by_text1("Tiêu điểm")
    dealspage.click_by_text1("Đổi ưu đãi")
    dealspage.click_by_text1("Đóng")
    assert dealspage.is_result_displayed("Lịch sử điểm")  
    
#TC75. Kiểm tra lịch sử đơn hàng
@pytest.mark.tc75
def test_point_history_tc75(driver):
    dealspage = DealsPage(driver)
    dealspage.click_button_by_text("Ưu đãi")
    dealspage.click_by_image("1000004138")
    dealspage.click_by_text1("Chờ xử lý")
    dealspage.click_by_text1("Tạm duyệt")
    dealspage.click_by_text1("Đã hoàn")
    dealspage.click_by_text1("Đã huỷ")
    assert dealspage.is_result_displayed("Không có dữ liệu")  

#TC76. Click vào các icon trong tab tích điểm(Nạp thẻ, gói cước, mua sắm, khác)
@pytest.mark.tc76
def test_save_point_tc76(driver):
    dealspage = DealsPage(driver)
    dealspage.click_button_by_text("Ưu đãi")
    dealspage.click_by_text1("Tích điểm")
    dealspage.click_by_text1("Nạp thẻ")
    dealspage.click_button_by_text("icBack")
    dealspage.click_by_image("shopping-bag 1")
    dealspage.click_button_by_text("icBack")
    dealspage.click_by_image("Frame 1000004158")
    assert dealspage.is_result_displayed("Cước tạm tính")
#TC77. Click vào các icon trong tab tiêu điểm(Data, thẻ nạp, voucher)
@pytest.mark.tc77
def test_sell_point_tc77(driver):
    dealspage = DealsPage(driver)
    dealspage.click_button_by_text("Ưu đãi")
    dealspage.click_by_text1("Đổi điểm")
    dealspage.click_by_image("ticket-discount 1")
    dealspage.click_button_by_text("icBack")
    dealspage.click_by_image("empty-wallet 1")
    dealspage.wait_for_result("Tích điểm muôn nơi")
    assert dealspage.is_result_displayed("Tích điểm muôn nơi")
#Không ổn định code lại sau
#TC78. Đổi điểm lấy quà
@pytest.mark.tc78
def test_tc78(driver):
    dealspage = DealsPage(driver)
    dealspage.click_button_by_text("Ưu đãi")
    dealspage.scroll_to_element2("Đổi điểm lấy quà")
    # dealspage.click_by_text1("Tất cả")
    dealspage.click_by_text1("VC FLASALE 2")
    dealspage.click_by_text1("Đổi ngay")
    dealspage.input_otp("888888")
    dealspage.wait_for_result("Đổi voucher thành công")
    assert dealspage.is_result_displayed("Đổi voucher thành công")
#TC79. Kiểm tra chi tiết voucher
@pytest.mark.tc79
def test_detail_voucher(driver):
    dealspage = DealsPage(driver)
    dealspage.click_button_by_text("Ưu đãi")
    dealspage.scroll_to_element2("Đổi điểm lấy quà")
    dealspage.click_by_text("Xem thêm")
    dealspage.click_by_text1("  VC FLASALE 2")
    dealspage.wait_for_result("Đổi ngay")
    assert dealspage.is_result_displayed("Đổi ngay")
#TC80. Kiểm tra click ưu đãi tích điểm ở màn hình ngoài
@pytest.mark.tc80
def test_click_deals_point_out(driver):
    dealspage = DealsPage(driver)
    dealspage.click_button_by_text("Ưu đãi")
    dealspage.scroll_to_element2("Ưu đãi tích điểm")
    dealspage.click_by_text1("Thời trang")
    dealspage.click_reward_point(1)
    dealspage.click_button_by_text("icClose")
    dealspage.click_by_text1("Thương mại điện tử")
    dealspage.click_reward_point(1)
    dealspage.click_button_by_text("icClose")
    dealspage.click_reward_point(2)
    dealspage.click_button_by_text("icClose")
    dealspage.click_by_text1("Giáo dục")
    dealspage.click_reward_point(1)
    dealspage.click_button_by_text("icClose")
    dealspage.click_by_text1("Làm đẹp")
    dealspage.click_reward_point(1)
    dealspage.click_button_by_text("icClose")
    dealspage.click_reward_point(2)
    dealspage.click_button_by_text("icClose")
    dealspage.click_by_text1("Mẹ và bé")
    dealspage.click_reward_point(1)
    dealspage.click_button_by_text("icClose")
    dealspage.click_reward_point(2)
    dealspage.click_button_by_text("icClose")
    dealspage.wait_for_result("Ưu đãi tích điểm")
    assert dealspage.is_result_displayed("Ưu đãi tích điểm")
#TC81. Kiểm tra click ưu đãi tích điểm ở màn hình tất cả ưu đãi 
@pytest.mark.tc81
def test_click_deals_point_in(driver):
    dealspage = DealsPage(driver)
    dealspage.click_button_by_text("Ưu đãi")
    # dealspage.scroll_to_element2("Ưu đãi tích điểm")
    dealspage.click_deals_list_all()
    dealspage.click_by_text1("Thời trang")
    dealspage.click_reward_point1(1)
    dealspage.click_button_by_text("icClose")
    dealspage.click_by_text1("Thương mại điện tử")
    dealspage.click_reward_point1(1)
    dealspage.click_button_by_text("icClose")
    dealspage.click_reward_point1(2)
    dealspage.click_button_by_text("icClose")
    dealspage.click_by_text1("Giáo dục")
    dealspage.click_reward_point1(1)
    dealspage.click_button_by_text("icClose")
    dealspage.click_by_text1("Làm đẹp")
    dealspage.click_reward_point1(1)
    dealspage.click_button_by_text("icClose")
    dealspage.click_reward_point1(2)
    dealspage.click_button_by_text("icClose")
    dealspage.click_by_text1("Mẹ và bé")
    dealspage.click_reward_point1(1)
    dealspage.click_button_by_text("icClose")
    dealspage.click_reward_point1(2)
    dealspage.click_button_by_text("icClose")
    dealspage.wait_for_result("Ưu đãi tích điểm")
    assert dealspage.is_result_displayed("Ưu đãi tích điểm")
#TC82. Kiểm tra click ưu đãi khác ở màn hình ngoài
@pytest.mark.tc82
def test_click_deals_point_other_out(driver):
    dealspage = DealsPage(driver)
    dealspage.click_button_by_text("Ưu đãi")
    dealspage.scroll_to_element2("Ưu đãi khác")
    dealspage.click_reward_point3(1)
    dealspage.click_button_by_text("icClose")
    dealspage.click_reward_point3(2)
    dealspage.click_button_by_text("icClose")
    dealspage.click_by_text1("Giáo dục")
    dealspage.click_reward_point3(1)
    dealspage.click_button_by_text("icClose")
    dealspage.click_by_text1("Mua sắm - Giải trí")
    dealspage.click_reward_point3(1)
    dealspage.click_button_by_text("icClose")
    dealspage.click_reward_point3(2)
    dealspage.click_button_by_text("icClose")
    dealspage.click_reward_point3(3)
    dealspage.click_button_by_text("icClose")
    dealspage.click_reward_point3(4)
    dealspage.click_button_by_text("icClose")
    dealspage.wait_for_result("Ưu đãi khác")
    assert dealspage.is_result_displayed("Ưu đãi khác")
#TC83. Kiểm tra click ưu đãi khác ở màn hình tất cả ưu đãi khác
@pytest.mark.tc83
def test_click_deals_point_other_in(driver):
    dealspage = DealsPage(driver)
    dealspage.click_button_by_text("Ưu đãi")
    dealspage.scroll_to_element2("Ưu đãi khác")
    dealspage.click_deals_list_all_other()
    dealspage.click_reward_point4(1)
    dealspage.click_button_by_text("icClose")
    dealspage.click_reward_point4(2)
    dealspage.click_button_by_text("icClose")
    dealspage.click_by_text1("Giáo dục")
    dealspage.click_reward_point4(1)
    dealspage.click_button_by_text("icClose")
    dealspage.click_by_text1("Mua sắm - Giải trí")
    dealspage.click_reward_point4(1)
    dealspage.click_button_by_text("icClose")
    dealspage.click_reward_point4(2)
    dealspage.click_button_by_text("icClose")
    dealspage.click_reward_point4(3)
    dealspage.click_button_by_text("icClose")
    dealspage.click_reward_point4(4)
    dealspage.click_button_by_text("icClose")
    dealspage.wait_for_result("Ưu đãi khác")
    assert dealspage.is_result_displayed("Ưu đãi khác")