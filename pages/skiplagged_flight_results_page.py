from selenium.webdriver.common.by import By


class SkipLaggedFlightResultsPage:
    # Selectors
    _duration_tab_button = (By.XPATH, "//button[contains(text(),'Price') and @class='active']")

    # Web elements
    _duration_tab_button_element = property(lambda self: self.base.find_element(*self._duration_tab_button))

    def __init__(self, base):
        self.base = base

    def wait_for_page_to_be_loaded(self):
        self.base.wait_element(self._duration_tab_button)
