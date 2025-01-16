from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementClickInterceptedException, TimeoutException
import time

def setup_driver():
    chrome_options = webdriver.ChromeOptions()
    prefs = {"download.default_directory": "/path/to/your/download/folder"}
    chrome_options.add_experimental_option("prefs", prefs)
    return webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

def close_popups(driver):
    """Close any unexpected popups that may appear."""
    try:
        popup_elements = WebDriverWait(driver, 3).until(
            EC.presence_of_all_elements_located((By.CLASS_NAME, "QSIWebResponsive-creative-container-fade"))
        )
        for popup in popup_elements:
            try:
                popup.click()
                print("Closed a popup.")
            except:
                pass  # Ignore if the popup cannot be clicked
    except TimeoutException:
        print("No popups detected.")

def click_with_retry(driver, element):
    """Try clicking an element, retry if intercepted by a popup."""
    try:
        element.click()
    except ElementClickInterceptedException:
        print("Element click intercepted, trying again after closing popups...")
        close_popups(driver)  # Close any popups blocking the click
        driver.execute_script("arguments[0].scrollIntoView(true);", element)  # Ensure visibility
        driver.execute_script("arguments[0].click();", element)  # Use JavaScript click as a fallback

def download_project_report():
    driver = setup_driver()
    try:
        # Open the World Bank Projects page
        driver.get("https://projects.worldbank.org/en/projects-operations/projects-home")
        driver.maximize_window()

        # Search for the project ID
        search_box = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "qterm")))
        project_id = "P050658"
        search_box.send_keys(project_id)
        search_box.send_keys(Keys.RETURN)

        # Click on the first project link
        project_link = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.CLASS_NAME, "project-list-link"))
        )[0]
        click_with_retry(driver, project_link)

        # Navigate to the "Documents" tab
        documents_tab = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "documents_top"))
        )
        click_with_retry(driver, documents_tab)

        # Click on the first document link
        first_document_link = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located(
                (By.XPATH, "//a[contains(@href, 'documents.worldbank.org/curated')]")
            )
        )[0]
        click_with_retry(driver, first_document_link)

        # Locate the "Official PDF" link
        official_pdf_link = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//a[contains(text(), 'Official PDF')]"))
        )
        click_with_retry(driver, official_pdf_link)

        print("PDF download initiated successfully!")
        time.sleep(10)  # Wait for the download to complete
    finally:
        driver.quit()

if __name__ == "__main__":
    download_project_report()
