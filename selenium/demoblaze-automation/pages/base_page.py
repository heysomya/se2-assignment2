from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time
import os

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 15)

    def find_element(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))

    def click_element(self, locator):
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    def enter_text(self, locator, text):
        element = self.wait.until(EC.visibility_of_element_located(locator))
        element.clear()
        element.send_keys(text)
        
    def get_text(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator)).text

    def capture_screenshot(self, filename="failure"):
        try:
            timestamp = time.strftime("%Y%m%d-%H%M%S")
            folder = "screenshots"
            os.makedirs(folder, exist_ok=True)
            path = os.path.join(folder, f"{filename}_{timestamp}.png")
            self.driver.get_screenshot_as_file(path)
            print(f"Screenshot saved to: {os.path.abspath(path)}")
        except Exception as e:
            print(f"Failed to capture screenshot: {e}")
