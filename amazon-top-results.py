import json
import time
import sys

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Loads config json file
def loadConfig(filename):
    with open(filename, 'r') as configFile:
        return json.load(configFile)

# Get search input element
def getSearchInput(driver):
    searchDiv = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, 'nav-search-field'))
    )
    return searchDiv.find_element_by_tag_name('input')

# Perform a search
def searchTerm(inputElem, term):
    inputElem.send_keys(term)
    inputElem.send_keys(Keys.RETURN)

# Returns list of result candidates
def getResults(driver):
    return driver.find_elements_by_class_name('s-result-item')

# Tests the element to see if it's a result that should be checked
def validResult(result):
    valid = True
    
    # Test if it has 'div span.a-text-normal'
    try:
        result.find_element_by_css_selector('div span.a-text-normal')
        result.find_element_by_css_selector('div span.a-offscreen')
    except:
        valid = False

    # Test if contains class contains 'AdHolder'
    if 'AdHolder' in result.get_attribute('class'):
        valid = False
    
    return valid

# Gets the title of a result item
def getTitle(element):
    return element.find_element_by_css_selector('div span.a-text-normal').text

# Gets the price of a result item
def getPrice(element):
    return element.find_element_by_css_selector('div span.a-offscreen').get_attribute('innerHTML')

# Main function
if __name__ == "__main__":
    if len(sys.argv) <= 1:
        print('USAGE: executable "<search phrase>"')
        sys.exit()

    searchPhrase = sys.argv[1]

    # Read config file
    config = loadConfig('config.json')
    address = config['address']
    driverPath = config['driver']

    # Build options
    chrome_options = Options()
    chrome_options.add_argument('--headless')

    try:
        # Initialize webdriver
        driver = webdriver.Chrome(executable_path = driverPath, chrome_options=chrome_options);
        driver.get(address)

        searchInput = getSearchInput(driver)
        searchTerm(searchInput, searchPhrase)

        # Ensure page is loaded
        #time.sleep(10)

        # Find individual search results
        results = getResults(driver)

        count = 10
        position = 0
        while count > 0:
            if validResult(results[position]):
                print(getPrice(results[position]), getTitle(results[position]))
                count -= 1
            position += 1
    except Exception as exc:
        print("Program encountered and error: " + str(exc))
    finally:
        # Close webdriver
        driver.close()
