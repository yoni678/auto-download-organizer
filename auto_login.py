from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    # 1. Go to login page
    page.goto("https://practicetestautomation.com/practice-test-login/")

    # 2. Fill username and password
    page.fill("#username", "student")
    page.fill("#password", "Password123")

    # 3. Click login button
    page.click("#submit")

    # 4. Print success message
    message = page.text_content("h1")
    print("Login result:", message)

    page.pause()
    browser.close()



    

    







