import os
import pytest
from playwright.sync_api import sync_playwright
from utils.logger import get_logger
from config.config import BASE_URL, BROWSER, HEADLESS

logger = get_logger()

@pytest.fixture
def page():

    with sync_playwright() as p:

        if BROWSER == "chromium":
            browser = p.chromium.launch(headless=HEADLESS)
        
        elif BROWSER == "firefox":
            browser = p.firefox.launch(headless=HEADLESS)
        
        elif BROWSER == "webkit":
            browser = p.webkit.launch(headless=HEADLESS)
        
        page = browser.new_page()

        yield page

        page.close()
        browser.close()


# This Hook is used to caputre screenshots on test failure and save them in the "screenshots" folder
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):

    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:

        page = item.funcargs.get("page")

        if page:
        
            os.makedirs("screenshots", exist_ok=True)

            screenshot_path = f"screenshots/{item.name}.png"

            page.screenshot(path=screenshot_path)

            logger.error(
                f"Test Failed. Screenshot saved: {screenshot_path}"
            )