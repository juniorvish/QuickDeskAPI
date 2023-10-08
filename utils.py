```python
import json

def transform_data(data):
    """
    This function transforms the data from Quickbooks API to match the Deskera API schema.
    """
    transformed_data = []

    for item in data:
        transformed_item = {
            'name': item['Name'],
            'description': item['Description'],
            'type': item['AccountType'],
            'sub_type': item['AccountSubType'],
            'current_balance': item['CurrentBalance'],
            'currency': item['CurrencyRef']['name']
        }
        transformed_data.append(transformed_item)

    return transformed_data

def validate_response(response):
    """
    This function validates the response from the API.
    """
    if response.status_code == 200:
        return True
    else:
        return False

def parse_json(response):
    """
    This function parses the JSON response from the API.
    """
    return json.loads(response.text)
```