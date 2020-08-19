from selenium import webdriver
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class FaceBookPage():
    email = (By.XPATH, "//div[@class='header-left']//span[contains(text(),'skiplagged')]")

    def __init__(self, base_page):
        self.base_page = base_page

    def fill_email(self, email: str):
        self.base_page.find_element(*self.email).send_keys(email)

    def wait_for_page_to_be_loaded(self):
        self.base_page.wait_element(self.email)


class BasePage():

    def __init__(self, driver: webdriver, default_time_out=30):
        self.driver = driver
        self.default_time_out = default_time_out
        self.wait = WebDriverWait(self.driver, default_time_out)

    def navigate_to_url(self, url):
        self.driver.get(url)

    @property
    def get_page_title(self):
        return self.driver.title

    def quit_browser(self):
        self.driver.quit()

    def find_element(self, *selector):
        try:
            return self.driver.find_element(*selector)
        except NoSuchElementException as ex:
            print(f"\nError {ex.msg}")

    def is_element_exist(self, *selector):
        try:
            self.driver.find_element(*selector)
            return True
        except Exception:
            return False

    def find_elements(self, *selector):
        return self.driver.find_elements(*selector)

    def wait_element(self, *element):
        try:
            self.wait.until(EC.visibility_of_element_located(*element))
        except TimeoutException:
            print(f"\n * Element not found within given time")
    print(f"\n * Element not found within given time")
