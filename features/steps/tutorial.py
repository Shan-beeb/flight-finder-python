from behave import given, when, then
from collections import Counter
from time import sleep

# URL initializer
from pages.skiplagged_flight_results_page import SkipLaggedFlightResultsPage
from pages.skiplagged_home_page import SkipLaggedHomeFlightSearchPage


@given('a user is in skiplagged.com')
def step_impl(context):
    context.page.navigate_to_url("https://www.skiplagged.com")
    context.skipLagged_home_page = SkipLaggedHomeFlightSearchPage(context.page)
    context.skipLagged_home_page.wait_for_page_to_be_loaded()


@when('we implement a test')
def step_impl(context):
    assert True is not False
    print(f"Hi")


@then('behave will test it for us!')
def step_impl(context):
    assert context.failed is False


@when("a user selects round trip")
def user_selects_round_trip(context):
    context.skipLagged_home_page.click_round_trip()


@when("a user selects one way trip")
def user_selects_one_way_trip(context):
    context.skipLagged_home_page.click_one_way_trip()


@when("a user selects '{source_airport}' as source airport")
def user_selects_source_airport(context, source_airport):
    context.skipLagged_home_page.fill_source_airport_name(source_airport)


@when("a user selects '{destination_airport}' as destination airport")
def user_selects_destination_airport(context, destination_airport):
    context.skipLagged_home_page.fill_destination_airport_name(destination_airport)


@when("a user selects '{departure_date}' as date of departure")
def user_selects_departure_date(context, departure_date):
    context.skipLagged_home_page.pick_a_start_data(departure_date)


@when("a user selects '{arrival_date}' as date of arrival")
def user_selects_arrival_date(context, arrival_date):
    context.skipLagged_home_page.pick_a_end_data(arrival_date)


@when("a user selects {source_airport}, {destination_airport}, and {departure_date}")
def step_impl(context, source_airport, destination_airport, departure_date):
    user_selects_one_way_trip(context)
    user_selects_source_airport(context, source_airport)
    user_selects_destination_airport(context, destination_airport)
    user_selects_departure_date(context, departure_date)
    # context.skipLagged_home_page.click_one_way_trip()
    # context.skipLagged_home_page.fill_source_airport_name(source_airport)
    # context.skipLagged_home_page.fill_destination_airport_name(destination_airport)
    # context.skipLagged_home_page.pick_a_start_data(departure_date)


@when("a user selects {source_airport}, {destination_airport}, {departure_date} and {arrival_date}")
def step_impl(context, source_airport, destination_airport, departure_date, arrival_date):
    user_selects_round_trip(context)
    user_selects_source_airport(context, source_airport)
    user_selects_destination_airport(context, destination_airport)
    user_selects_departure_date(context, departure_date)
    user_selects_arrival_date(context, arrival_date)
    # context.skipLagged_home_page.click_round_trip()
    # context.skipLagged_home_page.fill_source_airport_name(source_airport)
    # context.skipLagged_home_page.fill_destination_airport_name(destination_airport)
    # context.skipLagged_home_page.pick_a_start_data(departure_date)
    # context.skipLagged_home_page.pick_a_end_data(arrival_date)


@then("skiplagged.com page title should be '{page_title}'")
def step_impl(context, page_title):
    assert page_title == context.skipLagged_home_page.get_skip_lagged_home_page_title


@then("default currency would be '{current_currency}'")
def step_impl(context, current_currency):
    assert current_currency == context.skipLagged_home_page.get_current_currency_type


@when("a user selects currency options")
def step_impl(context):
    context.skipLagged_home_page.click_currency_dropdown()


@then("a user should be seeing the following currency list")
def step_impl(context):
    assert Counter(map(lambda e: e['Currency'], context.table)) == Counter(
        context.skipLagged_home_page.get_all_currency_list)


@then("a user should be able to select '{currency}' as currency")
def step_impl(context, currency):
    context.skipLagged_home_page.select_currency(currency)


@when("a user clicks on search flights button")
def step_impl(context):
    context.skipLagged_home_page.click_search_flights()


@then("a user should be navigated to flight search results page")
def step_impl(context):
    search_results_page = SkipLaggedFlightResultsPage(context.page)
    search_results_page.wait_for_page_to_be_loaded()
