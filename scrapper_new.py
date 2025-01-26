from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os
import requests

def setup_driver():
    """Set up the Selenium WebDriver with Chrome options."""
    chrome_options = webdriver.ChromeOptions()
    # Set the default download directory (change the path as needed)
    prefs = {"download.default_directory": os.path.abspath("path/to/download/folder")}
    chrome_options.add_experimental_option("prefs", prefs)
    # Initialize the WebDriver
    return webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

def click_element(driver, locator):
    """Click an element using its locator."""
    element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(locator))
    element.click()

def download_file(url, save_path):
    """Download a file from a URL and save it to the specified path."""
    response = requests.get(url)
    with open(save_path, 'wb') as file:
        file.write(response.content)
    print(f"File downloaded successfully and saved to {save_path}")

def handle_ad(driver):
    """Handle the ad if it appears."""
    try:
        # Locate the ad element (update the locator as needed)
        ad_locator = (By.CSS_SELECTOR, "div.ad-class-name")  # Replace with the actual ad locator
        close_button_locator = (By.CSS_SELECTOR, "button.close-ad-button")  # Replace with the actual close button locator

        # Check if the ad is present
        ad_element = WebDriverWait(driver, 5).until(EC.presence_of_element_located(ad_locator))
        print("Ad detected. Attempting to close it...")

        # Close the ad by clicking the close button
        close_button = WebDriverWait(driver, 5).until(EC.element_to_be_clickable(close_button_locator))
        close_button.click()
        print("Ad closed successfully.")

    except Exception as e:
        # If the ad is not present or cannot be closed, continue without interruption
        print(f"No ad detected or ad could not be closed: {e}")

def download_project_appraisal_document(project_id):
    """Download the 'Project Appraisal Document' for a given project ID."""
    driver = setup_driver()
    try:
        # Step 1: Open the project page
        driver.get(f"https://projects.worldbank.org/en/projects-operations/document-detail/{project_id}?type=projects")
        print(f"Opened project page for ID: {project_id}")

        # Step 2: Handle the ad if it appears
        handle_ad(driver)

        # Step 3: Wait for the table to load
        table_locator = (By.CSS_SELECTOR, "table.project-operation-tab-table")
        WebDriverWait(driver, 10).until(EC.presence_of_element_located(table_locator))

        # Step 4: Handle pagination
        while True:
            # Find all rows in the current page
            rows = driver.find_elements(By.CSS_SELECTOR, "table.project-operation-tab-table tbody tr")

            # Iterate through the rows to find the "Project Appraisal Document"
            for row in rows:
                document_type = row.find_element(By.CSS_SELECTOR, "td[data-th='DOCUMENT TYPE:']").text
                if document_type == "Project Appraisal Document":
                    # Click the document link
                    document_link = row.find_element(By.CSS_SELECTOR, "td a")
                    document_url = document_link.get_attribute("href")
                    print(f"Found Project Appraisal Document: {document_url}")
                    document_link.click()

                    # Step 5: Handle the ad if it appears
                    handle_ad(driver)

                    # Step 6: Wait for the new page to load and locate the download section
                    download_section_locator = (By.CSS_SELECTOR, "p.downloads-info")
                    WebDriverWait(driver, 10).until(EC.presence_of_element_located(download_section_locator))

                    # Step 7: Find the .TXT or .PDF download link
                    download_links = driver.find_elements(By.CSS_SELECTOR, "p.downloads-info a")
                    for link in download_links:
                        href = link.get_attribute("href")
                        if href and (href.endswith(".txt") or href.endswith(".pdf")):
                            print(f"Found download link: {href}")
                            # Determine the file extension
                            file_extension = os.path.splitext(href)[1].lower()
                            # Define the save path
                            save_path = os.path.abspath(f"{project_id}_Project_Appraisal_Document{file_extension}")
                            # Download the file using requests
                            download_file(href, save_path)
                            return  # Exit after downloading the document

            # Step 8: Check if there is a "Next" button and click it
            try:
                next_button = WebDriverWait(driver, 5).until(
                    EC.element_to_be_clickable((By.CSS_SELECTOR, "ul.pagination li:not(.disabled) a i.fa-angle-right"))
                )
                # Check if the parent <li> element is disabled
                parent_li = next_button.find_element(By.XPATH, "./ancestor::li")
                if "disabled" in parent_li.get_attribute("class"):
                    print("No more pages or 'Next' button is disabled.")
                    break  # Exit if there are no more pages
                else:
                    next_button.click()
                    print("Moving to the next page...")
                    time.sleep(3)  # Wait for the next page to load
            except:
                print("No more pages or 'Next' button not found.")
                break  # Exit if there are no more pages

    except Exception as e:
        print(f"An error occurred for project {project_id}: {e}")
    finally:
        driver.quit()

def process_project_ids(project_ids):
    """Process a list of project IDs one by one."""
    for project_id in project_ids:
        print(f"Processing project ID: {project_id}")
        download_project_appraisal_document(project_id)
        time.sleep(5)  # Add a delay between processing each project

if __name__ == "__main__":
    # List of project IDs to process
    project_ids = ["P130548","P050658"]  # Add or modify project IDs as needed

    # Process the project IDs
    process_project_ids(project_ids)