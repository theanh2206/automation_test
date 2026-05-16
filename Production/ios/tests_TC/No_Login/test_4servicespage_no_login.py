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
    servicespage.click_by_text("Vietlott SMS")
    servicespage.click_button_by_text("icBack")
    servicespage.click_by_text("MobiSafe")
    servicespage.click_button_by_text("icBack")
    servicespage.click_by_text("MobiPA")
    servicespage.click_button_by_text("icBack")
    servicespage.click_by_text("MobiGames")
    servicespage.click_button_by_text("icBack")
    servicespage.scroll_left(times=1)
    servicespage.click_by_text("Meet")
    servicespage.click_button_by_text("icBack")
    servicespage.click_by_text("S.Travel")
    servicespage.click_button_by_text("icBack")
    servicespage.click_by_text("mobiCloud")
    servicespage.click_button_by_text("icBack")
    assert servicespage.is_result_displayed("Đăng nhập")
#TC156. CLick từng dịch vụ trong danh sách dịch vụ
@pytest.mark.tc156
def test_click_services_tc156(driver):
    servicespage = ServicesPage(driver)
    servicespage.click_button_by_text("Dịch vụ")
    servicespage.wait_for_result("Dịch vụ nổi bật")
    servicespage.scroll_to_element2("Thư viện số")
    #Thư viện số
    servicespage.click_by_text1("Thư viện số")
    servicespage.click_by_text("mobiEdu")
    servicespage.click_button_by_text("icBack")
    servicespage.click_by_text("mobiAgri")
    servicespage.click_button_by_text("icBack")
    servicespage.click_by_text("MobiGames")
    servicespage.click_button_by_text("icBack")
    servicespage.click_by_text("mobiOn")
    servicespage.click_button_by_text("icBack")
    servicespage.click_by_text("Onlive TV")
    servicespage.click_button_by_text("icBack")
    servicespage.wait_for_result("Danh sách dịch vụ")
    assert servicespage.is_result_displayed("Danh sách dịch vụ")
    
#Giáo dục
@pytest.mark.tc156_1
def test_click_services_tc156_1(driver):
    servicespage = ServicesPage(driver)
    servicespage.click_button_by_text("Dịch vụ")
    servicespage.wait_for_result("Dịch vụ nổi bật")
    servicespage.scroll_to_element2("Thư viện số")
    servicespage.click_by_text("Giáo dục")
    servicespage.click_by_text("Trường học số Quốc gia")
    servicespage.click_button_by_text("icBack")
    servicespage.click_by_text("Cổng thi đại học mobiEdu")
    servicespage.click_button_by_text("icBack")
    servicespage.click_by_text("Mobistudy")
    servicespage.click_button_by_text("icBack")
    servicespage.click_by_text("IELTS")
    servicespage.click_button_by_text("icBack")
    servicespage.click_by_text("Gitiho")
    servicespage.click_button_by_text("icBack")
    servicespage.click_by_text("TOEIC")
    servicespage.click_button_by_text("icBack")
    servicespage.wait_for_text("Mlearn")
    servicespage.click_by_text1("Mlearn")
    servicespage.click_button_by_text("icBack")
    servicespage.click_by_text("GIÁO DỤC KỸ NĂNG SỐNG")
    servicespage.click_button_by_text("icBack")
    servicespage.wait_for_text("Học Mãi")
    servicespage.click_by_text("Học Mãi")
    servicespage.click_button_by_text("icBack")
    servicespage.click_by_text("MOBIENGLISH")
    servicespage.click_button_by_text("icBack")
    servicespage.wait_for_result("Danh sách dịch vụ")
    assert servicespage.is_result_displayed("Danh sách dịch vụ")
#Dịch vụ nổi bật
@pytest.mark.tc156_2
def test_click_services_tc156_2(driver):
    servicespage = ServicesPage(driver)
    servicespage.click_button_by_text("Dịch vụ")
    servicespage.wait_for_result("Dịch vụ nổi bật")
    servicespage.scroll_to_element2("Thư viện số")
    servicespage.click_by_text("Dịch vụ nổi bật", 2)
    servicespage.click_by_text("Vietlott SMS")
    servicespage.click_button_by_text("icBack")
    servicespage.click_by_text("MyPoint")
    servicespage.click_button_by_text("icBack")
    servicespage.click_by_text("MobiPA", 2)
    servicespage.click_button_by_text("icBack")
    servicespage.click_by_text("Funring")
    servicespage.click_button_by_text("icBack")
    servicespage.click_by_text("Meet")
    servicespage.click_button_by_text("icBack")
    servicespage.click_by_text("S.Travel")
    servicespage.click_button_by_text("icBack")
    servicespage.wait_for_result("Danh sách dịch vụ")
    assert servicespage.is_result_displayed("Danh sách dịch vụ")
