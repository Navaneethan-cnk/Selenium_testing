from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys

# Specify the path to your ChromeDriver
service = Service('./chromedriver/chromedriver.exe')

# Initialize the WebDriver with the Service object
driver = webdriver.Chrome(service=service)

try:
    # Open Google
    driver.get("https://www.google.com")

    # Wait for the page to load
    driver.implicitly_wait(10)  # Optional: Wait for elements to load

    # Locate the search bar using its name attribute
    search_box = driver.find_element("name", "q")

    # Enter search query and hit Enter
    search_box.send_keys("Selenium Python tutorial")
    search_box.send_keys(Keys.RETURN)

    # Locate and print the titles of the first few search results
    results = driver.find_elements("css selector", "h3")
    for idx, result in enumerate(results[:5], start=1):  # Fetch first 5 results
        print(f"{idx}. {result.text}")

finally:
    # Close the browser
    driver.quit()
