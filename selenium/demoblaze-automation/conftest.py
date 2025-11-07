import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
import os
import time

BROWSERS = ["chrome", "firefox"]
MODES = ["headed", "headless"]

@pytest.fixture(params=[(b, m) for b in BROWSERS for m in MODES], scope="function")
def driver(request):
    browser, mode = request.param

    if browser == "chrome":
        options = ChromeOptions()
        if mode == "headless":
            options.add_argument("--headless")
        service = ChromeService(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=options)

    elif browser == "firefox":
        options = FirefoxOptions()
        if mode == "headless":
            options.add_argument("--headless")
        service = FirefoxService(GeckoDriverManager().install())
        driver = webdriver.Firefox(service=service, options=options)

    else:
        pytest.skip(f"Unsupported browser: {browser}")

    driver.maximize_window()
    driver.implicitly_wait(10)

    yield driver

    if request.node.rep_call.failed:
        screenshots_dir = "screenshots"
        os.makedirs(screenshots_dir, exist_ok=True)
        timestamp = time.strftime("%Y%m%d-%H%M%S")
        test_name = f"{request.node.name}_{browser}_{mode}"
        path = os.path.join(screenshots_dir, f"{test_name}_{timestamp}.png")
        try:
            driver.save_screenshot(path)
            print(f"\n💥 Screenshot of failed test saved to: {path}")
        except Exception as e:
            print(f"Failed to save screenshot: {e}")

    driver.quit()
    print(f"\n{browser.capitalize()} ({mode}) WebDriver closed successfully.")

@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
