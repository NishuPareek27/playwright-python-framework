import json
import allure
from api.clients.api_clients import APIClient
from utils.logger import get_logger
from api.endpoints import BASE_URL

logger = get_logger()
client = APIClient()

@allure.feature("Products API: Get All Products")
@allure.story("Get All Products: Validate Response and Product Details")
def test_get_all_products():


    logger.info("Sending GET request to Products API")
    with allure.step("Send GET request to Products API"):
        response = client.get(
            f"{BASE_URL}/api/productsList"
        )

    with allure.step("Validate status code"):    
        assert response.status_code == 200

    with allure.step("Parse response JSON"):
        response_json = response.json()         # Parse JSON response here

        # Attach response to Allure report
        allure.attach(
            json.dumps(response_json, indent=4),
            name="Products API Response",
            attachment_type=allure.attachment_type.JSON
        )


    logger.info(f"Status Code: {response.status_code}")
    with allure.step("Validate response code"):
        assert response_json["responseCode"] == 200

        products = response_json["products"]        # Extract the list of products from the response JSON

        assert len(products) > 0

        first_product = products[0]             # # Get first product from the products list

        assert "id" in first_product
        assert "name" in first_product
        assert "price" in first_product
        assert "brand" in first_product
        assert "category" in first_product

    with allure.step("Validate first_product nested category and usertype"):
        category = first_product["category"]
        assert "category" in category
        assert "usertype" in category
        assert category["usertype"]["usertype"] != ""
        assert category["category"] != ""

        assert first_product["id"] > 0
        assert first_product["name"] != ""
        assert first_product["price"] != ""
        assert first_product["brand"] != ""

        logger.info(
            f"Response Code: {response_json['responseCode']}"
        )    

        logger.info(
            f"Products: {json.dumps(products, indent=4)}"
        )       # dumps means, converting the JSON object into a String representation of the JSON object. The indent=4 is used to format the output with an indentation of 4 spaces for better readability.

