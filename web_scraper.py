from playwright.sync_api import sync_playwright
import pandas as pd

# We will store all scraped items in this list.
data = []

# Start Playwright in synchronous mode.
with sync_playwright() as p:

    # Launch Chromium browser. headless=False means you SEE the browser.
    browser = p.chromium.launch(headless=False)

    # Create a new browser tab (page).
    page = browser.new_page()

    # Navigate to the target website.
    page.goto("https://webscraper.io/test-sites/e-commerce/allinone/phones/touch")

    # Wait until product cards are visible (ensures JS content is loaded).
    page.wait_for_selector(".thumbnail")

    # Select all product containers on the page.
    items = page.query_selector_all(".thumbnail")

    # Loop through each product card.
    for item in items:

        # Extract product title text.
        title = item.query_selector(".title").inner_text()

        # Extract product price text.
        price = item.query_selector(".price").inner_text()

        # Extract product description text.
        description = item.query_selector(".description").inner_text()

        # Add the extracted data to our list as a dictionary.
        data.append({
            "title": title,
            "price": price,
            "description": description
        })

    # Close the browser when scraping is done.
    browser.close()

# Convert the list of dictionaries into a DataFrame.
df = pd.DataFrame(data)

# Save the DataFrame to an Excel file.
df.to_excel("products1.xlsx", index=False)

print("Scraping complete! Saved to products1.xlsx")


