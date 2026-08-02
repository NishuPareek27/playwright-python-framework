import pytest
from playwright.sync_api import expect
from pages.login_page import LoginPage
from pages.home_page import HomePage
from config.config import BASE_URL
from testdata.login_data import INVALID_LOGIN_DATA


# Test to verify the homepage title and print a success message after launching the homepage
def test_homepage(page):
    page.goto(BASE_URL)

    page.wait_for_load_state(state="load")

    expect(page).to_have_title("Automation Exercise")

    print("Homepage launched successfully")
