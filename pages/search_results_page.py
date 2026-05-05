from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from pages.product_details_page import ProductDetailsPage


class SearchResultsPage(BasePage):
    product_title = (By.CSS_SELECTOR, ".product-title")
    result_error=(By.CSS_SELECTOR,".result")


    def get_product_locator(self, product_name):
        return (By.XPATH, f"//a[contains(normalize-space(),'{product_name}')]")

    def is_product_displayed(self, product_name):
        return self.is_visible(self.get_product_locator(product_name))

    def click_product(self, product_name):
        locator = self.get_product_locator(product_name)
        self.click(locator)
        return ProductDetailsPage(self.driver)

    def is_product_title_visible(self):
        return self.is_visible(self.product_title)

    def get_search_results_count(self):
        locator=self.product_title
        elements=self.driver.find_elements(*locator)
        count=len(elements)
        return count

    def get_all_product_titles(self):
        elements=self.driver.find_elements(*self.product_title)
        return [el.text for el in elements]


