# Selenium Table Search Test

## Overview

This Python script (`qa_selenium_test.py`) automates the process of navigating to the [Selenium Playground Table Sort Search Demo](https://www.lambdatest.com/selenium-playground/table-sort-search-demo), interacts with the search box to search for "New York," and validates that the search results display 5 entries out of a total of 24 entries.

The script uses **Selenium WebDriver** to interact with the web page and **pytest** for test execution. It is designed to run in a **headless** browser mode for environments like Google Colab.

## Features

- Navigates to the URL: https://www.lambdatest.com/selenium-playground/table-sort-search-demo
- Locates the search box and performs a search for the term "New York."
- Validates the search results by ensuring only the relevant entries are displayed.
- Confirms that the total number of entries shown after the search matches the expected count.

## Prerequisites

- **Google colab**: Browser based tool to run and execute python code.
- **Selenium**: Web automation tool.
- **pytest**: Testing framework for Python.
- **Google Chrome**: The default browser used for running the Selenium tests.
- **Chromedriver**: A separate executable used to interact with the Chrome browser.


## Setup Instructions

1. Install Dependencies
   1. To install selenium use cmd - pip install selenium
   2. To install pytest framework use cmd - pip install pytest
2. Configure Google Colab to run Selenium with Chrome in headless mode

  **Set up options for headless Chrome**
  chrome_options = Options()
  chrome_options.add_argument('--headless')  
  chrome_options.add_argument('--no-sandbox')
  chrome_options.add_argument('--disable-dev-shm-usage')
  chrome_options.add_argument('--remote-debugging-port=9222')

### Run script in Google colab

 1. Clone or upload the qa_selenium_test.py script to google colab note book.
 2. Use command !pytest  qa_selenium_test.py to execute the test.
    

The script will navigate to the Selenium Playground Table, search for "New York," and verify that the search results match the expected entries:

The search term "New York" will appear in the results.
The text showing the total entries will match "Showing 1 to 5 of 5 entries (filtered from 24 total entries)."
If all the assertions pass, the test will succeed.

### Code Explanation
setup_browser(): initializes the Selenium WebDriver and sets up the browser environment in headless mode.
test_to_validate_table_search(): test function that performs the following actions:
 1. Opens the target URL.
 2. Checks if the table and search box are visible and enabled.
 3. Searches for the term "New York" in the search box.
 4. Verifies that the search results show only "New York" entries.
 5. Checks if the total entries text is correctly updated based on the search.

### Troubleshooting
Headless Mode: If issues related to the headless mode  are observed, ensure the necessary flags (--headless, --no-sandbox, --disable-dev-shm-usage) are set in the Chrome options.
