from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import element_to_be_selected
from selenium.webdriver.support.select import Select

from pages.base_page import BasePage
from pages.compare_products_page import CompareProductsPage
from pages.email_friend_page import EmailAFriendPage
from pages.review_page import ReviewPage
from pages.shopping_cart_page import ShoppingCartPage


class ProductDetailsPage(BasePage):
    product_title = (By.CSS_SELECTOR, "h1[itemprop='name']")
    product_price=(By.XPATH,"//span[@itemprop='price']")
    overview_description = (By.CSS_SELECTOR, ".full-description p")
    product_image = (By.XPATH, "//img[@itemprop='image']")
    add_to_cart_locator=(By.XPATH,"//input[contains(@id,'add-to-cart-button')]")
    add_to_compare_list_locator=(By.XPATH,"//input[@value='Add to compare list']")
    email_a_friend_locator=(By.XPATH,"//input[@value='Email a friend']")
    quantity=(By.CSS_SELECTOR,".qty-input")
    add_to_wishlist_locator=(By.XPATH,"//input[@value='Add to wishlist']")
    success_message = (By.XPATH, "//p[@class='content']")
    close_notification_btn=(By.CSS_SELECTOR,".close")
    cart_link_in_notification=(By.XPATH,"//p[@class='content']//a[@href='/cart']")
    size_dropdown_locator=(By.ID,"//select[contains(@id,'product_attribute')]")
    add_review_locator=(By.XPATH,"//a[text()='Add your review']")


    #Product details

    def get_product_title(self):
        return self.get_text(self.product_title)

    def get_product_description(self):
        return self.get_text(self.overview_description)

    def get_product_price(self):
        price=self.get_text(self.product_price)
        return int(price)

    def get_product_quantity(self):
        qty=self.get_attribute(self.quantity,"value")
        return int(qty) if qty else 0

    def select_size(self,size):
        elements=self.driver.find_elements(*self.size_dropdown_locator)
        if elements:
            dropdown = Select(elements[0]) #take first web element
            options=[opt.text for opt in dropdown.options]
            if size in options:
                dropdown.select_by_value(size)
                return True
            else:
                return False

    def select_color(self, color_name):
        locator = (By.XPATH, f"//span[@class='color-container' and @title='{color_name}']")
        elements=self.driver.find_elements(*self.locator)
        for element in elements:
            if element.is_displayed():
                element.click()
                return True
        return False

    def set_quantity(self, qty):
        elements = self.driver.find_elements(*self.quantity)
        if elements:
            self.enter_text(self.quantity, qty)
            return True
        else:
            return False


    def is_product_visible(self):
        self.is_visible(self.product_title)
        self.is_visible(self.overview_description)
        self.is_visible(self.product_image)
        return True

    #Cart & Purchase Actions
    def add_to_cart(self):
        self.click(self.add_to_cart_locator)


    def click_shopping_cart_link(self):
        self.click(self.cart_link_in_notification)
        return ShoppingCartPage(self.driver)

    def go_to_cart(self):
        self.click(self.cart_link_in_notification)
        return ShoppingCartPage(self.driver)


    #Wishlist & Compare
    def add_to_compare_list(self):
        self.click(self.add_to_compare_list_locator)
        return CompareProductsPage(self.driver)

    def add_to_wishlist(self):
        self.click(self.add_to_wishlist_locator)

    #Sharing / Communication
    def email_friend(self):
        self.click(self.email_a_friend_locator)
        return EmailAFriendPage(self.driver)
        

    #Notification / Alerts

    def get_success_message_text(self):
        return self.get_text(self.success_message)

    
    def get_success_link(self, target):
        return (By.XPATH, f"//p[@class='content']//a[contains(@href,'{target}')]")

    def close_notification(self):
        self.click(self.close_notification_btn)

    def verify_success(self):
        return "The product has been added to your" in self.get_success_message_text()


    #Reviews
    def add_review(self):
        self.click(self.add_review_locator)
        return ReviewPage(self.driver)




