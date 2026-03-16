from playwright.sync_api import sync_playwright
import requests
import os

downloads = r"C:\Users\yelba\Downloads"
pdf_folder = os.path.join(downloads, "pdf")
os.makedirs(pdf_folder, exist_ok=True)

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://file-examples.com/index.php/sample-documents-download/sample-pdf-download/")

    # Get the href of the first PDF link
    link = page.locator("a[href$='.pdf']").first.get_attribute("href")
    print("Found PDF link:", link)

    browser.close()

# Download the PDF with requests
local_file = os.path.join(pdf_folder, link.split("/")[-1])
r = requests.get(link, stream=True)
with open(local_file, "wb") as f:
    for chunk in r.iter_content(chunk_size=8192):
        f.write(chunk)

print("PDF downloaded and saved to folder!")
