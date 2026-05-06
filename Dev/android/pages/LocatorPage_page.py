from appium.webdriver.common.appiumby import AppiumBy

class LocatorPage:
    BUY_PAKAGE = (AppiumBy.XPATH, '//android.widget.LinearLayout[@resource-id="vms.com.vn.mymobifone:id/bottomBar"]/android.widget.LinearLayout/android.widget.FrameLayout[2]')
    SEARCH_BOX = (AppiumBy.ID, "vms.com.vn.mymobifone:id/etSearch4x")
    SEARCH_BOX1 = (AppiumBy.ID, "vms.com.vn.mymobifone:id/etSearch")
    SEARCH_DEALS = (AppiumBy.ID, "vms.com.vn.mymobifone:id/tvSearchDeal")
    SEARCH_INPUT = (AppiumBy.CLASS_NAME, "android.widget.EditText")
    AVATA = (AppiumBy.ID, "vms.com.vn.mymobifone:id/ivAvatar")
    MENU = (AppiumBy.ID, "vms.com.vn.mymobifone:id/ivMenu")
    NOTIFICATION = (AppiumBy.ID, "vms.com.vn.mymobifone:id/ivNotification")
    DETAIL_D5 = (AppiumBy.XPATH, '//android.widget.TextView[@resource-id="vms.com.vn.mymobifone:id/tvPackName" and @text="D5"]')
    REGISTER_BUTTON = (AppiumBy.ID, "vms.com.vn.mymobifone:id/tvRegister")
    BUTTON_CANCEL = (AppiumBy.ID, "vms.com.vn.mymobifone:id/tvCancelPackage")
    BUTTON_CONTINUTE = (AppiumBy.ID, "vms.com.vn.mymobifone:id/btContinue")
    BUTTON_CONTINUTE1 = (AppiumBy.ID, "vms.com.vn.mymobifone:id/tvContinue")
    BACKGROUND = (AppiumBy.ID, "vms.com.vn.mymobifone:id/tvBack")
    BUTTON_SEE_ALL = (AppiumBy.ID, "vms.com.vn.mymobifone:id/tvSeeAll")
    RECHARGE = (AppiumBy.ID, "vms.com.vn.mymobifone:id/tvRecharge")
    BUTTON_LOGIN = (AppiumBy.ID, "vms.com.vn.mymobifone:id/btLogin")
    #---Dịch vụ mobigames
    MOBIGAMES_DETAIL = (AppiumBy.ID, "vms.com.vn.mymobifone:id/ivThumb")
    MOBIGAMES_REGISTER1 = (AppiumBy.XPATH, '(//android.widget.TextView[@resource-id="vms.com.vn.mymobifone:id/tvRegister"])[1]')
    MOBIGAMES_REGISTER2 = (AppiumBy.ID, "vms.com.vn.mymobifone:id/btContinue")
    MOBIGAME_UNREGISTER = (AppiumBy.XPATH, '//android.widget.TextView[@resource-id="vms.com.vn.mymobifone:id/tvRegister" and @text="Hủy"]')
    #---Gói cước của bạn
    BUTTON_EXTEND = (AppiumBy.ID, "vms.com.vn.mymobifone:id/tvExtendPackage")
    BUTTON_CANCEL_EXTEND = (AppiumBy.ID,"vms.com.vn.mymobifone:id/tvCancelExtendPackage")
    DETAIL_MY_PAKAGE = (AppiumBy.XPATH, '//android.widget.RelativeLayout[@resource-id="vms.com.vn.mymobifone:id/rlPB4"]')
    BUTTON_CONFIRM_EXTEND = (AppiumBy.ID, "vms.com.vn.mymobifone:id/tvConfirmExtend")
    BUTTON_CONFIRM_CANCEL_EXTEND = (AppiumBy.ID, "vms.com.vn.mymobifone:id/tvConfirmCancelExtend")
    #-- Thông tin sử dụng/tiện ích nổi bật
    CVQT = (AppiumBy.XPATH, '(//android.widget.ImageView[@resource-id="vms.com.vn.mymobifone:id/ivIcon"])[1]')
    KNDL1 = (AppiumBy.XPATH, '(//android.widget.ImageView[@resource-id="vms.com.vn.mymobifone:id/ivIcon"])[4]')
    VTC83 = (AppiumBy.XPATH, '(//android.widget.ImageView[@resource-id="vms.com.vn.mymobifone:id/ivIcon"])[5]')
    KHS = (AppiumBy.XPATH, '(//android.widget.ImageView[@resource-id="vms.com.vn.mymobifone:id/ivIcon"])[6]')
    BUTTON_BACK_LEFT = (AppiumBy.ID, "vms.com.vn.mymobifone:id/ivLeftIcon")
    #--Tiện ích của bạn

    #--Tất cả tiện ích
    VIEW_ALL_UTILS = (AppiumBy.ID, "vms.com.vn.mymobifone:id/tvViewAllUtils")
    BTN_CANCEL = (AppiumBy.ID, "vms.com.vn.mymobifone:id/btCancel")
    INFORMATION = (AppiumBy.ID, "vms.com.vn.mymobifone:id/llUsageInfos")
    INFOR_SUBCRIBER = (AppiumBy.ID, "vms.com.vn.mymobifone:id/ivArrowInfo")
    INFOR_LOOKUP = (AppiumBy.XPATH, '//android.widget.LinearLayout[@resource-id="vms.com.vn.mymobifone:id/lineCheckCharges"]/android.widget.ImageView')
    BUTTON_BACK = (AppiumBy.ID, "vms.com.vn.mymobifone:id/ivBack")
    BUTTON_UP = (AppiumBy.ID, "vms.com.vn.mymobifone:id/ivUp")
    DEPOSITE_HISTORY = (AppiumBy.XPATH, '//android.widget.LinearLayout[@resource-id="vms.com.vn.mymobifone:id/lineHistoryTopup"]/android.widget.ImageView')
    SUBCRIBER_HISTORY = (AppiumBy.XPATH, '//android.widget.LinearLayout[@resource-id="vms.com.vn.mymobifone:id/lineHistoryPackage"]/android.widget.ImageView')
    BUTTON_BUY_PAKAGE = (AppiumBy.ID, "vms.com.vn.mymobifone:id/tvBuyPackage")
    BUTTON_REGISTER_KNDL = (AppiumBy.ID, "vms.com.vn.mymobifone:id/bvRegKNDL")
    KNDL = (AppiumBy.ID, "vms.com.vn.mymobifone:id/ivCardLoyalty")
    # Hẹn roaming
    BUTTON_RESHEDULE = (AppiumBy.ID, "vms.com.vn.mymobifone:id/btnDoiLichHen")
    BUTTON_CANCEL_SCHEDULE = (AppiumBy.ID, "vms.com.vn.mymobifone:id/btnHuyRoaming")
    BUTTON_SUBMIT = (AppiumBy.ID, "vms.com.vn.mymobifone:id/btnSubmit")
    ET_TIME = (AppiumBy.ID, "vms.com.vn.mymobifone:id/etTime")
    BUTTON_SCHEDULE_ROAMING =(AppiumBy.ID, "vms.com.vn.mymobifone:id/tvRoamingV2")
    #Liên hệ tư vấn
    BUTTON_CONTACT_CONSULTING = (AppiumBy.ID, "vms.com.vn.mymobifone:id/tvContactConsultingV2")
    PHONE_NUMBER = (AppiumBy.ID, "vms.com.vn.mymobifone:id/tvPhoneNumber")
    DAY_CONTACT = (AppiumBy.ID, "vms.com.vn.mymobifone:id/relaSelectDay")
    TIME_CONTACT = (AppiumBy.ID, "vms.com.vn.mymobifone:id/relaShowSelectTime")
    SELECT_TIME = (AppiumBy.ID, "vms.com.vn.mymobifone:id/tvTime15To17")
    BOOK = (AppiumBy.ID, "vms.com.vn.mymobifone:id/tvSchedule")
    #Đổi số điện thoại con
    CHANGE_NUMBER = (AppiumBy.XPATH, '//android.widget.LinearLayout[@resource-id="vms.com.vn.mymobifone:id/llChangeNumber"]/android.widget.ImageView')
    NEW_NUMBER = (AppiumBy.XPATH, '(//android.widget.RelativeLayout[@resource-id="vms.com.vn.mymobifone:id/rlView"])[2]')
    ADD_PHONE = (AppiumBy.ID, "vms.com.vn.mymobifone:id/rlAddPhone")
    INPUT_PHONE = (AppiumBy.ID, "vms.com.vn.mymobifone:id/etPhoneNumber")
    BUTTON_ACCEPT =(AppiumBy.ID, "vms.com.vn.mymobifone:id/btAccept")
    # Banner
    BANNER = (AppiumBy.XPATH, '//android.widget.ImageView[@resource-id="vms.com.vn.mymobifone:id/ivBannerService"]')
    
    #Tạo gói cước cá nhân
    PERSONAL_FLEX = (AppiumBy.ID, "vms.com.vn.mymobifone:id/rlPersonalFlex")
    TIME_FLEX = (AppiumBy.ID, "vms.com.vn.mymobifone:id/rlTimeFlex")
    ICON_CVQT = (AppiumBy.ID, "vms.com.vn.mymobifone:id/rlCvqt")
    BUTTON_CREATE_PAKAGE =(AppiumBy.ID, "vms.com.vn.mymobifone:id/btCreatePackage")
    PAYMENT_CONFIRM = (AppiumBy.ID, "vms.com.vn.mymobifone:id/tvPaymentConfirm")
    REGISTER_BUTTON2 = (AppiumBy.ID, "vms.com.vn.mymobifone:id/btRegister")
    
    #Chuyển vùng quốc tế
    SEARCH_COUNTRY = (AppiumBy.ID, "vms.com.vn.mymobifone:id/tvSearchCountry")
    SEARCH_BY_KEY = (AppiumBy.ID, "vms.com.vn.mymobifone:id/etSearchByKey")
    SEARCH_COUNTRY1 = (AppiumBy.ID, "vms.com.vn.mymobifone:id/etSearch")
    BUTTON_APPLY = (AppiumBy.ID, "vms.com.vn.mymobifone:id/tvApply")
    CHECK_TRIP = (AppiumBy.XPATH, '//android.widget.TextView[@text="Kiểm tra trước chuyến đi"]')
    PAKAGE_ROAMING = (AppiumBy.ID, "vms.com.vn.mymobifone:id/tvMsgPackageRoamFlexCreate")
    CREATE_PAKAGE_ROAMING = (AppiumBy.ID, "vms.com.vn.mymobifone:id/tvCreatePackageRoamFlex")
    
    #Chọn chu kỳ gói cước
    RADIO_BUTTON_ALL = (AppiumBy.ID, "vms.com.vn.mymobifone:id/rbAll")
    RADIO_BUTTON_DAYS = (AppiumBy.ID, "vms.com.vn.mymobifone:id/rbDays")
    RADIO_BUTTON_MONTHS = (AppiumBy.ID, "vms.com.vn.mymobifone:id/rbMonths")
    
    #Bộ lọc theo giá, dung lượng
    SORT_PRICE = (AppiumBy.ID, "vms.com.vn.mymobifone:id/tvSortingPrice")
    SORT_DATA = (AppiumBy.ID, "vms.com.vn.mymobifone:id/tvSortingData")
    
    #Màn tất cả gói cước
    VIEW_ALL_PAKAGE = (AppiumBy.ID, "vms.com.vn.mymobifone:id/llViewAll")
    BUTTON_DETAIL = (AppiumBy.ID, "vms.com.vn.mymobifone:id/tvDetail")
    
    #Chia sẻ/tặng gói cước
    GIFT = (AppiumBy.ID, "vms.com.vn.mymobifone:id/ivGift")
    PHONE_RECIEVE = (AppiumBy.ID, "vms.com.vn.mymobifone:id/etPhone")
    GIFT_CONFIRM = (AppiumBy.ID, "vms.com.vn.mymobifone:id/btConfirm")
    ICON_SHARE = (AppiumBy.ID, "vms.com.vn.mymobifone:id/ivShare")
    BUTTON_SHARE = (AppiumBy.ID, "vms.com.vn.mymobifone:id/tvShare")
    
    #Mẹo tích điểm 
    SAVE_POINT = (AppiumBy.ID, "vms.com.vn.mymobifone:id/tvTipsSavePoint")
    
    #Lịch sử điểm
    POINT_HISTORY = (AppiumBy.ID, "vms.com.vn.mymobifone:id/tvHistoryPoint")
    CART_HISTORY = (AppiumBy.ID, "vms.com.vn.mymobifone:id/tvHistoryCart")
    CLOSE = (AppiumBy.ID, "vms.com.vn.mymobifone:id/ivClose")
    BUTTON_CLOSE = (AppiumBy.ID, "vms.com.vn.mymobifone:id/btClose")
    #Đổi ưu đãi
    BUTTON_EXCHANGE = (AppiumBy.ID, "vms.com.vn.mymobifone:id/bvExchange")
    DEALS_LIST_ALL = (AppiumBy.ID, "vms.com.vn.mymobifone:id/tvDealListAll")
    DEALS_LIST_ALL_OTHER = (AppiumBy.ID, "vms.com.vn.mymobifone:id/tvDealListAllOther")
    
    #Kết nối dài lâu
    ADD_PAKAGE = (AppiumBy.ID, "vms.com.vn.mymobifone:id/btAdd")
    EXCHANGE_POINT = (AppiumBy.ID, "vms.com.vn.mymobifone:id/bvExchanage")
    BUY_NOW = (AppiumBy.ID, "vms.com.vn.mymobifone:id/tvBuyNow")
    KNDL_CONFIRM = (AppiumBy.ID, "vms.com.vn.mymobifone:id/btnConfirm")
    BUTTON_SEE_MORE = (AppiumBy.ID, "vms.com.vn.mymobifone:id/rlSeeMore")
    BUTTON_REFESH = (AppiumBy.ID, "vms.com.vn.mymobifone:id/ivUpdateRefresh")
    INPUT_MAIL = (AppiumBy.ID, "vms.com.vn.mymobifone:id/etEmail")
    
    #Hồ sơ cá nhân
    BUTTON_DETAIL1 = (AppiumBy.ID, "vms.com.vn.mymobifone:id/bvDetails")
    BUTTON_DELETE = (AppiumBy.ID, "vms.com.vn.mymobifone:id/btDelete")
    SELECT_DATE = (AppiumBy.ID, "vms.com.vn.mymobifone:id/tvMonthYear")
    BUTTON_OK = (AppiumBy.ID, "android:id/button1")
    BUTTON_FILLTER = (AppiumBy.ID, "vms.com.vn.mymobifone:id/btFilter")
    ICON_BIN =(AppiumBy.ID, "vms.com.vn.mymobifone:id/ivBin")
    BUTTON_UPDATE = (AppiumBy.ID, "vms.com.vn.mymobifone:id/btUpdate")
    SWITCH_LANGUAGE = (AppiumBy.ID, "vms.com.vn.mymobifone:id/jtbSwitchLanguage")
    SWITCH_NOTIFICATION = (AppiumBy.ID, "vms.com.vn.mymobifone:id/switchNotification")
    SMART_OTP = (AppiumBy.ID, "vms.com.vn.mymobifone:id/rlSmartOtp")
    SWITCH_SMART_OTP = (AppiumBy.ID, "vms.com.vn.mymobifone:id/switchSmartOtp")
    INPUT_SMART_OTP = (AppiumBy.ID, "vms.com.vn.mymobifone:id/etPassword")
    CONFIRM_SMART_OTP = (AppiumBy.ID, "vms.com.vn.mymobifone:id/etConfirmPass")
    SWITCH_SPAM = (AppiumBy.XPATH, '//android.widget.Switch[@resource-id="vms.com.vn.mymobifone:id/switchOnOffSpam"]')
    SWITCH_BLOCK = (AppiumBy.XPATH, '//android.widget.Switch[@resource-id="vms.com.vn.mymobifone:id/switchOnOffBlock"]')