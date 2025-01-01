%%writefile qa_selenium_test.py
""" Test to validate table search functionality."""
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

# Test Setup: Declaring the URL and expected values
_URL = "https://www.lambdatest.com/selenium-playground/table-sort-search-demo"
_SEARCH_TERM_NEW_YORK = "New York"
_EXPECTED_TOTAL_ENTRIES = 5
_TOTAL_ENTRIES_TEXT = "Showing 1 to 5 of 5 entries (filtered from 24 total entries)"
_WAIT_TIME_SECONDS = 10

@pytest.fixture
def setup_browser():
    """Setup the WebDriver and open the browser."""
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--headless")  # Run without GUI
    chrome_options.add_argument("--no-sandbox")  # Required for some environments
    chrome_options.add_argument("--disable-dev-shm-usage")  # Overcome resource limits

    driver = webdriver.Chrome(options=chrome_options)
    driver.implicitly_wait(_WAIT_TIME_SECONDS)
    yield driver
    driver.quit()

def test_to_validate_table_search(setup_browser):
    """ test to validate search functionality of a sorted table."""
    driver = setup_browser
    # Navigate to URL
    driver.get(_URL)
    # Wait for load page
    driver.implicitly_wait(_WAIT_TIME_SECONDS)

    # Pre_condition: Check table is present in the web page when page is loaded.
    table = driver.find_element(By.XPATH, '//*[@id="example"]/tbody/tr')
    assert table.is_displayed(),"pre_condition_failed:table is not displayed when page is loaded"
    # Pre_condition: Validate search box is available and interactable.
    search_box = driver.find_element(By.XPATH, '//*[@id="example_filter"]/label/input')
    assert search_box.is_displayed(),"pre_condition_failed:Search box is not visible on the page"
    assert search_box.is_enabled(), "pre_condition_failed:Search box is not enabled for interaction"

    # Interact with search box.
    search_box.clear()
    search_box.send_keys(_SEARCH_TERM_NEW_YORK)
    search_box.send_keys(Keys.RETURN)

    # Validate , only "new york" entries are fetched.
    rows = driver.find_elements(By.XPATH, '//*[@id="example"]/tbody/tr')
    for row in rows:
        assert _SEARCH_TERM_NEW_YORK in row.text, "Search term New York is not available in the row entries"
    
    # Verify total entries text updated based on search term
    expected_total_entries_text = f"Showing 1 to {_EXPECTED_TOTAL_ENTRIES} of {_EXPECTED_TOTAL_ENTRIES} entries (filtered from 24 total entries)"
    actual_total_entries_text = driver.find_element(By.ID, "example_info").text
    assert expected_total_entries_text == actual_total_entries_text, "The total entries text does not match the expected value."
