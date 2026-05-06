import pytest
from selenium.webdriver.support import expected_conditions as EC
from pages.ServicesPage_page import ServicesPage
from pages.BasePage_page import BasePage

#Tìm kiếm gói cước/ dịch vụ bất kỳ trên thanh tìm kiếm
#TC84. Tìm kiếm gói cước tồn tại trong db
@pytest.mark.tc84
def test_search_package_tc84(driver):
    servicespage = ServicesPage(driver)
    servicespage.click_button_by_text("Dịch vụ")
    servicespage.search_package("D5")
    servicespage.wait_for_result("Gói Data ngày D5")
    assert servicespage.is_result_displayed("Gói Data ngày D5")
#TC85. Tìm kiếm gói cước không có trong DB
@pytest.mark.tc85
def test_search_package_tc85(driver):
    servicespage = ServicesPage(driver)
    servicespage.click_button_by_text("Dịch vụ")
    servicespage.search_package("DDDDDDDDD")
    servicespage.wait_for_result("Không có dữ liệu")
    assert servicespage.is_result_displayed("Không có dữ liệu")
#TC86. Tìm kiếm gói dịch vụ có trong DB
@pytest.mark.tc86
def test_search_package_tc86(driver):
    servicespage = ServicesPage(driver)
    servicespage.click_button_by_text("Dịch vụ")
    servicespage.search_package("Game Data")
    servicespage.wait_for_result("Game Data")
    assert servicespage.is_result_displayed("Game Data")

#TC87. Scroll banner 
@pytest.mark.tc87
def test_scroll_banner_tc87(driver):
    servicespage = ServicesPage(driver)
    servicespage.click_button_by_text("Dịch vụ")
    servicespage.wait_for_result("Dịch vụ nổi bật")
    servicespage.swipe_banner(5)
    assert servicespage.is_result_displayed("Dịch vụ nổi bật")
#TC88. Click từng banner
@pytest.mark.tc88
def test_scroll_banner_tc88(driver):
    servicespage = ServicesPage(driver)
    servicespage.click_button_by_text("Dịch vụ")
    servicespage.wait_for_result("Dịch vụ nổi bật")
    servicespage.click_banner()
    assert servicespage.is_result_displayed("Chi tiết dịch vụ")

#TC89. Click từng dịch vụ nổi bật
@pytest.mark.tc89
def test_scroll_services(driver):
    servicespage = ServicesPage(driver)
    servicespage.click_button_by_text("Dịch vụ")
    servicespage.wait_for_result("Dịch vụ nổi bật") 
    servicespage.click_by_text1("ON2")
    servicespage.click_button_by_text("icBack")
    servicespage.click_by_text1("MobiGames")
    servicespage.click_button_by_text("icBack")
    servicespage.click_by_text1("Ltest VieON data 4")
    servicespage.click_button_by_text("icBack")
    servicespage.click_by_text1("Ltest VieON data")
    servicespage.click_button_by_text("icBack")
    assert servicespage.is_result_displayed("Dịch vụ nổi bật")
    
#TC90. Đăng ký đổi dịch vụ nổi bật
@pytest.mark.tc90
def test_register_services_tc90(driver):
    servicespage = ServicesPage(driver)
    servicespage.click_button_by_text("Dịch vụ")
    servicespage.wait_for_result("Dịch vụ nổi bật") 
    servicespage.click_by_text1("MobiGames")
    servicespage.click_button_by_text("btn signed")
    servicespage.click_button_by_text("Đăng ký")
    servicespage.input_otp("000000")
    servicespage.wait_for_result("Yêu cầu thành công")
    assert servicespage.is_result_displayed("Yêu cầu thành công")
#TC91. Huỷ đăng ký dịch vụ nổi bặt
@pytest.mark.tc91
def test_unregister_services(driver):
    servicespage = ServicesPage(driver)
    servicespage.click_button_by_text("Dịch vụ")
    servicespage.wait_for_result("Dịch vụ nổi bật")
    servicespage.click_by_text1("MobiGames")
    servicespage.click_button_by_text("btn huy")
    servicespage.click_button_by_text("Đồng ý")
    servicespage.input_otp("888888")
    servicespage.wait_for_result("Hủy gói dịch vụ thành công")
    assert servicespage.is_result_displayed("Hủy gói dịch vụ thành công")
    
#TC92. CLick từng dịch vụ trong danh sách dịch vụ
@pytest.mark.tc92
def test_click_services_tc92(driver):
    servicespage = ServicesPage(driver)
    servicespage.click_button_by_text("Dịch vụ")
    servicespage.wait_for_result("Dịch vụ nổi bật")
    servicespage.click_by_text1("Gói Cước Global Saving 1313")
    servicespage.wait_for_result("Chi tiết dịch vụ")
    servicespage.click_button_by_text("icBack")
    servicespage.click_by_text1("K+ data")
    servicespage.wait_for_result("Chi tiết dịch vụ")
    servicespage.click_button_by_text("icBack")
    servicespage.click_by_text1("iflix")
    servicespage.wait_for_result("Chi tiết dịch vụ")
    servicespage.click_button_by_text("icBack")
    servicespage.click_by_text1("mGame")
    servicespage.wait_for_result("Chi tiết dịch vụ")
    servicespage.click_button_by_text("icBack")
    servicespage.click_by_text1("Elsa data")
    servicespage.wait_for_result("Chi tiết dịch vụ")
    servicespage.click_button_by_text("icBack")
    servicespage.click_by_text1("MobiClip")
    servicespage.wait_for_result("Chi tiết dịch vụ")
    servicespage.click_button_by_text("icBack")
    servicespage.click_by_text1("Game Data")
    servicespage.wait_for_result("Chi tiết dịch vụ")
    servicespage.click_button_by_text("icBack")
    servicespage.click_by_text1("Witalk")
    servicespage.wait_for_result("Chi tiết dịch vụ")
    servicespage.click_button_by_text("icBack")
    servicespage.wait_for_result("Danh sách dịch vụ")
    assert servicespage.is_result_displayed("Danh sách dịch vụ")