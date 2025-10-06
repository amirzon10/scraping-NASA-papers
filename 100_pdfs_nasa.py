
import os
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.options import Options
import time
import glob

# inputs
df = pd.read_csv("/Users/amirz/Desktop/Temporary shit/FER research local/unrelated/SB_publication_PMC.csv")
nasa_info = df.to_dict(orient='records')



# Set up Edge options to auto-download PDFs
options = Options()
options.add_experimental_option("prefs", {
    "download.default_directory": "/Users/amirz/Desktop/pmc_pdfs",  # Change to your desired folder
    "download.prompt_for_download": False,
    "download.directory_upgrade": True,
    "plugins.always_open_pdf_externally": True
})

# Launch Edge (assumes msedgedriver is in PATH)
driver = webdriver.Edge(options=options)

for entry in nasa_info:
    page = entry['Link']
    name = entry['Title']

    print(f"Processing page: {page}")
    driver.get(page)
    time.sleep(2)

    try:
        pdf_button = driver.find_element(By.CSS_SELECTOR, "a[data-ga-label='pdf_download_desktop']")
        pdf_button.click()
        print("Download initiated.")
    except Exception as e:
        print(f"PDF button not found on {page}: {e}")

    time.sleep(5)

    latest_pdf = max(glob.glob("/Users/amirz/Desktop/pmc_pdfs/*.pdf"), key=os.path.getctime)
    safe_name = "".join(c if c.isalnum() or c in "._-" else "_" for c in name)
    new_name = f"/Users/amirz/Desktop/pmc_pdfs/{safe_name}.pdf"
    if not os.path.exists(new_name):
        os.rename(latest_pdf, new_name)
    else:
        print(f"File {new_name} already exists. Skipping rename.")



    time.sleep(3)

# Quit browser after all downloads
driver.quit()
print("All downloads completed. Check your folder at /Users/amirz/Desktop/pmc_pdfs.")

  # Rename the most recently downloaded PDF
    
    