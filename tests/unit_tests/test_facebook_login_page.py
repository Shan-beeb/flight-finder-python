import pytest
import subprocess
from pages.base import BasePage
from selenium import webdriver
from pages.skiplagged_home_page import SkipLaggedHomeFlightSearchPage
from time import sleep


def test_test_base_page_functionality():
    driver = webdriver.Chrome(executable_path="../../drivers/chromedriver.exe")
    page = BasePage(driver)
    skip_lagged_home_page = SkipLaggedHomeFlightSearchPage(page)
    page.navigate_to_url("https://skiplagged.com/")
    skip_lagged_home_page.wait_for_page_to_be_loaded()
    #skip_lagged_home_page.click_trip_type()
    #skip_lagged_home_page.click_one_way_trip()
    #face_book.fill_email("kar@gmail.com")
    skip_lagged_home_page.fill_source_airport_name("NYC")
    skip_lagged_home_page.fill_destination_airport_name("CMB")
    skip_lagged_home_page.pick_a_start_data("December 2020 20")
    skip_lagged_home_page.pick_a_end_data("March 2020 20")
    sleep(5)
    page.quit_browser()
    PROCNAME = "chromedriver.exe"
    subprocess.call(f"taskkill /IM {PROCNAME} /F")
    

