from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Set up the WebDriver
# service = Service(r"C:\Users\Navaneethan\Desktop\python\selenium\chromedriver\chromedriver.exe")
driver = webdriver.Chrome()

try:
    # Open Google
    driver.get("https://www.google.com")

    # Wait for the search box to be present
    search_box = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "q"))
    )

    # Enter search query and press Enter
    search_box.send_keys("Selenium Python tutorial")
    search_box.send_keys(Keys.RETURN)

    # Wait for the search results to load
    WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, "h3"))
    )

    # Locate and print the titles of the first few search results
    results = driver.find_elements(By.CSS_SELECTOR, "h3")
    for idx, result in enumerate(results[:5], start=1):
        print(f"{idx}. {result.text}")

finally:
    # Close the browser
    driver.quit()
