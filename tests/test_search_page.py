import pytest


from utilities.helpers import load_test_data

data = load_test_data("../test_data/search_data.json")



@pytest.mark.smoke
@pytest.mark.parametrize("search_product",data["valid_search"])
def test_search_with_valid_product_displays_results(home_page,search_page,search_product):
    # Perform search
    home_page.search_product(search_product["search_text"])

    # Step 2: Validate results
    assert search_page.is_product_displayed(search_product["search_text"]), \
        f"Search failed for {search_product['search_text']}"



@pytest.mark.regression
@pytest.mark.parametrize("search_product",data["valid_search"])
def test_search_results_count_is_positive(home_page,search_page,search_product):
    home_page.search_product(search_product["search_text"])
    result_count = search_page.get_search_results_count()
    assert result_count  > 0,f"No products displayed for {search_product['search_text']}"

@pytest.mark.regression
@pytest.mark.parametrize("search_product",data["key_word_search"])
def test_search_results_relevance(home_page,search_page,search_product):
    keyword = search_product["search_text"]

    # Step 1: Perform search
    home_page.search_product(keyword)

    # Step 2: Validate results exist
    count = search_page.get_search_results_count()
    assert count > 0, f"No results found for keyword :{keyword}"

    # Step 3: Fetch product titles
    products=search_page.get_all_product_titles()

    # Step 4: Validate relevance
    for product in products:
        assert keyword.lower() in product.lower(), f"Irrelevant product found: {product}"


@pytest.mark.negative
@pytest.mark.parametrize("search_product",data["invalid_search"])
def test_search_with_invalid_product_shows_no_results(search_product,search_page,home_page):
    keyword=search_product["search_text"]

    #search for product
    home_page.search_product(keyword)

    #wait and get the error text
    error_message=search_page.get_text(search_page.result_error)

    #verify no products exists for invalid data

    assert "No products were found" in error_message,f"Expected no results message for keyword: {keyword}"

    # Validate no products exist
    count = search_page.get_search_results_count()
    assert count == 0, f"Products found for invalid keyword: {keyword}"


@pytest.mark.negative
@pytest.mark.parametrize("search_text",[""])
def test_search_with_empty_search(home_page,search_page,search_text):
    home_page.search_product(search_text)

    alert_text=search_page.get_alert_text()

    assert "Please enter" in alert_text

    search_page.accept_alert()



@pytest.mark.smoke1
@pytest.mark.parametrize("search_product",data["valid_search"])
def test_search_and_open_product(home_page,search_page,search_product):
    keyword=search_product['search_text']
    home_page.search_product(keyword)   # reuse existing method
    product_page=search_page.click_product(keyword)  # additional step
    assert product_page.is_product_visible()







