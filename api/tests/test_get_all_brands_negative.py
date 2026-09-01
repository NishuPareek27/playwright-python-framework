import allure
import json
from api.clients.api_clients import APIClient
from utils.logger import get_logger
from api.endpoints import *


logger = get_logger()
client = APIClient()

@allure.feature("Brands API: Get All Brands")
@allure.story("Brands API: Validate Invalid http method")
def test_get_all_brands_invalid_http_method():

    logger.info("Sending POST request to GET Brands API(Invalid HTTP Method)")
    with allure.step("Sending POST request to GET Brands API(Invalid HTTP Method)"):
        response = client.post(
            BASE_URL + BRANDS_LIST
        )

    response_json = response.json()
    logger.info(
        f"Brands: {json.dumps(response_json, indent=4)}"
    )
    allure.attach(
        json.dumps(response_json, indent=4),
        name="Brands API Response",
        attachment_type=allure.attachment_type.JSON
    )

    with allure.step("Validate Status Code"):
        assert response.status_code == 200
    with allure.step("Validate responseCode"):    
        assert response_json["responseCode"] == 405
    with allure.step("Validate error message"):    
        assert response_json["message"] == "This request method is not supported."

@allure.feature("Brands API: Get All Brands")
@allure.story("Brands API: Validate Invalid endpoint")
def test_get_all_brands_invalid_endpoint():

    response = client.get(
        BASE_URL + BRANDS_LIST+"/s"
    )

    # response_json = response.json()

    allure.attach(
        str(response.status_code),
        name="Status code",
        attachment_type=allure.attachment_type.TEXT
    )

    allure.attach(
        response.text,
        name="Response Body",
        attachment_type=allure.attachment_type.TEXT
    )

    with allure.step("Validate status code"):
        assert response.status_code == 404