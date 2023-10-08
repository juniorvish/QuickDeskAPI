```python
from flask import Flask, request, jsonify
from quickbooks_api import get_quickbooks_data
from deskera_api import send_data_to_deskera

app = Flask(__name__)

@app.route('/import', methods=['POST'])
def import_data():
    data = request.get_json()
    quickbooks_data = get_quickbooks_data(data['quickbooks_credentials'])
    response = send_data_to_deskera(quickbooks_data, data['deskera_credentials'])
    return jsonify(response)

if __name__ == "__main__":
    app.run(debug=True)
```