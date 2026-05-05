from selenium.webdriver.common.by import By

from pages.base_page import BasePage

import time

from pages.home_page import HomePage


class RegisterPage(BasePage):

    #locators class variables
    gender_male = (By.ID, "gender-male")
    gender_female = (By.ID, "gender-female")
    first_name=(By.ID,"FirstName")
    last_name=(By.ID,"LastName")
    email=(By.ID,"Email")
    password=(By.XPATH,"//input[@name='Password']")
    confirm_password=(By.CSS_SELECTOR,"input[name='ConfirmPassword']")
    register_button=(By.CSS_SELECTOR,"#register-button")
    registration_success=(By.XPATH,"//div[@class='result']")
    continue_button=(By.CSS_SELECTOR,"input[value='Continue']")
    validation_email_exists=(By.CSS_SELECTOR,".validation-summary-errors")




    #Field methods

    def select_gender(self, gender):
        gender = gender.lower()
        if gender == "male":
            self.click(self.gender_male)

        elif gender == "female":
            self.click(self.gender_female)
        else:
            raise ValueError("Invalid gender provided")

    def enter_first_name(self, first_name):
        self.enter_text(self.first_name, first_name)

    def enter_last_name(self, last_name):
        self.enter_text(self.last_name, last_name)

    def enter_email(self, email):
        self.enter_text(self.email, email)

    def enter_password(self, password):
        self.enter_text(self.password, password)

    def enter_confirm_password(self, password):
        self.enter_text(self.confirm_password, password)

    def click_register(self):
        self.click(self.register_button)
    #Actions methods
    def register_user(self,gender,first_name,last_name,email,password,confirm_password=None):
        self.select_gender(gender)
        self.enter_first_name(first_name)
        self.enter_last_name(last_name)
        self.enter_email(email)
        self.enter_password(password)
        if confirm_password is None:
            confirm_password = password
        self.enter_confirm_password(confirm_password)
        self.click(self.register_button)

    def click_continue(self):
        self.click(self.continue_button)
        return HomePage(self.driver)

    #Validation methods
    def get_validation_message(self, field_name):
        locator = (By.XPATH, f"//span[@data-valmsg-for='{field_name}']")
        return self.get_text(locator)

    def get_registration_success_message(self):
        return self.get_text(self.registration_success)

    def get_existing_email_error(self):
        return self.get_text(self.validation_email_exists)





