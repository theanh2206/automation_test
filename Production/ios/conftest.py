import pytest
import logging
import os
from appium import webdriver
from appium.options.android import UiAutomator2Options
from selenium.webdriver.support.ui import WebDriverWait
from appium.options.ios import XCUITestOptions
from utils.csv_reporter import CSVReporter

# ========= CONFIG ANDROID =========
DEVICE_UDID = "auto"
BUNDLE_ID = "vms.com.MyMobifone"
APPIUM_URL = "http://127.0.0.1:4723"
TEAM_ID = "2LSM987Q67"
WDA_BUNDLE_ID = "com.truong.wda"

CSV_OUTPUT = "reports/test_result.csv"
LOG_FILE = "logs/test_execution.log"

# ========= GLOBAL LOGGER =========
LOGGER = None


def setup_global_logger():
    global LOGGER

    os.makedirs("logs", exist_ok=True)

    LOGGER = logging.getLogger("test_execution")
    LOGGER.setLevel(logging.INFO)

    # clear handler cũ nếu có
    if LOGGER.hasHandlers():
        LOGGER.handlers.clear()

    file_handler = logging.FileHandler(LOG_FILE, encoding="utf-8")

    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)s | %(message)s"
    )

    file_handler.setFormatter(formatter)
    LOGGER.addHandler(file_handler)

    return LOGGER


# ================= DRIVER FIXTURE =================
@pytest.fixture(scope="function")
def driver():
    options = XCUITestOptions()
    # ===== BASIC =====
    options.platform_name = "iOS"
    options.device_name = "iPhone 13"
    options.udid = DEVICE_UDID
    options.automation_name = "XCUITest"
    # ===== APP =====
    options.bundle_id = BUNDLE_ID
    # ===== SIGNING =====
    options.xcode_org_id = TEAM_ID
    options.xcode_signing_id = "Apple Development"
    options.updated_wda_bundle_id = WDA_BUNDLE_ID
    # ===== WDA =====
    options.use_prebuilt_wda = True
    options.use_new_wda = False
    # ===== PERFORMANCE =====
    options.no_reset = True
    options.new_command_timeout = 300
    # 👉 QUAN TRỌNG: đảm bảo mỗi test launch lại app
    options.force_app_launch = True
    options.should_terminate_app = True
    # 👉 timeout WDA
    options.wda_launch_timeout = 60000
    options.wda_connection_timeout = 60000
    options.should_use_singleton_test_manager = False
    driver = webdriver.Remote(APPIUM_URL, options=options)
    print("✅ iOS CONNECTED SUCCESSFULLY")
    wait = WebDriverWait(driver, 20)
    driver.wait = wait
    yield driver
    print("🧹 CLEAN APP")
    try:
        # 👉 kill app sau mỗi test
        driver.terminate_app(BUNDLE_ID)
    except:
        pass
    print("🧹 QUIT DRIVER")
    driver.quit()


@pytest.fixture(scope="function")
def wait(driver):
    return WebDriverWait(driver, 20)


# ================= PYTEST CONFIG =================
def pytest_configure(config):
    # CSV reporter
    config._csv_reporter = CSVReporter(device_name=DEVICE_UDID)

    # ✅ INIT LOGGER ĐÚNG CHỖ
    setup_global_logger()


# ================= MAIN REPORT HOOK =================
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when != "call" and not report.skipped:
        return
    message = ""
    if report.failed:
        message = str(report.longrepr)
    elif report.skipped:
        message = str(report.longrepr)

    item.config._csv_reporter.add_result(
        nodeid=item.nodeid,
        outcome=report.outcome,
        duration=report.duration,
        phase=report.when,
        message=message
    )

    # ===== LOG =====
    global LOGGER
    logger = LOGGER

    test_name = item.nodeid.split("::")[-1]
    duration = round(report.duration, 2)

    if report.passed:
        logger.info(f"[{test_name}] ✅ PASSED ({duration}s)")

    elif report.failed:
        logger.error(f"[{test_name}] ❌ FAILED ({duration}s)")

        if hasattr(report.longrepr, "reprcrash"):
            logger.error(f"📍 File: {report.longrepr.reprcrash.path}")
            logger.error(f"📍 Line: {report.longrepr.reprcrash.lineno}")
            logger.error(f"📍 Error: {report.longrepr.reprcrash.message}")
        else:
            logger.error(str(report.longrepr))

    elif report.skipped:
        logger.warning(f"[{test_name}] ⚠️ SKIPPED")


# ================= SESSION FINISH =================
def pytest_sessionfinish(session, exitstatus):
    _ = exitstatus
    os.makedirs("reports", exist_ok=True)

    print("🔥 pytest_sessionfinish CALLED")
    print("TOTAL CSV RECORDS:", len(session.config._csv_reporter.results))

    # CSV
    try:
        session.config._csv_reporter.write_csv(CSV_OUTPUT)
        print(f"📄 CSV saved: {CSV_OUTPUT}")
    except Exception as e:
        print(f"❌ CSV write failed: {e}")

    # ✅ flush log
    global LOGGER
    if LOGGER:
        for h in LOGGER.handlers:
            h.flush()