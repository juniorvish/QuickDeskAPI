```python
import requests
import json

def get_chart_of_accounts():
    url = "https://quickbooks.api.intuit.com/v3/company/<realmID>/query"
    query = {
        "query": "SELECT * FROM ChartOfAccounts"
    }
    headers = {
        "Accept": "application/json",
        "Authorization": "Bearer <access_token>"
    }

    response = requests.request("GET", url, headers=headers, params=query)
    data = json.loads(response.text)

    return data
```