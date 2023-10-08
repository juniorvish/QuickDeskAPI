```python
import requests
import json

def get_chart_of_accounts():
    response = requests.get('https://api.quickbooks.com/v3/company/123146206183384/chartofaccounts')
    data = response.json()
    return data

def post_to_deskera(data):
    headers = {'Content-Type': 'application/json'}
    response = requests.post('https://api.deskera.com/chartofaccounts', headers=headers, data=json.dumps(data))
    return response.status_code

def import_to_deskera():
    data = get_chart_of_accounts()
    status = post_to_deskera(data)
    return status
```