#Tài chính
@pytest.mark.tc156_3
def test_click_services_tc156_3(driver):
    servicespage = ServicesPage(driver)
    servicespage.click_button_by_text("Dịch vụ")
    servicespage.wait_for_result("Dịch vụ nổi bật")
    servicespage.scroll_to_element2("Thư viện số")
    servicespage.click_by_text("Tài chính")
    servicespage.click_by_text("MobiFone Money")
    servicespage.click_button_by_text("icBack")
    servicespage.click_by_text("mobiCloud")
    servicespage.click_button_by_text("icBack")
    servicespage.wait_for_result("Danh sách dịch vụ")
    assert servicespage.is_result_displayed("Danh sách dịch vụ")
#Khác
@pytest.mark.tc156_4
def test_click_services_tc156_4(driver):
    servicespage = ServicesPage(driver)
    servicespage.click_button_by_text("Dịch vụ")
    servicespage.wait_for_result("Dịch vụ nổi bật")
    servicespage.scroll_to_element2("Thư viện số")
    servicespage.click_by_text("Tài chính")
    servicespage.click_by_text("Khác")
    servicespage.click_by_text("Thanh Toán Trên Google Play")
    servicespage.click_button_by_text("icBack")
    servicespage.click_by_text("Thông báo cuộc gọi nhỡ (MCA)")
    servicespage.click_button_by_text("icBack")
    servicespage.click_by_text("Witalk")
    servicespage.click_button_by_text("icBack")
    servicespage.click_by_text("Buzz me")
    servicespage.click_button_by_text("icBack")
    servicespage.click_by_text("Dịch vụ Chuyển vùng quốc tế")
    servicespage.click_button_by_text("icBack")
    servicespage.wait_for_result("Danh sách dịch vụ")
    assert servicespage.is_result_displayed("Danh sách dịch vụ")
#Dịch vụ quốc tế
@pytest.mark.tc156_5
def test_click_services_tc156_5(driver):
    servicespage = ServicesPage(driver)
    servicespage.click_button_by_text("Dịch vụ")
    servicespage.wait_for_result("Dịch vụ nổi bật")
    servicespage.scroll_to_element2("Thư viện số")
    servicespage.click_by_text("Tài chính")
    servicespage.click_by_text("Dịch vụ Quốc tế")
    servicespage.click_by_text("CVQT trên Máy bay và Tàu biển")
    servicespage.click_button_by_text("icBack")
    servicespage.click_by_text("Thuê bao nước ngoài đến Việt Nam")
    servicespage.click_button_by_text("icBack")
    servicespage.click_by_text("Thuê bao Mobifone ra nước ngoài")
    servicespage.click_button_by_text("icBack")
    servicespage.click_by_text("Dịch Vụ Thoại Quốc Tế")
    servicespage.click_button_by_text("icBack")
    servicespage.click_by_text("Dịch Vụ SMS Quốc Tế")
    servicespage.click_button_by_text("icBack")
    servicespage.click_by_text("Dịch Vụ Đặt Phòng Khách Sạn")
    servicespage.click_button_by_text("icBack")
    servicespage.wait_for_result("Danh sách dịch vụ")
    assert servicespage.is_result_displayed("Danh sách dịch vụ")
@pytest.mark.tc156_6
def test_click_services_tc156_6(driver):
    servicespage = ServicesPage(driver)
    servicespage.click_button_by_text("Dịch vụ")
    servicespage.wait_for_result("Dịch vụ nổi bật")
    servicespage.scroll_to_element2("Thư viện số")
    #Internet an toàn
    servicespage.click_by_text("Khác")
    servicespage.click_by_text("Internet an toàn")
    servicespage.click_by_text("MobiSafe")
    servicespage.click_button_by_text("icBack")
    servicespage.wait_for_result("Danh sách dịch vụ")
    assert servicespage.is_result_displayed("Danh sách dịch vụ")
   