import requests


def update_Data(conception, conception_cost, electrical_load):
    url = "http://127.0.0.1:8000/api/smartmeter/A220150279/"

    payload = "{\n\t\"conception\": %s,\n    \"conception_cost\": %s,\n    \"electrical_load\": %s\n}" % (
        str(conception), str(conception_cost), str(electrical_load))
    headers = {
        'Authorization': 'Token 7c36a899778d32f7ad54dc953a810c70b67d3526 ',
        'Content-Type': 'application/json'
    }

    response = requests.request("PUT", url, headers=headers, data=payload)

    print(response.text.encode('utf8'))



