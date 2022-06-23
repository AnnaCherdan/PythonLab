import pytest


@pytest.fixture
def fix():
    input_pet = {
        "id": 219,
        "category": {
            "id": 25,
            "name": "Vrapp"
        },
        "name": "BOOGY",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 14,
                "name": "string"
            }
        ],
        "status": "available"
    }

    header = {'accept': 'application/json', 'Content-Type': 'application/json'}
    return input_pet, header
