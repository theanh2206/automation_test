import pytest
from pages.ServicesPage_page import ServicesPage


#Tìm kiếm gói cước/ dịch vụ bất kỳ trên thanh tìm kiếm
#TC84. Tìm kiếm gói cước tồn tại trong db
@pytest.mark.tc84
def test_search_package_D5_tc84(driver):
    servicespage = ServicesPage(driver)
    servicespage.click_icon_services(4)
    servicespage.search_package("D5")
    servicespage.wait_for_result("D5")
    assert servicespage.is_result_displayed("D5")
#TC85. Tìm kiếm gói cước không có trong DB
@pytest.mark.tc85
def test_search_package_DDDDDDDDD_tc85(driver):
    servicespage = ServicesPage(driver)
    servicespage.click_icon_services(4)
    servicespage.search_package("DDDDDDDDD")
    servicespage.wait_for_result("DDDDDDDDD")
    assert servicespage.is_result_displayed("Lịch sử tìm kiếm")
#TC86. Tìm kiếm gói dịch vụ có trong DB
@pytest.mark.tc86
def test_search_package_DV_tc86(driver):
    servicespage = ServicesPage(driver)
    servicespage.click_icon_services(4)
    servicespage.search_package("MobiGames")
    servicespage.wait_for_result("MobiGames")
    assert servicespage.is_result_displayed("MobiGames")

#TC87. Scroll banner 
@pytest.mark.tc87
def test_scroll_banner_tc87(driver):
    servicespage = ServicesPage(driver)
    servicespage.click_icon_services(4)
    servicespage.wait_for_result("Dịch vụ nổi bật")
    servicespage.swipe_banner(5)
    servicespage.wait_for_result("Dịch vụ nổi bật")
    assert servicespage.is_result_displayed("Dịch vụ nổi bật")
#TC88. Click từng banner
@pytest.mark.tc88
def test_click_banner_tc88(driver):
    servicespage = ServicesPage(driver)
    servicespage.click_icon_services(4)
    servicespage.wait_for_result("Dịch vụ nổi bật")
    servicespage.click_banner()
    servicespage.wait_for_result("Chi tiết dịch vụ")
    assert servicespage.is_result_displayed("Chi tiết dịch vụ")

#TC89. Click từng dịch vụ nổi bật
@pytest.mark.tc89
def test_scroll_services_tc89(driver):
    servicespage = ServicesPage(driver)
    servicespage.click_icon_services(4)
    servicespage.wait_for_result("Dịch vụ nổi bật")
    servicespage.swipe_services(4)
    assert servicespage.is_result_displayed("Dịch vụ nổi bật")
    
#TC90. Đăng ký đổi dịch vụ nổi bật
@pytest.mark.tc90
def test_register_services_tc90(driver):
    servicespage = ServicesPage(driver)
    servicespage.click_icon_services(4)
    servicespage.wait_for_result("Dịch vụ nổi bật") 
    servicespage.click_services_outstanding(2)
    servicespage.click_button_register_services()
    # servicespage.press_back()
    servicespage.click_button_continute()
    servicespage.input_otp("000000")
    servicespage.wait_for_result("Yêu cầu thành công")
    assert servicespage.is_result_displayed("Yêu cầu thành công")
#TC91. Huỷ đăng ký dịch vụ nổi bặt
@pytest.mark.tc91
def test_unregister_services_tc91(driver):
    servicespage = ServicesPage(driver)
    servicespage.click_icon_services(4)
    servicespage.wait_for_result("Dịch vụ nổi bật")
    servicespage.click_services_outstanding(2)
    servicespage.click_by_text("Hủy")
    servicespage.press_back()
    servicespage.click_button_continute()
    servicespage.input_otp("000000")
    servicespage.wait_for_result("Hủy gói dịch vụ thành công")
    assert servicespage.is_result_displayed("Hủy gói dịch vụ thành công")
    
#TC92. CLick từng dịch vụ trong danh sách dịch vụ
@pytest.mark.tc92
def test_click_services_tc92(driver):
    servicespage = ServicesPage(driver)
    servicespage.click_icon_services(4)
    servicespage.wait_for_result("Dịch vụ nổi bật")
    servicespage.click_services(1)
    servicespage.wait_for_result("Chi tiết dịch vụ")
    servicespage.press_back()
    servicespage.click_services(2)
    servicespage.wait_for_result("Chi tiết dịch vụ")
    servicespage.press_back()
    servicespage.click_services(3)
    servicespage.wait_for_result("Chi tiết dịch vụ")
    servicespage.press_back()
    servicespage.click_services(4)
    servicespage.wait_for_result("Chi tiết dịch vụ")
    servicespage.press_back()
    servicespage.click_services(5)
    servicespage.wait_for_result("Chi tiết dịch vụ")
    servicespage.press_back()
    servicespage.wait_for_result("Danh sách dịch vụ")
    assert servicespage.is_result_displayed("Danh sách dịch vụ")
#Tab giáo dục
@pytest.mark.tc92_1
def test_click_services_tc92_1(driver):
    servicespage = ServicesPage(driver)
    servicespage.click_icon_services(4)
    servicespage.wait_for_result("Dịch vụ nổi bật")
    servicespage.scroll_to_element1("Onlive TV")
    servicespage.click_by_text("Giáo dục")
    servicespage.click_services(1)
    servicespage.wait_for_result("Chi tiết dịch vụ")
    servicespage.press_back()
    servicespage.click_services(2)
    servicespage.wait_for_result("Chi tiết dịch vụ")
    servicespage.press_back()
    servicespage.click_services(3)
    servicespage.wait_for_result("Chi tiết dịch vụ")
    servicespage.press_back()
    servicespage.click_services(4)
    servicespage.wait_for_result("Chi tiết dịch vụ")
    servicespage.press_back()
    servicespage.wait_for_result("Danh sách dịch vụ")
    assert servicespage.is_result_displayed("Danh sách dịch vụ")
#Tab dịch vụ nổi bật
@pytest.mark.tc92_2
def test_click_services_tc92_2(driver):
    servicespage = ServicesPage(driver)
    servicespage.click_icon_services(4)
    servicespage.wait_for_result("Dịch vụ nổi bật")
    servicespage.scroll_to_element1("Onlive TV")
    servicespage.click_by_text("Dịch vụ nổi bật", 2)
    servicespage.click_services(1)
    servicespage.press_back()
    servicespage.click_services(2)
    servicespage.press_back()
    servicespage.click_services(3)
    servicespage.press_back()
    servicespage.click_services(4)
    servicespage.press_back()
    servicespage.wait_for_result("Danh sách dịch vụ")
    assert servicespage.is_result_displayed("Danh sách dịch vụ")