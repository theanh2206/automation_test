from appium.webdriver.common.appiumby import AppiumBy
class LocatorPage:
    BUY_PAKAGE = (AppiumBy.XPATH, '//XCUIElementTypeButton[@name="Mua gói"]')
    SEARCH_BOX = (AppiumBy.XPATH, '//XCUIElementTypeWindow/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeButton')
    SEARCH_BOX1 = (AppiumBy.XPATH, '//XCUIElementTypeTextField[@value="Tìm kiếm"]')
    SEARCH_BOX2 = (AppiumBy.XPATH, '//XCUIElementTypeTextField[@value="Tìm kiếm dịch vụ"]')
    SEARCH_DEALS = (AppiumBy.XPATH, '//XCUIElementTypeTextField[@value="Tìm kiếm ưu đãi"]')
    SEARCH_INPUT = (AppiumBy.XPATH, '//XCUIElementTypeTextField[@value="Tìm kiếm"]')
    AVATA = (AppiumBy.XPATH, '//XCUIElementTypeWindow/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeScrollView/XCUIElementTypeOther[1]/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeImage')
    MENU = (AppiumBy.XPATH, '//XCUIElementTypeButton[@name="ic leftBar blur"]')
    NOTIFICATION = (AppiumBy.XPATH, '//XCUIElementTypeWindow/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeButton')
    REGISTER_BUTTON = (AppiumBy.XPATH, '//XCUIElementTypeApplication[@name="MyMobiFone"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[4]/XCUIElementTypeOther/XCUIElementTypeButton')
    #--Tất cả tiện ích
    INFORMATION = (AppiumBy.XPATH, '(//XCUIElementTypeButton[@name="Button"])[1]')
    INFOR_SUBCRIBER = (AppiumBy.XPATH, '//XCUIElementTypeScrollView/XCUIElementTypeOther[1]/XCUIElementTypeButton')
    INFOR_LOOKUP = (AppiumBy.XPATH, '//XCUIElementTypeScrollView/XCUIElementTypeOther[4]/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeButton')
    BUTTON_BACK = (AppiumBy.XPATH, '//XCUIElementTypeButton[@name="arrow left roaming"]')
    BUTTON_BACK1 = (AppiumBy.XPATH, '//XCUIElementTypeButton[@name="icBack"]')
    DEPOSITE_HISTORY = (AppiumBy.XPATH, '//XCUIElementTypeScrollView/XCUIElementTypeOther[4]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeButton')
    SUBCRIBER_HISTORY = (AppiumBy.XPATH, '//XCUIElementTypeScrollView/XCUIElementTypeOther[4]/XCUIElementTypeOther/XCUIElementTypeOther[3]/XCUIElementTypeButton')
    BUTTON_BUY_PAKAGE = (AppiumBy.XPATH, '//XCUIElementTypeScrollView/XCUIElementTypeOther[5]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[4]')
    KNDL = (AppiumBy.XPATH, '//XCUIElementTypeWindow/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeScrollView/XCUIElementTypeOther[2]/XCUIElementTypeOther[3]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeButton')
    KNDL1 = (AppiumBy.XPATH, '//XCUIElementTypeScrollView/XCUIElementTypeOther[6]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeButton')
    #Đổi số điện thoại con
    INPUT_PHONE = (AppiumBy.XPATH, '//XCUIElementTypeTextField[@value="Số thuê bao"]')
    BUTTON_ACCEPT =(AppiumBy.XPATH, '(//XCUIElementTypeStaticText[@name="Xác nhận"])[2]')
    # Banner
    BANNER = (AppiumBy.XPATH, '//XCUIElementTypeWindow/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeScrollView/XCUIElementTypeOther[2]/XCUIElementTypeOther[5]/XCUIElementTypeOther/XCUIElementTypeCollectionView/XCUIElementTypeCell[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeImage')
    BANNER2 =(AppiumBy.XPATH, '//XCUIElementTypeApplication[@name="MyMobiFone"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeScrollView/XCUIElementTypeOther[2]/XCUIElementTypeOther[5]/XCUIElementTypeOther/XCUIElementTypeCollectionView/XCUIElementTypeCell[2]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeImage')
    BANNER3 =(AppiumBy.XPATH, '//XCUIElementTypeApplication[@name="MyMobiFone"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeScrollView/XCUIElementTypeOther[2]/XCUIElementTypeOther[5]/XCUIElementTypeOther/XCUIElementTypeCollectionView/XCUIElementTypeCell[2]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeImage')
    BANNER_KNDL = (AppiumBy.XPATH, '//XCUIElementTypeScrollView/XCUIElementTypeOther[1]/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeCollectionView/XCUIElementTypeCell[2]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeImage')
    BANNER_SERVICES = (AppiumBy.XPATH, '//XCUIElementTypeWindow/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeScrollView/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeOther/XCUIElementTypeCollectionView/XCUIElementTypeCell[2]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeImage')
    #Tạo gói cước cá nhân
    PERSONAL_FLEX = (AppiumBy.XPATH, '//XCUIElementTypeWindow/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeScrollView/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[3]/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeButton')
    TIME_FLEX = (AppiumBy.XPATH, '//XCUIElementTypeWindow/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeScrollView/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[3]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeButton')
    ICON_CVQT = (AppiumBy.XPATH, '//XCUIElementTypeWindow/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeScrollView/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[3]/XCUIElementTypeOther/XCUIElementTypeOther[3]/XCUIElementTypeButton')
    #Chuyển vùng quốc tế
    SEARCH_COUNTRY = (AppiumBy.XPATH, '//XCUIElementTypeWindow/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[3]')
    SEARCH_COUNTRY1 = (AppiumBy.XPATH, '//XCUIElementTypeTextField[@value="Tìm kiếm quốc gia"]')
    CHECK_TRIP = (AppiumBy.XPATH, '//XCUIElementTypeScrollView/XCUIElementTypeOther[1]/XCUIElementTypeButton')
    #Chia sẻ/tặng gói cước
    PHONE_RECIEVE = (AppiumBy.XPATH, '//XCUIElementTypeTextField[@value="Nhập số điện thoại"]')
    #Mẹo tích điểm 
    SAVE_POINT = (AppiumBy.XPATH, '//XCUIElementTypeStaticText[@name="Mẹo tích điểm"]')
    #Lịch sử điểm
    POINT_HISTORY = (AppiumBy.XPATH, '//XCUIElementTypeStaticText[@name="Lịch sử đơn hàng"]')
    CLOSE = (AppiumBy.XPATH, '//XCUIElementTypeButton[@name="add roam"]')
    BUTTON_CLOSE1 = (AppiumBy.XPATH, '//XCUIElementTypeButton[@name="close dt"]')
    #Đổi ưu đãi
    DEALS_LIST_ALL = (AppiumBy.XPATH, '(//XCUIElementTypeStaticText[@name="Tất cả"])[1]')
    DEALS_LIST_ALL1 = (AppiumBy.XPATH, '(//XCUIElementTypeStaticText[@name="Tất cả"])[2]')
    DEALS_LIST_ALL_OTHER = (AppiumBy.XPATH, '(//XCUIElementTypeStaticText[@name="Tất cả"])[2]')
    DEALS_LIST_ALL_OTHER1 = (AppiumBy.XPATH, '(//XCUIElementTypeStaticText[@name="Tất cả"])[3]')
    #Kết nối dài lâu
    INPUT_MAIL = (AppiumBy.XPATH, '//XCUIElementTypeTextField[@value="Nhập email nhận ưu đãi"]')
    #Hồ sơ cá nhân
    ON_SWITCH_NOTIFICATION = (AppiumBy.XPATH, '//XCUIElementTypeSwitch[@value="1"]')
    OFF_SWITCH_NOTIFICATION = (AppiumBy.XPATH, '(//XCUIElementTypeSwitch[@value="0"])[1]')
    SWITCH_SMART_OTP = (AppiumBy.XPATH, '//XCUIElementTypeSwitch[@value="0"]')
    INPUT_SMART_OTP = (AppiumBy.XPATH, '//XCUIElementTypeSecureTextField[@value="Nhập mã PIN 4 chữ số"]')
    CONFIRM_SMART_OTP = (AppiumBy.XPATH, '//XCUIElementTypeSecureTextField[@value="Xác nhận mã PIN"]')
    ON_SWITCH_SPAM = (AppiumBy.XPATH, '(//XCUIElementTypeSwitch[@value="0"])[1]')
    ON_SWITCH_BLOCK = (AppiumBy.XPATH, '//XCUIElementTypeSwitch[@value="0"]')
    OFF_SWITCH_SPAM = (AppiumBy.XPATH, '(//XCUIElementTypeSwitch[@value="1"])[1]')
    OFF_SWITCH_BLOCK = (AppiumBy.XPATH, '//XCUIElementTypeSwitch[@value="1"]')
    