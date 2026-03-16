# Import the synchronous Playwright API, which allows controlling browsers like Chrome, Firefox, and WebKit.
from playwright.sync_api import sync_playwright
# Start a Playwright context using a 'with' block so everything is cleaned up automatically afterward.
with sync_playwright() as p:
    # Launch a Chromium browser instance. headless=False means the browser window will be visible.
    browser = p.chromium.launch(headless=False)

    # Open a new blank browser tab (page).
    page = browser.new_page()

    # Navigate the page to the official Python website.
    page.goto("https://www.python.org")

    # Retrieve the title of the current webpage.
    title = page.title()

    # Print the page title to the console.
    print("Page title:", title)

    # Select the first blog article link inside the .blog-widget section and extract its text.
    first_article = page.locator(".blog-widget li a").first.text_content()

    # Print the text of the first blog article.
    print("First blog article:", first_article)

    # Close the browser window and end the session.
    browser.close()

    # playwright codegen https://www.python.org
    
    # Playwright will record your browser actions and generate Python code automatically
    # A browser will open and every click you make becomes Python code. This is how many automation developers learn extremely fast.




