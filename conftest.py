import os

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.chrome.service import Service

from pages.home_page import HomePage
from pages.product_details_page import ProductDetailsPage
from pages.register_page import RegisterPage
from pages.search_results_page import SearchResultsPage
from pages.shopping_cart_page import ShoppingCartPage
from pages.sign_in_page import SigninPage

from utilities.helpers import load_test_data, generate_email

data = load_test_data("../test_data/registration_data.json")
# get browser configuration from inbuilt terminal of pycharm

#pytest hook - to register a new command-line argument
def pytest_addoption(parser):
    parser.addoption(
        "--browser", action="store", default="chrome", help="Specify the browser: chrome or edge"
    )

#setup and teardown fixture
@pytest.fixture(scope="function")
def browser_instance(request):#request param is used to get configuration options from terminal
    browser_name=request.config.getoption("browser")
    if browser_name == "chrome":
        options = ChromeOptions()
        options.add_argument("--start-maximized")
        options.add_argument('--ignore-certificate-errors')
        options.add_argument('--ignore-ssl-errors=yes')
        driver = webdriver.Chrome(options=options)
    elif browser_name=='edge':
        options = EdgeOptions()
        options.add_argument("--start-maximized")
        driver = webdriver.Edge(options=options)
    else:
        raise ValueError(f"Browser {browser_name} not supported")
    driver.get("https://demowebshop.tricentis.com/")
    yield driver#control is sent to business process flow in test function .
    driver.quit()#post condition step where the control comes back from test function after business process is completed and close the browser

@pytest.fixture
def register_page(home_page):
    home_page.click_register()
    return RegisterPage(home_page.driver)

@pytest.fixture
def home_page(browser_instance):
    return HomePage(browser_instance)

@pytest.fixture
def login_page(browser_instance):
    return SigninPage(browser_instance)

@pytest.fixture
def search_page(browser_instance):
    return SearchResultsPage(browser_instance)

@pytest.fixture
def product_page(browser_instance):
    return ProductDetailsPage(browser_instance)

@pytest.fixture
def shopping_page(browser_instance):
    return ShoppingCartPage(browser_instance)

@pytest.fixture(params=data['positive_registration'])
def existing_customer(request,register_page):
    user=request.param
    email=generate_email()

    register_page.register_user(user["gender"],user["first_name"], user["last_name"],email, user["password"])
    register_page.click_continue()
    return {"email": email,"password": user["password"]}


#html image screenshots attached in report for failed test case only
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    """
        Extends the PyTest Plugin to take and embed screenshot in html report, whenever test fails.
        :param item:
        """
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            reports_dir = os.path.join(os.path.dirname(__file__), 'reports')
            if not os.path.exists(reports_dir):
                os.makedirs(reports_dir)
            file_name = os.path.join(reports_dir, report.nodeid.replace("::", "_").replace("/", "_") + ".png")
            print("file name is " + file_name)

            driver = item.funcargs.get("browser_instance")
            if driver:
                _capture_screenshot(driver, file_name)
                html = (
                    f'<div><img src="{file_name}" alt="screenshot" style="width:304px;height:228px;" '
                    'onclick="window.open(this.src)" align="right"/></div>'
                )
                extra.append(pytest_html.extras.html(html))
        report.extra = extra


def _capture_screenshot(driver, file_name):
    driver.get_screenshot_as_file(file_name)




