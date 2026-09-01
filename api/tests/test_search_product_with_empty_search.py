import json
import allure
from api.clients.api_clients import APIClient
from utils.logger import get_logger
from api.endpoints import *


logger = get_logger()
client = APIClient()


def test_search_product_with_empty_search():

    payload = { }    

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

    logger.info(f"length of response are: {len(response_json)}")
    logger.info(f'keys are: {list(response_json.keys())}')
