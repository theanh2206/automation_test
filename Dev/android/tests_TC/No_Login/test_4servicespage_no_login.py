import pytest
from pages.ServicesPage_page import ServicesPage

#TC152. Click button đăng nhập
@pytest.mark.tc152
def test_click_button_login_tc152(driver):
    servicespage = ServicesPage(driver)
    servicespage.click_icon_services(4)
    servicespage.click_button_login()
    servicespage.wait_for_result("Đăng nhập")
    assert servicespage.is_result_displayed("Đăng nhập")
#TC153. Click thanh menu
@pytest.mark.tc153
def test_click_button_login_tc153(driver):
    servicespage = ServicesPage(driver)
    servicespage.click_icon_services(4)
    servicespage.click_menu()
    servicespage.wait_for_result("Đăng nhập")
    assert servicespage.is_result_displayed("Đăng nhập")
#TC154. Click banner
@pytest.mark.tc154
def test_click_banner_tc154(driver):
    servicespage = ServicesPage(driver)
    servicespage.click_icon_services(4)
    servicespage.wait_for_result("Dịch vụ nổi bật")
    servicespage.swipe_banner(5)
    servicespage.click_banner()
    servicespage.wait_for_result("Chi tiết dịch vụ")
    assert servicespage.is_result_displayed("Chi tiết dịch vụ")
#TC155. Click từng dịch vụ nổi bật
@pytest.mark.tc155
def test_click_services_tc155(driver):
    servicespage = ServicesPage(driver)
    servicespage.click_icon_services(4)
    servicespage.wait_for_result("Dịch vụ nổi bật")
    servicespage.swipe_services(4)
    servicespage.click_services_outstanding(2)
    servicespage.wait_for_result("Chi tiết dịch vụ")
    assert servicespage.is_result_displayed("Chi tiết dịch vụ")
#TC156. CLick từng dịch vụ trong danh sách dịch vụ
@pytest.mark.tc156
def test_click_services_tc156(driver):
    servicespage = ServicesPage(driver)
    servicespage.click_icon_services(4)
    servicespage.wait_for_result("Danh sách dịch vụ")
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