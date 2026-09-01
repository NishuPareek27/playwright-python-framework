import requests
import json
import allure
from api.clients.api_clients import APIClient
from utils.logger import get_logger
from api.endpoints import *

logger = get_logger()
client = APIClient()
@allure.feature("Products API: Get All Products")
@allure.story("Products API: Validate with invalid endpoint")
def test_get_all_products_with_invalid_endpoint():

    logger.info("Sending GET request to Products API with invalid endpoint")
    with allure.step("Sending GET request to Products API with invalid endpoint"):
        response = client.get(
            BASE_URL + PRODUCTS_LIST + "s"
        )

    content_type = response.headers.get("Content-Type")
    print(f"Content-Type: {content_type}")

# Attaching HTML response to Allure Report
    allure.attach(
        str(response.status_code),
        name="Status Code",
        attachment_type=allure.attachment_type.TEXT
    )

    allure.attach(
        response.text,
        name="Response Body",
        attachment_type=allure.attachment_type.TEXT
    )

    logger.info(f"Status Code: {response.status_code}")
    with allure.step("Validate status code for invalid endpoint"):
        assert response.status_code == 404


@allure.feature("Products API: Get All Products")
@allure.story("Products API: Validate with invalid http methods")
def test_invalid_http_method_for_get_all_products():

    logger.info("Sending POST request to GET Products API(Invalid HTTP Method)")
    with allure.step("Sending POST request to GET Products API(Invalid HTTP Method)"):
        response = client.post(
            BASE_URL + PRODUCTS_LIST
        )
        content_type = response.headers.get("Content-Type")
        logger.info(f"Content-Type: {content_type}")

    response_json = response.json()
    logger.info(
        f"Products: {json.dumps(response_json, indent=4)}"
    ) 
    allure.attach(
        json.dumps(response_json, indent=4),
        name="Products API Response",
        attachment_type=allure.attachment_type.JSON
    )

    assert response.status_code == 200
    assert response_json["responseCode"] == 405
    