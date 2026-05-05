import pytest

from utilities.helpers import load_test_data

data = load_test_data("../test_data/search_data.json")


from pages.shopping_cart_page import ShoppingCartPage

@pytest.mark.parametrize("search_product",data["valid_search"])
def test_add_product(home_page,search_page,search_product,product_page,shopping_page):

    #Search product
    keyword = search_product['search_text']
    home_page.search_product(keyword)  # reuse existing method

    #Select Product
    product_page = search_page.click_product(keyword)  # additional step
    assert product_page.is_product_visible()

    # 3. Capture product details
    product_price = product_page.get_product_price()
    product_qty = product_page.get_product_quantity()

    # 4. Add to cart
    product_page.add_to_cart()
    assert product_page.verify_success()

    # 5. Go to cart
    product_page.click_shopping_cart_link()

    # 6. Cart validations
    assert shopping_page.is_product_present(keyword), f"{keyword} does not exist"










