import pytest
from pages.ServicesPage_page import ServicesPage

#TC152. Click button đăng nhập
@pytest.mark.tc152
def test_click_button_login_tc152(driver):
    servicespage = ServicesPage(driver)
    servicespage.click_icon_services()
    servicespage.click_button_by_text("Đăng nhập", 2)
    servicespage.wait_for_result("Số điện thoại")
    assert servicespage.is_result_displayed("Đăng nhập")
#TC153. Click thanh menu
@pytest.mark.tc153
def test_click_button_login_tc153(driver):
    servicespage = ServicesPage(driver)
    servicespage.click_icon_services()
    servicespage.click_menu()
    servicespage.wait_for_result("Đăng nhập")
    assert servicespage.is_result_displayed("Đăng nhập")
#TC154. Click banner
@pytest.mark.tc154
def test_click_banner_tc154(driver):
    servicespage = ServicesPage(driver)
    servicespage.click_icon_services()
    servicespage.wait_for_result("Dịch vụ nổi bật")
    servicespage.swipe_banner(5)
    servicespage.click_banner()
    servicespage.wait_for_result("Chi tiết dịch vụ")
    assert servicespage.is_result_displayed("Chi tiết dịch vụ")
#TC155. Click từng dịch vụ nổi bật
@pytest.mark.tc155
def test_click_services_tc155(driver):
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
    servicespage.wait_for_result("Dịch vụ nổi bật")
    assert servicespage.is_result_displayed("Đăng nhập")
#TC156. CLick từng dịch vụ trong danh sách dịch vụ
@pytest.mark.tc156
def test_click_services_tc156(driver):
    servicespage = ServicesPage(driver)
    servicespage.click_button_by_text("Dịch vụ")
    servicespage.wait_for_result("Dịch vụ nổi bật")
    servicespage.scroll_to_element2("Giải đố")
    servicespage.click_icon_services1(1)
    servicespage.wait_for_result("Chi tiết dịch vụ")
    servicespage.click_button_by_text("icBack")
    servicespage.click_icon_services1(2)
    servicespage.wait_for_result("Chi tiết dịch vụ")
    servicespage.click_button_by_text("icBack")
    servicespage.click_icon_services1(3)
    servicespage.wait_for_result("Chi tiết dịch vụ")
    servicespage.click_button_by_text("icBack")
    servicespage.click_icon_services1(4)
    servicespage.wait_for_result("Chi tiết dịch vụ")
    servicespage.click_button_by_text("icBack")
    servicespage.click_icon_services1(5)
    servicespage.wait_for_result("Chi tiết dịch vụ")
    servicespage.click_button_by_text("icBack")
    servicespage.click_icon_services1(6)
    servicespage.wait_for_result("Chi tiết dịch vụ")
    servicespage.click_button_by_text("icBack")
    servicespage.click_icon_services1(7)
    servicespage.wait_for_result("Chi tiết dịch vụ")
    servicespage.click_button_by_text("icBack")
    servicespage.click_icon_services1(8)
    servicespage.wait_for_result("Chi tiết dịch vụ")
    servicespage.click_button_by_text("icBack")
    servicespage.wait_for_result("Danh sách dịch vụ")
    assert servicespage.is_result_displayed("Danh sách dịch vụ")