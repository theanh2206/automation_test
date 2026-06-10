import pytest
import logging
import os
from datetime import datetime
from appium import webdriver
from appium.options.android import UiAutomator2Options
from selenium.webdriver.support.ui import WebDriverWait
from utils.csv_reporter import CSVReporter


# ========= CONFIG ANDROID =========
DEVICE_UDID = "R83X20ACPQV"
APP_PACKAGE = "vms.com.vn.mymobifone"
APP_ACTIVITY = "vms.com.vn.mymobi.activities.SplashScreenActivity"
APPIUM_URL = "http://127.0.0.1:4723"

CSV_OUTPUT = "reports/test_result.csv"
LOG_FILE = "logs/test_execution.log"


# ========= GLOBAL LOGGER =========
LOGGER = None


def setup_global_logger():
    global LOGGER

    os.makedirs("logs", exist_ok=True)

    today = datetime.now().strftime("%Y-%m-%d")
    log_file = f"logs/{today}.log"

    LOGGER = logging.getLogger("test_execution")
    LOGGER.setLevel(logging.INFO)

    if LOGGER.hasHandlers():
        LOGGER.handlers.clear()

    file_handler = logging.FileHandler(
        log_file,
        encoding="utf-8"
    )

    formatter = logging.Formatter(
        "[%(asctime)s] [%(levelname)s] %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )

    file_handler.setFormatter(formatter)
    LOGGER.addHandler(file_handler)

    return LOGGER


# ================= DRIVER FIXTURE =================
@pytest.fixture(scope="function")
def driver():
    options = UiAutomator2Options()

    # ===== BASIC =====
    options.platform_name = "Android"
    options.device_name = DEVICE_UDID
    options.udid = DEVICE_UDID
    options.automation_name = "UiAutomator2"

    # ===== APP =====
    options.app_package = APP_PACKAGE
    options.app_activity = APP_ACTIVITY

    # ===== PERFORMANCE =====
    options.no_reset = True
    options.auto_launch = True
    options.new_command_timeout = 300

    # ===== CREATE DRIVER =====
    driver = webdriver.Remote(
        APPIUM_URL,
        options=options
    )

    print("✅ ANDROID CONNECTED SUCCESSFULLY")

    driver.implicitly_wait(0)

    wait = WebDriverWait(driver, 20)
    driver.wait = wait

    yield driver

    # ================= CLEANUP =================
    print("🧹 CLEAN APP")

    try:
        driver.terminate_app(APP_PACKAGE)
    except Exception as e:
        print(f"⚠️ terminate_app error: {e}")

    print("🧹 QUIT DRIVER")

    try:
        driver.quit()
    except Exception as e:
        print(f"⚠️ quit error: {e}")


# ================= WAIT FIXTURE =================
@pytest.fixture(scope="function")
def wait(driver):
    return WebDriverWait(driver, 20)


# ================= PYTEST CONFIG =================
def pytest_configure(config):
    config._csv_reporter = CSVReporter(
        device_name=DEVICE_UDID
    )

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

    # ===== CSV =====
    item.config._csv_reporter.add_result(
        nodeid=item.nodeid,
        outcome=report.outcome,
        duration=report.duration,
        phase=report.when,
        message=message
    )

    # ===== LOGGER =====
    global LOGGER
    logger = LOGGER

    test_name = item.nodeid.split("::")[-1]
    duration = round(report.duration, 2)

    # ================= PASS =================
    if report.passed:
        logger.info(
            f"[{test_name}] ✅ PASSED ({duration}s)"
        )

    # ================= FAIL =================
    elif report.failed:
        logger.error(
            f"[{test_name}] ❌ FAILED ({duration}s)"
        )

        # ===== SCREENSHOT =====
        driver = item.funcargs.get("driver")

        if driver:
            try:
                today = datetime.now().strftime("%Y-%m-%d")
                os.makedirs(
                    f"reports/screenshots/{today}",
                    exist_ok=True
                )

                timestamp = datetime.now().strftime("%H%M%S")
                screenshot_path = os.path.join(
                    f"reports/screenshots/{today}",
                    f"{test_name}_{timestamp}.png"
                )

                driver.save_screenshot(
                    screenshot_path
                )

                logger.error(
                    f"📸 Screenshot: {screenshot_path}"
                )

                print(f"📸 Screenshot saved: {screenshot_path}")

            except Exception as e:
                logger.error(
                    f"❌ Screenshot failed: {e}"
                )

        # ===== SHORT ERROR =====
        if hasattr(report.longrepr, "reprcrash"):
            logger.error(
                f"📍 File: {report.longrepr.reprcrash.path}"
            )
            logger.error(
                f"📍 Line: {report.longrepr.reprcrash.lineno}"
            )
            logger.error(
                f"📍 Error: {report.longrepr.reprcrash.message}"
            )
        else:
            logger.error(str(report.longrepr))

    # ================= SKIP =================
    elif report.skipped:
        logger.warning(
            f"[{test_name}] ⚠️ SKIPPED"
        )


# ================= SESSION FINISH =================
def pytest_sessionfinish(session, exitstatus):
    _ = exitstatus

    os.makedirs("reports", exist_ok=True)

    print("🔥 pytest_sessionfinish CALLED")
    print(
        "TOTAL CSV RECORDS:",
        len(session.config._csv_reporter.results)
    )

    # ===== WRITE CSV =====
    try:
        session.config._csv_reporter.write_csv(
            CSV_OUTPUT
        )
        print(f"📄 CSV saved: {CSV_OUTPUT}")
    except Exception as e:
        print(f"❌ CSV write failed: {e}")

    # ===== FLUSH LOG =====
    global LOGGER

    if LOGGER:
        for h in LOGGER.handlers:
            h.flush()