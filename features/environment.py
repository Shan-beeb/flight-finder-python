import os, sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), '.'))
from selenium import webdriver
from pages.base import BasePage


def before_scenario(context, scenario):
    driver = webdriver.Firefox(executable_path='../drivers/geckodriver.exe')
    page = BasePage(driver)
    context.page = page


def after_scenario(context, scenario):
    context.page.quit_browser()
