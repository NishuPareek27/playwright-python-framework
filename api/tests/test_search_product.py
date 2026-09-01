import json
import allure
from api.clients.api_clients import APIClient
from utils.logger import get_logger
from api.endpoints import *


logger = get_logger()
client = APIClient()


def test_search_product():

    payload = {
        "search_product" : "top"
    }

    response = client.post(
        BASE_URL + SEARCH_PRODUCT,
        data=payload
    )


    response_json = response.json()
    allure.attach(
    json.dumps(response_json, indent=4),
    name="Search Product Response",
    attachment_type=allure.attachment_type.JSON
    )

    logger.info(
        f"\nSearched product is {json.dumps(response_json, indent=4)}"
    )
    assert response.status_code == 200
    assert response_json["responseCode"] == 200

    assert "responseCode" in response_json
    assert "products" in response_json

    logger.info( f"Top level Keys: {list(response_json.keys())}")

    products = response_json["products"]
    assert products, "Product list is empty"
    assert len(products) > 0

    first_product = products[0]
    logger.info( f"first_product Keys: {list(first_product.keys())}")

    assert "id" in first_product
    assert "name" in first_product
    assert "price" in first_product
    assert "brand" in first_product
    assert "category" in first_product

    assert isinstance(first_product["id"], int)
    assert isinstance(first_product["name"], str)
    assert isinstance(first_product["price"], str)
    assert isinstance(first_product["brand"], str)
    assert isinstance(first_product["category"], dict)

    # Category is usually a nested object in the response
    category = first_product["category"]
    assert "category" in category
    assert "usertype" in category

    assert category['usertype']['usertype'] != ''
    assert category['category'] != ''
    assert isinstance(category['usertype'], dict)
    assert isinstance(category['category'], str)
    assert isinstance(category['usertype']['usertype'], str)
