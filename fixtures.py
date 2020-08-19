from behave.fixture import fixture, use_fixture_by_tag
from selenium import webdriver

from pages.base import BasePage





@fixture
def browser_chrome(context):
    driver = webdriver.Chrome(executable_path="C:\\Users\\K14\\Desktop\\Repos\\flight-finder-python\\drivers\\chromedriver.exe")
    page = BasePage(driver)
    context.page = page
    yield context.page
    page.quit_browser()


def before_all(context):
    context.page.naviage_to_url("https://www.google.com")


fixture_registry = {
    "fixture.page": browser_chrome,

}
