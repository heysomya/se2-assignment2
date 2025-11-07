import pytest
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.base_page import BasePage
import time

VALID_USERNAME = "somya"
VALID_PASSWORD = "somya"

class TestDemoBlazeFeatures:

    def test_valid_login(self, driver):
        home_page = HomePage(driver)
        login_page = LoginPage(driver)
        home_page.navigate_to_home()
        home_page.click_login_link()
        login_page.login(VALID_USERNAME, VALID_PASSWORD)
        welcome_message = home_page.get_welcome_message()
        assert f"Welcome {VALID_USERNAME}" == welcome_message, f"Login failed. Expected 'Welcome {VALID_USERNAME}' but found '{welcome_message}'"

    def test_invalid_password_login(self, driver):
        home_page = HomePage(driver)
        login_page = LoginPage(driver)
        home_page.navigate_to_home()
        home_page.click_login_link()
        login_page.login(VALID_USERNAME, "randompass")
        alert_text = login_page.get_alert_text()
        assert alert_text == "Wrong password.", f"Expected 'Wrong password.' alert, but got '{alert_text}'"

    def test_invalid_username_login(self, driver):
        home_page = HomePage(driver)
        login_page = LoginPage(driver)
        home_page.navigate_to_home()
        home_page.click_login_link()
        login_page.login("randomuser99", "randompass")
        alert_text = login_page.get_alert_text()
        assert alert_text == "User does not exist.", f"Expected 'User does not exist.' alert, but got '{alert_text}'"

    def test_add_product_to_cart(self, driver):
        home_page = HomePage(driver)
        base_page = BasePage(driver)
        PRODUCT_NAME = "Nexus 6"
        home_page.navigate_to_home()
        home_page.click_product(PRODUCT_NAME)
        base_page.click_element((By.LINK_TEXT, "Add to cart"))
        time.sleep(1)
        alert = base_page.wait.until(EC.alert_is_present())
        alert_text = alert.text
        alert.accept()
        assert alert_text == "Product added", "Expected 'Product added' alert after clicking Add to cart."
        home_page.click_cart_link()
        cart_item_locator = (By.XPATH, f"//td[text()='{PRODUCT_NAME}']")
        try:
            base_page.wait.until(EC.visibility_of_element_located(cart_item_locator))
            is_in_cart = True
        except TimeoutException:
            base_page.capture_screenshot("cart_verification_failure")
            is_in_cart = False
        assert is_in_cart, f"Product '{PRODUCT_NAME}' was not found in the shopping cart."

    def test_product_details_display(self, driver):
        home_page = HomePage(driver)
        base_page = BasePage(driver)
        PRODUCT_NAME = "Sony xperia z5"
        home_page.navigate_to_home()
        home_page.click_product(PRODUCT_NAME)
        product_name = base_page.get_text((By.CSS_SELECTOR, ".name"))
        product_price = base_page.get_text((By.CSS_SELECTOR, ".price-container"))
        product_description = base_page.get_text((By.ID, "more-information"))
        assert "Sony xperia z5" in product_name, f"Expected 'Sony xperia z5', got '{product_name}'"
        assert "$320" in product_price, f"Expected price '$320', got '{product_price}'"
        assert len(product_description) > 0, "Product description was not visible."

    def test_checkout_process(self, driver):
        home_page = HomePage(driver)
        base_page = BasePage(driver)
        home_page.navigate_to_home()
        home_page.click_product("Nexus 6")
        base_page.click_element((By.LINK_TEXT, "Add to cart"))
        time.sleep(1)
        alert = base_page.wait.until(EC.alert_is_present())
        alert.accept()
        home_page.click_cart_link()
        base_page.click_element((By.XPATH, "//button[text()='Place Order']"))
        base_page.enter_text((By.ID, "name"), "Somya Dass")
        base_page.enter_text((By.ID, "country"), "USA")
        base_page.enter_text((By.ID, "city"), "Arlington")
        base_page.enter_text((By.ID, "card"), "1234567890123456")
        base_page.enter_text((By.ID, "month"), "11")
        base_page.enter_text((By.ID, "year"), "2025")
        base_page.click_element((By.XPATH, "//button[text()='Purchase']"))
        confirmation_text = base_page.get_text((By.CSS_SELECTOR, ".sweet-alert h2"))
        assert "Thank you for your purchase!" in confirmation_text, f"Expected confirmation message not displayed. Got '{confirmation_text}'"


    def test_homepage_navigation_links(self, driver):
        home_page = HomePage(driver)
        base_page = BasePage(driver)
        home_page.navigate_to_home()

        base_page.wait.until(EC.visibility_of_element_located((By.ID, "navbarExample")))
        base_page.wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "#navbarExample a.nav-link")))

        links = ["Home", "Contact", "About us", "Cart", "Log in", "Sign up"]
        for link_text in links:
            element = base_page.wait.until(EC.visibility_of_element_located((By.PARTIAL_LINK_TEXT, link_text)))
            text_clean = element.text.strip().replace("\n", " ")
            assert link_text in text_clean, f"Expected '{link_text}' in '{text_clean}'"
            assert element.is_displayed(), f"Link '{link_text}' is not visible."