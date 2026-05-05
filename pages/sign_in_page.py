from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class SigninPage(BasePage):

    #class variables
    email=(By.ID,"Email")
    password=(By.ID,"Password")
    login_button=(By.CSS_SELECTOR,"input[value='Log in']")
    forgot_password_link=(By.LINK_TEXT,"Forgot password?")
    password_recovery_header=(By.XPATH, "//h1[normalize-space()='Password recovery']")
    password_recovery_helptext=(By.CSS_SELECTOR, "p.tooltip")
    recover_button=(By.NAME,"send-email")
    invalid_credentials_error=(By.CSS_SELECTOR,".validation-summary-errors")
    customer_not_found_error=(By.XPATH,"//div[@class='validation-summary-errors']//li[text()='No customer account found']")
    email_format_error=(By.XPATH,"//span[@for='Email']")
    #page methods

    #Returning customer page methods

    def login(self,email,password):
        self.enter_text(self.email,email)
        self.enter_text(self.password,password)
        self.click(self.login_button)

    def forgot_password(self,email):
        self.click(self.forgot_password_link)
        self.is_visible(self.password_recovery_header)
        self.is_visible(self.password_recovery_helptext)
        self.enter_text(self.email,email)
        self.click(self.recover_button)

    def get_invalid_credentials_error(self):
        return self.get_text(self.invalid_credentials_error)

    def get_customer_not_found_error(self):
        return  self.get_text(self.customer_not_found_error)

    def get_email_format_error(self):
        return  self.get_text(self.email_format_error)





