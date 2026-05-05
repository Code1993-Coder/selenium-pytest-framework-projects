import json

import pytest


from pages.home_page import HomePage
from pages.search_results_page import ProductDetailsPage





#Navigation
def test_logo_visible(browser_instance):
    home = HomePage(browser_instance)

    assert home.is_visible(home.logo)

def test_register_navigation(browser_instance):
    home = HomePage(browser_instance)

    assert home.is_visible(home.register)

    home.click_register()

    assert "register" in home.get_current_url().lower()

def test_login_navigation(browser_instance):

    home = HomePage(browser_instance)

    assert home.is_visible(home.login)

    home.click_login()

    assert "login" in home.get_current_url().lower()


def test_cart_navigation(browser_instance):

    home = HomePage(browser_instance)

    assert home.is_visible(home.cart)

    home.click_cart()

    assert "cart" in home.get_current_url().lower()

def test_wishlist_navigation(browser_instance):

    home = HomePage(browser_instance)

    assert home.is_visible(home.wishlist)

    home.click_wishlist()

    assert "wishlist" in home.get_current_url().lower()

#Search product/store
def test_search_product_gui(browser_instance):
    home = HomePage(browser_instance)

    assert home.is_visible(home.search_box)

    assert home.is_visible(home.search_button)



@pytest.mark.smoke2
@pytest.mark.parametrize( "menu_name, sub_menu",[
        ("Apparel & Shoes",None),
        ("Electronics", "Camera, photo"),
    ]
)
def test_select_menu(browser_instance,menu_name,sub_menu):
    home=HomePage(browser_instance)
    home.select_top_menu(menu_name,sub_menu)
    if sub_menu is None:
        assert menu_name.lower().replace(" & ", "-").replace(" ", "-").replace(",","-") in home.get_current_url().lower()
    else:
        assert sub_menu.lower().replace(" & ", "-").replace(",","-").replace(" ","-").replace(", ","-") in home.get_current_url().lower()







    









