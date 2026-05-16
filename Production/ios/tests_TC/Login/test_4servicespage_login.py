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
    servicespage.wait_for_result("D5")
    assert servicespage.is_result_displayed("D5")
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
    servicespage.search_package("MobiGames")
    servicespage.wait_for_result("MobiGames")
    assert servicespage.is_result_displayed("MobiGames")

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
def test_scroll_services_tc89(driver):
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
    servicespage.scroll_left1(times=1)
    servicespage.click_by_text("Meet")
    servicespage.click_button_by_text("icBack")
    servicespage.click_by_text("S.Travel")
    servicespage.click_button_by_text("icBack")
    servicespage.click_by_text("mobiCloud")
    servicespage.click_button_by_text("icBack")
    assert servicespage.is_result_displayed("Dịch vụ nổi bật")
    
#TC90. Đăng ký đổi dịch vụ nổi bật
@pytest.mark.tc90
def test_register_services_tc90(driver):
    servicespage = ServicesPage(driver)
    servicespage.click_button_by_text("Dịch vụ")
    servicespage.wait_for_result("Dịch vụ nổi bật") 
    servicespage.search_package("Funring")
    servicespage.wait_for_result("Funring")
    servicespage.click_by_text1("Funring")
    servicespage.click_button_by_text("btn signed")
    servicespage.click_button_by_text("Đăng ký")
    servicespage.input_otp("000000")
    servicespage.wait_for_result("Yêu cầu thành công")
    assert servicespage.is_result_displayed("Yêu cầu thành công")
#TC91. Huỷ đăng ký dịch vụ nổi bặt
@pytest.mark.tc91
def test_unregister_services_tc91(driver):
    servicespage = ServicesPage(driver)
    servicespage.click_button_by_text("Dịch vụ")
    servicespage.wait_for_result("Dịch vụ nổi bật")
    servicespage.search_package("Funring")
    servicespage.wait_for_result("Funring")
    servicespage.click_by_text1("Funring")
    servicespage.click_button_by_text("btn huy")
    servicespage.click_button_by_text("Đồng ý")
    servicespage.input_otp("000000")
    servicespage.wait_for_result("Huỷ dịch vụ")
    assert servicespage.is_result_displayed("Huỷ dịch vụ")
    
#TC92. CLick từng dịch vụ trong danh sách dịch vụ
@pytest.mark.tc92
def test_click_services_tc92(driver):
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
@pytest.mark.tc92_1
def test_click_services_tc92_1(driver):
    servicespage = ServicesPage(driver)
    servicespage.click_button_by_text("Dịch vụ")
    servicespage.wait_for_result("Dịch vụ nổi bật")
    servicespage.scroll_to_element2("Thư viện số")
    servicespage.click_by_text("Giáo dục")
    servicespage.click_by_text("Trường học số Quốc gia")
    servicespage.click_button_by_text("icBack")
    servicespage.click_by_text("Cổng thi đại học mobiEdu")
    servicespage.click_button_by_text("icBack")
    servicespage.click_by_text1("Mobistudy")
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
@pytest.mark.tc92_2
def test_click_services_tc92_2(driver):
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
@pytest.mark.tc92_3
def test_click_services_tc92_3(driver):
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
@pytest.mark.tc92_4
def test_click_services_tc92_4(driver):
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
@pytest.mark.tc92_5
def test_click_services_tc92_5(driver):
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
@pytest.mark.tc92_6
def test_click_services_tc92_6(driver):
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
    