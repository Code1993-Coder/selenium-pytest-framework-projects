import pytest

from utilities.helpers import load_test_data

data = load_test_data("../test_data/search_data.json")


@pytest.mark.smoke
@pytest.mark.parametrize("search_product",data["valid_search"])
@pytest.mark.parametrize("search_product",data["valid_search"])
def test_product_details_displayed(home_page,search_page,product_page,search_product):
    # search valid product
    keyword = search_product["search_text"]
    home_page.search_product(keyword)

    # click on product
    search_page.click_product(keyword)

    # verify product details are visible
    assert product_page.is_product_visible()




@pytest.mark.cart
@pytest.mark.parametrize("search_product",data["valid_search"])

def test_add_product_to_cart(home_page,search_page,product_page,search_product):

    #search valid product
    keyword=search_product["search_text"]
    home_page.search_product(keyword)

    #click on product
    search_page.click_product(keyword)

    #add the product to cart
    product_page.add_to_cart()

    #verify the product is added to cart from notification
    assert product_page.verify_success()

@pytest.mark.wishlist
@pytest.mark.parametrize("search_product",data["valid_search"])
def test_add_product_to_wishlist(home_page,search_page,product_page,search_product):

    #search valid product
    keyword=search_product["search_text"]
    home_page.search_product(keyword)

    #click on product
    search_page.click_product(keyword)

    #add the product to cart
    product_page.add_to_wishlist()

    # verify the product is added to cart from notification
    assert product_page.verify_success()

@pytest.mark.quantity
@pytest.mark.parametrize("search_product",data["valid_search"])
def test_add_to_cart_with_updated_quantity(home_page,search_page,product_page,search_product):
    # search valid product
    keyword = search_product["search_text"]
    qty= search_product.get("quantity")
    home_page.search_product(keyword)

    # click on product
    search_page.click_product(keyword)

    # Update quantity only when provided
    if qty is not None:
        assert product_page.set_quantity(qty),f" Quantity field not available"

    #add the product to cart
    product_page.add_to_cart()

    #verify the product is added to cart from notification

    assert product_page.verify_add_to_cart_success()

@pytest.mark.size
@pytest.mark.parametrize("search_product",data["valid_search"])
def test_select_size_and_add_to_cart(home_page,search_page,product_page,search_product):
    # search valid product
    keyword = search_product["search_text"]
    size=search_product.get("size")


    home_page.search_product(keyword)

    # click on product
    search_page.click_product(keyword)

    #select size
    if size is not None:
       assert product_page.select_size(size),f"Size {size} is not available."
    # add the product to cart
    product_page.add_to_cart()

    # verify the product is added to cart from notification
    assert product_page.verify_add_to_cart_success()

@pytest.mark.color
@pytest.mark.parametrize("search_product", data["valid_search"])
def test_select_color_and_add_to_cart(home_page, search_page, product_page, search_product):
    # search valid product
    keyword = search_product["search_text"]
    color = search_product.get("color")

    home_page.search_product(keyword)

    # click on product
    search_page.click_product(keyword)

    # select color (if available)
    if color is not None:
        assert product_page.select_color(color), f"Color {color} not available"

    product_page.add_to_cart()

    assert product_page.verify_add_to_cart_success()

@pytest.mark.smoke
@pytest.mark.parametrize("search_product", data["valid_search"])
def test_product_flow(home_page, search_page, product_page, search_product):
    # search valid product
    keyword = search_product["search_text"]
    color = search_product.get("color")
    size=search_product.get("size")
    qty = search_product.get("quantity")


    home_page.search_product(keyword)

    # click on product
    search_page.click_product(keyword)

    # select color (if available)
    if color is not None:
        assert product_page.select_color(color), f"Color {color} not available"
    if  size is not None:
        assert product_page.select_size(size), f"Size {size} not available"
    if qty is not None:
            assert product_page.set_quantity(qty), f"Quantity field not available"


    product_page.add_to_cart()

    assert product_page.verify_add_to_cart_success()

@pytest.mark.negative
@pytest.mark.parametrize("search_product", data["valid_search"])
def test_empty_quantity(home_page,search_page,product_page,search_product):
    # search valid product
    keyword = search_product["search_text"]
    qty = search_product.get("quantity")

    home_page.search_product(keyword)

    # click on product
    search_page.click_product(keyword)

    #Verify for empty quantity error message is thrown
    assert qty == 0, "This test requires quantity 0" #this checks whether qty is 0 if not then it throws error-This test requires quantity 0
    product_page.set_quantity(qty)
    product_page.add_to_cart()

    assert "Quantity should be positive" in product_page.get_success_message_text()


@pytest.mark.negative
@pytest.mark.parametrize("search_product", data["valid_search"])
def test_max_quantity_limit(home_page,search_page,product_page,search_product):
    # search valid product
    keyword = search_product["search_text"]
    qty = search_product.get("quantity")

    home_page.search_product(keyword)

    # click on product
    search_page.click_product(keyword)

    # Verify for empty quantity error message is thrown
    assert qty>=300,"This test requires quantity >= 300"
    product_page.set_quantity(qty)
    product_page.add_to_cart()

    assert "The maximum quantity allowed for purchase is 300." in product_page.get_success_message_text()

