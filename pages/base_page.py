from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.expected_conditions import element_to_be_clickable
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    def __init__(self,driver):
        self.driver=driver #instance variable
        self.wait=WebDriverWait(driver,10) #instance variable
    


    def click(self,locator):
        self.wait.until(EC.element_to_be_clickable(locator)).click()


    def enter_text(self,locator,text):
        element = self.wait.until(EC.visibility_of_element_located(locator))
        element.clear()
        element.send_keys(text)

    def get_text(self,locator):
        return self.wait.until(EC.visibility_of_element_located(locator)).text

    def get_title(self):
        return self.driver.title

    def get_current_url(self):
        return self.driver.current_url

    def is_visible(self,locator):
        element=self.wait.until(EC.visibility_of_element_located(locator))
        return  element.is_displayed()
    
    def get_alert_text(self):
        alert=self.wait.until(EC.alert_is_present())
        return alert.text

    def accept_alert(self):
       alert=self.driver.switch_to.alert
       alert.accept()

    def select_checkbox(self,locator):
        checkbox=self.wait.until(EC.element_to_be_clickable(locator))
        if not checkbox.is_selected():
            checkbox.click()

    def get_attribute(self, locator, attr_name):
        return self.find(locator).get_attribute(attr_name)

    
