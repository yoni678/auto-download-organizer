# Import the Selenium WebDriver module, which allows Python to control web browsers.
from selenium import webdriver

# Import the Selenium WebDriver module again (this line is redundant and can be removed).
from selenium import webdriver

# Create a new Chrome browser instance using the default ChromeDriver on your system.
driver = webdriver.Chrome()

# Navigate the browser to the specified URL ("https://example.com").
driver.get("https://example.com")

# Print the title of the current webpage to the console.
print(driver.title)

# Close the browser window and end the WebDriver session.
driver.quit()



