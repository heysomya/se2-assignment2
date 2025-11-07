# DemoBlaze Automation Project

This project contains automated end-to-end tests for the DemoBlaze e-commerce application using Selenium WebDriver and the Page Object Model (POM) design pattern.

## Prerequisites

* **Python:** Version 3.8 or higher.
* **Browser:** Google Chrome and Mozilla Firefox

## Setup Instructions

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/heysomya/se2-assignment2.git
    cd se2-assignment2/selenium/demoblaze-automation
    ```

2.  **Create a virtual environment (Recommended):**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv/Scripts/activate
    ```

3.  **Install dependencies:**
    ```bash
    pip install selenium pytest pytest-html webdriver-manager
    ```

4. **Run the tests:**
    ```bash
    pytest tests/test_scenarios.py --html=reports/demo_blaze_report.html --self-contained-html
    ```

## Project Structure

The project follows the Page Object Model structure:

```
selenium/
├── demoblaze-automation/
│   ├── pages/
│   │   ├── base_page.py              # Contains common WebDriver methods
│   │   ├── home_page.py              # Locators and methods for the homepage
│   │   └── login_page.py             # Locators and methods for the login modal
│   │   └── login_page.py             # Locators and methods for the login modal
│   │
│   └── tests/
│      ├── conftest.py               # Pytest fixtures (WebDriver setup for Chrome & Firefox)
│      └── test_scenarios.py         # Test functions for all identified test cases
│
├── docs/
│   ├── README.md                     # Environment setup instructions
│   └── testcases.pdf                 # List of test cases
│   
│
├── reports/
│   ├── screenshots/                  # Captured screenshots from failed tests
│   │   └── (auto-saved .png files)
│   ├── demo_blaze_report.html        # Generated pytest HTML report
│   └── testcases_results.pdf         # Results of testcases
│
└── .gitignore                        # To exclude virtual envs, cache, reports, etc.
```