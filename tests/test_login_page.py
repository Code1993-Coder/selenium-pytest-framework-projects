import pytest
from Demos.win32ts_logoff_disconnected import username

from conftest import home_page
from pages.sign_in_page import SigninPage
from utilities.helpers import generate_email
from utilities.helpers import load_test_data

data = load_test_data("../test_data/registration_data.json")

@pytest.mark.smoke
def test_login_success_with_valid_credentials(home_page,login_page,existing_customer):
    home_page.click_logout()
    home_page.click_login()

    email = existing_customer["email"]
    password = existing_customer["password"]

    login_page.login(email, password)

    assert home_page.is_login_successful()

    print(f"Logged in with {existing_customer["email"]} ")

@pytest.mark.negative
@pytest.mark.parametrize("user",data["invalid_login_credentials"])
def test_login_with_invalid_credentials(home_page,login_page,user):
    home_page.click_login()

    email=generate_email()
    login_page.login(email,user["password"])

    assert login_page.get_invalid_credentials_error()

    print(f"Tried login with invalid user {email} and {user["password"]}")

@pytest.mark.negative
def test_login_with_unregistered_email(home_page,login_page,existing_customer):
    home_page.click_logout()
    home_page.click_login()

    email=generate_email()
    password=existing_customer["password"]

    login_page.login(email,password)

    assert login_page.get_invalid_credentials_error()

    print(f"Tried with unregistered email {email}")

@pytest.mark.negative
@pytest.mark.parametrize("user",data["missing_credentials"])
def test_login_empty_fields(home_page,login_page,user):

    home_page.click_login()

    email=user['email']
    password=user['password']

    login_page.login(email,password)

    error_message = login_page.get_customer_not_found_error()
    assert "No customer account found" in error_message

    print(f"Tried empty credentials → Got error: {error_message}")

@pytest.mark.negative
@pytest.mark.parametrize("user",data["invalid_email_format"])
def test_invalid_email_format(home_page,login_page,user):

    home_page.click_login()
    email = user['email']
    password = user['password']

    login_page.login(email, password)

    assert login_page.get_email_format_error()

    print(f"Tried with invalid email format and got the error as {login_page.get_email_format_error()}")









