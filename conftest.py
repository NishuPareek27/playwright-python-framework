# import os
# import pytest
# from playwright.sync_api import sync_playwright
# from utils.logger import get_logger
# from config.config import BASE_URL, BROWSER, HEADLESS

# logger = get_logger()

# @pytest.fixture
# def page():

#     with sync_playwright() as p:

#         if BROWSER == "chromium":
#             browser = p.chromium.launch(headless=HEADLESS)
        
#         elif BROWSER == "firefox":
#             browser = p.firefox.launch(headless=HEADLESS)
        
#         elif BROWSER == "webkit":
#             browser = p.webkit.launch(headless=HEADLESS)
        
#         context = browser.new_context(
#             user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
#                        "(KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
#             viewport={"width": 1920, "height": 1080}
#         )
#         page = context.new_page()

#         yield page

#         browser.close()


# # This Hook is used to caputre screenshots on test failure and save them in the "screenshots" folder
# @pytest.hookimpl(hookwrapper=True)
# def pytest_runtest_makereport(item, call):

#     outcome = yield
#     report = outcome.get_result()

#     if report.when == "call" and report.failed:

#         page = item.funcargs.get("page")

#         if page:
        
#             os.makedirs("screenshots", exist_ok=True)

#             screenshot_path = f"screenshots/{item.name}.png"

#             page.screenshot(path=screenshot_path)

#             logger.error(
#                 f"Test Failed. Screenshot saved: {screenshot_path}"
#             )


import os
import pytest
import allure
import re

from playwright.sync_api import sync_playwright

from utils.logger import get_logger
from config.config import BASE_URL, BROWSER, HEADLESS


logger = get_logger()


# ============================================================
# Directories
# ============================================================

SCREENSHOT_DIR = "screenshots"
TRACE_DIR = "traces"
VIDEO_DIR = "videos"

os.makedirs(SCREENSHOT_DIR, exist_ok=True)
os.makedirs(TRACE_DIR, exist_ok=True)
os.makedirs(VIDEO_DIR, exist_ok=True)


# ============================================================
# Page Fixture
# ============================================================

@pytest.fixture
def page():

    with sync_playwright() as p:

        # ----------------------------------------------------
        # Launch Browser
        # ----------------------------------------------------

        if BROWSER == "chromium":
            browser = p.chromium.launch(
                headless=HEADLESS
            )

        elif BROWSER == "firefox":
            browser = p.firefox.launch(
                headless=HEADLESS
            )

        elif BROWSER == "webkit":
            browser = p.webkit.launch(
                headless=HEADLESS
            )

        else:
            raise ValueError(
                f"Unsupported browser: {BROWSER}"
            )

        # ----------------------------------------------------
        # Create Context
        # ----------------------------------------------------

        context = browser.new_context(

            user_agent=(
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                "AppleWebKit/537.36 "
                "(KHTML, like Gecko) "
                "Chrome/120.0.0.0 Safari/537.36"
            ),

            viewport={
                "width": 1920,
                "height": 1080
            },

            # Record video
            record_video_dir=VIDEO_DIR
        )

        # ----------------------------------------------------
        # Start Playwright Trace
        # ----------------------------------------------------

        context.tracing.start(
            screenshots=True,
            snapshots=True,
            sources=True
        )

        # ----------------------------------------------------
        # Create Page
        # ----------------------------------------------------

        page = context.new_page()

        yield page

        # ----------------------------------------------------
        # Cleanup
        # ----------------------------------------------------

        context.close()
        browser.close()


# ============================================================
# Pytest Hook - Failure Handling
# ============================================================

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):

    outcome = yield

    report = outcome.get_result()

    # We only want to handle actual test failures
    if report.when == "call" and report.failed:

        page = item.funcargs.get("page")

        if page:

            test_name = item.name

            # ------------------------------------------------
            # Screenshot
            # ------------------------------------------------

            screenshot_path = (
                f"{SCREENSHOT_DIR}/{test_name}.png"
            )

            try:

                page.screenshot(
                    path=screenshot_path,
                    full_page=True
                )

                logger.error(
                    f"Test Failed. "
                    f"Screenshot saved: {screenshot_path}"
                )

                # Attach screenshot to Allure
                allure.attach.file(
                    screenshot_path,
                    name="Failure Screenshot",
                    attachment_type=allure.attachment_type.PNG
                )

            except Exception as e:

                logger.error(
                    f"Could not capture screenshot: {e}"
                )

            # ------------------------------------------------
            # Current URL
            # ------------------------------------------------

            try:

                allure.attach(
                    page.url,
                    name="Failure URL",
                    attachment_type=allure.attachment_type.TEXT
                )

            except Exception as e:

                logger.error(
                    f"Could not attach URL: {e}"
                )

            # ------------------------------------------------
            # Playwright Trace
            # ------------------------------------------------

            safe_name = (
                re.sub(r"[^a-zA-Z0-9_-]", "_", item.name)
            )

            trace_path = (
                f"{TRACE_DIR}/{safe_name}.zip"
            )

            try:

                # Stop tracing and save it
                page.context.tracing.stop(
                    path=trace_path
                )

                logger.error(
                    f"Playwright trace saved: {trace_path}"
                )

                # Attach trace to Allure
                allure.attach.file(
                    trace_path,
                    name="Playwright Trace",
                    attachment_type="application/zip"
                )

            except Exception as e:

                logger.error(
                    f"Could not save trace: {e}"
                )
