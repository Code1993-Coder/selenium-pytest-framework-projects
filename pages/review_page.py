from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class ReviewPage(BasePage):
    review_title_locator=(By.ID,"AddProductReview_Title")
    review_text_locator=(By.ID,"AddProductReview_ReviewText")
    submit_reviw_locator=(By.XPATH,"//input[@name='add-review']")

    def select_rating(self, rating):
        return (By.XPATH, f"//input[@name='AddProductReview.Rating' and @value='{rating}']")
