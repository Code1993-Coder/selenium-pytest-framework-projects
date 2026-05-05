
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from pages.base_page import BasePage
from pages.home_page import HomePage
#from pages.product_details_page import ProductDetailsPage

class ShoppingCartPage(BasePage):
    update_shopping_cart_locator=(By.NAME,"updatecart")
    continues_shopping_locator=(By.NAME,"continueshopping")
    cart_qty_locator=(By.CSS_SELECTOR,".cart - qty")
    table_qty=(By.CSS_SELECTOR,"qty-input valid")
    cart = (By.XPATH,"//span[text()='Shopping cart']")
    remove_locator=(By.NAME,"removefromcart")
    terms_of_service_locator=(By.ID,"termsofservice")
    checkout_locator = (By.ID,"checkout")
    product_price=(By.CLASS_NAME,"product-price")
    discount_price_locator=(By.NAME,"discountcouponcode")
    gift_card_code_locator=(By.NAME,"giftcardcouponcode")
    coupon_code_error_locator=(By.CLASS_NAME,"message")
    shipping_country_dropdown =(By.ID,"CountryId")
    estimate_shipping=(By.NAME,"estimateshipping")

    # Navigation
    def open_cart(self):
        self.click(self.cart)

    # Table operations
    def get_table_cell(self,product_name, column_name):
        cell_locator = (By.XPATH,f"//table//tr[.//a[normalize-space()='{product_name}']]/td[count(ancestor::table//th[normalize-space()='{column_name}']/preceding-sibling::th)+1]")
        return self.get_text(*cell_locator)

    def get_product_row(self,product_name):
        return (By.XPATH, f"//tr[.//a[normalize-space()='{product_name}']]")

    def is_product_present(self, product_name):
        return self.is_visible(self.get_product_row(product_name))


    def get_product_quantity(self, product_name):
        qty_locator = (By.XPATH, f"//tr[.//a[normalize-space()='{product_name}']]//input[@class='qty-input']")
        qty = self.get_attribute(qty_locator,"value")
        return int(qty) if qty else 0

    def get_product_amount(self, product_name, column_name):
        text = self.get_table_cell(product_name, column_name)
        return float(text.replace("$", "").strip())

    # Actions
    def update_product_quantity(self,product_name,qty):
        qty_locator=(By.XPATH,f"//tr[.//a[normalize-space()='{product_name}']]//input[@class='qty-input']")
        self.enter_text(*qty_locator ,qty)
        self.click(self.update_shopping_cart_locator)

    def remove_product(self,product_name):
        remove_cell_locator = (By.XPATH,f"//tr[.//a[normalize-space()='{product_name}']]//input[@type='checkbox']")
        self.click(*remove_cell_locator)
        self.click(self.update_shopping_cart_locator)

    #Shipping
    def select_shipping_country(self,country_name):
        dropdown=Select(self.driver.find_element(*self.shipping_country_dropdown))
        dropdown.select_by_value(country_name)
        self.click(self.estimate_shipping)


    #Cart details
    def get_price_by_label(self,label):
        label_locator=(By.XPATH,f"//td[contains(.,'{label}')]/following-sibling::td//span[contains(@class,'product-price')]")
        return self.get_text(*label_locator)

    # Coupons

    def enter_coupon_code(self, code):
        self.enter_text(self.discount_price_locator, code)

    def enter_gift_card_code(self, code):
        self.enter_text(self.gift_card_code_locator, code)

    def get_coupon_code_text(self):
        return self.get_text(self.coupon_code_error_locator)

    # Checkout
    def accept_terms_and_checkout(self):
       self.select_checkbox(self.terms_of_service_locator)
       self.click(self.checkout_locator)













