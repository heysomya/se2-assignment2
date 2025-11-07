from selenium.webdriver.common.by import By
from .base_page import BasePage

class HomePage(BasePage):
    NAV_LOGIN_LINK = (By.ID, "login2")
    NAV_CART_LINK = (By.ID, "cartur")
    NAV_WELCOME_USER_LINK = (By.ID, "nameofuser")
    
    def product_link(self, product_name):
        return (By.LINK_TEXT, product_name)
    
    def navigate_to_home(self):
        self.driver.get("https://www.demoblaze.com")
        
    def click_login_link(self):
        self.click_element(self.NAV_LOGIN_LINK)
        
    def click_cart_link(self):
        self.click_element(self.NAV_CART_LINK)
        
    def click_product(self, product_name):
        self.click_element(self.product_link(product_name))
        
    def get_welcome_message(self):
        return self.get_text(self.NAV_WELCOME_USER_LINK)