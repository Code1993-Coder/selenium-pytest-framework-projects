from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class EmailAFriendPage(BasePage):
    friends_email_locator=(By.ID,"FriendEmail")
    your_email_address_locator=(By.ID,"YourEmailAddress")
    send_email_button_locator=(By.XPATH,"//input[@value='Send email']")
