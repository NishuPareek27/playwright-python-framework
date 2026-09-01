import allure
import json
from api.clients.api_clients import APIClient
from utils.logger import get_logger
from api.endpoints import *


logger = get_logger()
client = APIClient()

@allure.feature("Brands API: Get All Brands")
@allure.story("Get all Brands: Validate Response and Brands details")
def test_get_all_brands():
    response = client.get(
        BASE_URL + BRANDS_LIST
    )

    assert response.status_code == 200


    response_json = response.json()         # Parsing the JSON response

    allure.attach(
    json.dumps(response_json, indent=4),
    name="Brands API Response",
    attachment_type=allure.attachment_type.JSON
    )

    logger.info(
        f"Brands: {json.dumps(response_json, indent=4)}"

    )

    brands = response_json["brands"]
    assert brands, "Brands list is empty"          # This verifies response is not Empty

    first_brand = brands[0]


    assert response_json["responseCode"] == 200     # This verifies the responseCode of the response

    assert "id" in first_brand
    assert "brand" in first_brand
    assert first_brand["id"] > 0
    assert first_brand["brand"] != ""

    assert isinstance(first_brand["id"], int)       # This validates the DataType of the fields value
    assert isinstance(first_brand["brand"], str)

    assert "name" not in first_brand
    assert "price" not in first_brand
    assert "category" not in first_brand
    assert "usertype" not in first_brand
    assert "Invalid_field" not in first_brand


