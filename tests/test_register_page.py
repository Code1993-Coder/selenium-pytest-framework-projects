import pytest
import random


from pages.register_page import RegisterPage
from utilities.helpers import generate_email
from utilities.helpers import load_test_data


data = load_test_data("../test_data/registration_data.json")

#Positive Scenario
@pytest.mark.parametrize("user", data["positive_registration"])
@pytest.mark.smoke
def test_user_can_register_successfully(home_page,register_page,user):

    email = generate_email()
    register_page.register_user(user["gender"],user["first_name"],user["last_name"],email,user["password"])
    assert register_page.get_registration_success_message() == "Your registration completed"
    register_page.click_continue()

#Field Validations
@pytest.mark.parametrize("user",data["missing_first_name"])
@pytest.mark.validation
def test_registration_fails_when_first_name_missing(home_page,register_page,user):

    email = generate_email()
    register_page.register_user(user["gender"],user["first_name"],user["last_name"],email,user["password"])
    assert register_page.get_validation_message("FirstName") == "First name is required."

@pytest.mark.parametrize("user",data["missing_last_name"])
@pytest.mark.validation
def test_registration_fails_when_last_name_missing(home_page,register_page,user):

    email = generate_email()
    register_page.register_user(user["gender"],user["first_name"],user["last_name"],email,user["password"])
    assert "Last name is required" in register_page.get_validation_message("LastName")


@pytest.mark.validation
@pytest.mark.parametrize("user",data["missing_email"])
def test_register_with_missing_email(home_page,register_page,user):
    register_page.register_user(user["gender"],user["first_name"],user["last_name"],user['email'],user["password"])
    assert "Email is required" in register_page.get_validation_message("Email")


@pytest.mark.validation
@pytest.mark.parametrize("user",data["invalid_email_format"])
def test_invalid_email_format_validation(home_page,register_page,user):

    register_page.register_user(user["gender"],user["first_name"],user["last_name"],user['email'],user["password"])
    assert "Wrong email" in register_page.get_validation_message("Email")


#Business Rule Validations
@pytest.mark.validation
@pytest.mark.parametrize("user",data["password_mismatch"])

def test_registration_fails_when_password_mismatch(home_page,register_page,user):

    email=generate_email()
    register_page.register_user(user["gender"],user["first_name"],user["last_name"],email,user["password"],user["confirm_password"])
    assert "do not match" in register_page.get_validation_message("ConfirmPassword")

@pytest.mark.negative
@pytest.mark.parametrize("user",data['existing_user'])
def test_registration_fails_for_existing_email(home_page,register_page,user):

    email=generate_email()

    # First registration
    register_page.register_user(user["gender"],user["first_name"],user["last_name"],email,user["password"])
    register_page.click_continue()
    home_page.click_logout()

    # Try again

    home_page.click_register()
    register_page.register_user(user["gender"],user["first_name"],user["last_name"],email,user["password"])
    assert "already exists" in register_page.get_existing_email_error()

@pytest.mark.validation
@pytest.mark.parametrize("user",data['password_too_short'])
def test_password_too_short(home_page,register_page,user):
    email = generate_email()
    register_page.register_user(user["gender"],user["first_name"],user["last_name"],email,user["password"])
    assert "at least 6 characters" in register_page.get_validation_message("Password")

