from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time
from .base_page import BasePage

class LoginPage(BasePage):
    LOGIN_MODAL = (By.ID, "logInModal")
    USERNAME_INPUT = (By.ID, "loginusername")
    PASSWORD_INPUT = (By.ID, "loginpassword")
    LOGIN_BUTTON = (By.XPATH, "//button[text()='Log in']")

    def login(self, username, password):
        self.wait.until(EC.visibility_of_element_located(self.LOGIN_MODAL))
        self.enter_text(self.USERNAME_INPUT, username)
        self.enter_text(self.PASSWORD_INPUT, password)
        self.click_element(self.LOGIN_BUTTON)

    def get_alert_text(self):
        try:
            time.sleep(1)
            alert = self.wait.until(EC.alert_is_present())
            alert_text = alert.text.strip()
            alert.accept()
            return alert_text
        except TimeoutException:
            return None
