from selenium.webdriver.common import keys
from selenium.webdriver.common.by import By
from utils.miscellaneous import months
from time import sleep


class SkipLaggedHomeFlightSearchPage:
    _home_header = (By.ID, "home-container")
    _trip_type = (By.XPATH, "//div[@class='skip-select passengers-input-container trip-type-select']//button/span")
    _one_way_trip = (By.XPATH, "//div[contains(text(),'One Way')]")
    _round_trip = (By.XPATH, "//div[contains(text(),'Round Trip')]")
    _source_airport = (By.CLASS_NAME, "src-input")
    _source_airport_auto_complete = (By.XPATH, "//ul[@id='ui-id-1']")
    _destination_airport = (By.CLASS_NAME, "dst-input")
    _destination_airport_auto_complete = (By.XPATH, "//ul[@id='ui-id-2']")
    _current_currency_span = (By.XPATH, "//header//a[@class='dropdown-toggle']/span[@class='currency-code']")
    _currency_dropdown_span = (By.XPATH, "//header//span[@id='currency-dropdown']")
    _currency_name_spans = (By.XPATH, "//header//ul//span[@class='currency-code']")
    _search_flights_button = (By.XPATH, "//button[contains(text(),'Search Flights')]")

    # date picker
    _start_date = (By.XPATH, "//input[@class='date-input start-date hasDatepicker']")
    _end_date = (By.XPATH, "//input[@class='date-input end-date hasDatepicker']")
    _previous_month_span_tag = (By.XPATH, "//span[contains(text(),'Prev')]")

    _next_month_span_tag = (By.XPATH, "//a[@title='Next']")
    _year_span_tag = (By.CLASS_NAME, "ui-datepicker-year")
    _month_span_tag = (By.CLASS_NAME, "ui-datepicker-month")

    _home_header_element = property(lambda self: self.base.find_element(*self._home_header))
    _trip_type_element = property(lambda self: self.base.find_element(*self._trip_type))
    _one_way_trip_drop_down_element = property(lambda self: self.base.find_element(*self._one_way_trip))
    _round_trip_drop_down_element = property(lambda self: self.base.find_element(*self._round_trip))
    _source_airport_input_element = property(lambda self: self.base.find_element(*self._source_airport))
    _source_airport_auto_complete_element = property(
        lambda self: self.base.find_element(*self._source_airport_auto_complete))
    _destination_airport_input_element = property(lambda self: self.base.find_element(*self._destination_airport))
    _destination_airport_auto_complete_element = property(
        lambda self: self.base.find_element(*self._destination_airport_auto_complete))
    _current_currency_span_element = property(lambda self: self.base.find_element(*self._current_currency_span))
    _currency_dropdown_span_element = property(lambda self: self.base.find_element(*self._currency_dropdown_span))
    _currency_name_span_elements = property(lambda self: self.base.find_elements(*self._currency_name_spans))

    # Date picker
    _from_date_input_element = property(lambda self: self.base.find_element(*self._start_date))
    _till_date_input_element = property(lambda self: self.base.find_element(*self._end_date))
    _previous_month_span_element = property(lambda self: self.base.find_element(*self._previous_month_span_tag))
    _next_month_span_element = property(lambda self: self.base.find_element(*self._next_month_span_tag))
    _year_span_elements = property(lambda self: self.base.find_elements(*self._year_span_tag))
    _month_span_elements = property(lambda self: self.base.find_elements(*self._month_span_tag))
    _search_flights_button_element = property(lambda self: self.base.find_element(*self._search_flights_button))

    def __init__(self, base):
        self.base = base

    @property
    def get_skip_lagged_home_page_title(self):
        return self.base.get_page_title

    @property
    def get_current_currency_type(self):
        return self._current_currency_span_element.text

    @property
    def get_all_currency_list(self):
        return map(lambda e: e.text, self._currency_name_span_elements)

    def click_currency_dropdown(self):
        self._currency_dropdown_span_element.click()

    def click_trip_type(self):
        self._trip_type_element.click()

    def click_search_flights(self):
        self._search_flights_button_element.click()

    def click_one_way_trip(self):
        self.click_trip_type()
        self._one_way_trip_drop_down_element.click()

    def click_round_trip(self):
        self.click_trip_type()
        self._round_trip_drop_down_element.click()

    def fill_source_airport_name(self, source_airport_name):
        self._source_airport_input_element.clear()
        self._source_airport_input_element.send_keys(source_airport_name)
        # Wait for auto complete drop down is populated
        self.base.wait_element(self._source_airport_auto_complete)
        # Iterate all results in the drop down and click the one matches with source airport name
        airport_names = self._source_airport_auto_complete_element.find_elements(*self._source_airport_auto_complete)
        for airport_name in airport_names:
            if source_airport_name in airport_name.text:
                airport_name.click()
                break

    def fill_destination_airport_name(self, destination_airport_name):
        self._destination_airport_input_element.clear()
        self._destination_airport_input_element.send_keys(destination_airport_name)
        # Wait for auto complete drop down is populated
        self.base.wait_element(self._destination_airport_auto_complete)
        # Iterate all results in the drop down and click the one matches with destination airport name
        airport_names = self._destination_airport_auto_complete_element.find_elements(
            *self._destination_airport_auto_complete)
        sleep(1)
        for airport_name in airport_names:
            if destination_airport_name in airport_name.text:
                airport_name.click()
                break

    def wait_for_page_to_be_loaded(self):
        self.base.wait_element(self._home_header)

    def pick_a_start_data(self, start_date):
        self._from_date_input_element.click()
        self._date_picker(start_date)

    def pick_a_end_data(self, end_date):
        self._till_date_input_element.click()
        self._date_picker(end_date)

    def select_currency(self, currency):
        how = (By.XPATH, f"//header//span[contains(text(),'{currency}')]")
        is_element_exist = self.base.is_element_exist(*how)
        if is_element_exist:
            self.base.find_element(*how).click()
        else:
            print(f"No element found for //header//span[contains(text(),'{currency}') Xpath]")

    def _date_picker(self, date):
        """
        :param date: must be [full month] [year] [date]
        :example: August 2020 21
        :return:
        """
        [month, year, day] = date.split()
        month_as_number = int(months[month]) - 1
        is_month_and_year_matched = False
        is_next_disabled = False

        while not is_month_and_year_matched and not is_next_disabled:
            is_year_matched = False
            is_month_matched = False

            if not is_year_matched:
                for year_span_element in self._year_span_elements:
                    if year_span_element.text == year:
                        is_year_matched = True

            if not is_month_matched:
                for month_span_element in self._month_span_elements:
                    if month_span_element.text == month:
                        is_month_matched = True

            if is_month_matched and is_year_matched:
                is_month_and_year_matched = True
            else:
                self._next_month_span_element.click()

            is_next_disabled = "ui-state-disabled" in self._next_month_span_element.get_attribute("class")

        if not is_next_disabled:
            _day_a_tag = (
                By.XPATH, f"//td[@data-month='{month_as_number}' and @data-year='{year}']/a[contains(text(),'{day}')]")
            _day_a_tag_element = self.base.find_element(*_day_a_tag)
            _day_a_tag_element.click()
