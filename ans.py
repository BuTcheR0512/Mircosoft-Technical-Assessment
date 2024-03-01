from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
import os

options = webdriver.ChromeOptions()

prefs = {
   # "download.default_directory": r"C:\Users\KIIT\Documents\micro",    # save pdf to a file named micro i.e specific folder
    "download.prompt_for_download": False,
    "plugins.always_open_pdf_externally": True
}

options.add_experimental_option('prefs', prefs)

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)

URL = "https://jbvnl.co.in/noticeCommercial.php"
driver.get(URL)
driver.maximize_window()
driver.implicitly_wait(5)

all_a_tags = driver.find_elements(By.XPATH, "//a[contains(@href, '.pdf')]")
count = 0

for a in all_a_tags:
    if a.get_attribute('href') and '.pdf' in a.get_attribute('href') and "download" in a.text.lower(): # Download the file with .pdf extension
        
        file_name = f"file_{count}.pdf" # Generate a unique file name
        
        
        a.click()   # Click on the download link
        
        time.sleep(5)   # Wait for the download to complete

         # Check if the file has been downloaded
        if os.path.exists(os.path.join(r"C:\Users\KIIT\Documents\micro", file_name)):
            print(f"Downloaded {file_name}")
        else:
            print(f"Failed to download {file_name}")
        
        count += 1
        if count >= 5: # download latest 5 pdf
            break
