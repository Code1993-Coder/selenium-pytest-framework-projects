from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage



class  HomePage(BasePage):

    #locators
    logo = (By.XPATH, "//img[@alt='Tricentis Demo Web Shop']")
    register=(By.LINK_TEXT,"Register")
    login = (By.LINK_TEXT, "Log in")
    cart=(By.XPATH, "//span[text()='Shopping cart']")
    wishlist=(By.XPATH, "//span[text()='Wishlist']")
    search_box=(By.ID,"small-searchterms")
    search_button=(By.CSS_SELECTOR,"input[type='submit']")

    home_page=(By.XPATH,"//a[@title='Home']")
    top_menu=(By.XPATH,"//ul[@class='top-menu']//a[normalize-space()='{menu_name}']")
    top_menu_sub = (By.XPATH, "//ul[@class='top-menu']//a[normalize-space()='{submenu_name}']")
    logout=(By.LINK_TEXT, "Log out")




    #Navigation headers
    def click_logo(self):
        self.click(self.logo)

    def navigate_home(self):
        self.click(self.home_page)


    def click_register(self):
        self.click(self.register)

    def click_login(self):
        self.click(self.login)

    def click_cart(self):
        self.click(self.cart)

    def click_logout(self):
        self.click(self.logout)

    def click_wishlist(self):
        self.click(self.wishlist)

    #Search related
    def search_product(self,product_name):
        self.enter_text(self.search_box,product_name)
        self.click(self.search_button)

   #Menu options
    def get_top_menu_locator(self,menu_name):
        by,value=self.top_menu
        return (by,value.format(menu_name=menu_name))

    def get_sub_menu_locator(self, submenu_name):
        by, value = self.top_menu_sub
        return (by, value.format(submenu_name=submenu_name))

    #Menu selection
    def select_top_menu(self, menu_name,sub_menu=None):
        main_menu_locator = self.get_top_menu_locator(menu_name)
        main_element = self.wait.until(EC.visibility_of_element_located(main_menu_locator))


        if sub_menu==None:
            self.click(main_menu_locator)
        else:
            actions = ActionChains(self.driver)
            actions.move_to_element(main_element).perform()
            sub_menu_locator = self.get_sub_menu_locator(sub_menu)
            self.wait.until(EC.visibility_of_element_located(sub_menu_locator))
            self.click(sub_menu_locator)


    def is_login_successful(self):
        return self.is_visible(self.logout)















