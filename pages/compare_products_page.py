from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class CompareProductsPage(BasePage):
    clear_list_locator=(By.CSS_SELECTOR,".clear-list")