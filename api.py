import requests


def update_ser_local(conception, conception_cost, electrical_load):
    url = "http://127.0.0.1:8000/api/smartmeter/A220150279/"

    payload = "{\n\t\"conception\": %s,\n    \"conception_cost\": %s,\n    \"electrical_load\": %s\n}" % (
        str(conception), str(conception_cost), str(electrical_load))
    headers = {
        'Authorization': 'Token 7c36a899778d32f7ad54dc953a810c70b67d3526 ',
        'Content-Type': 'application/json'
    }

    response = requests.request("PUT", url, headers=headers, data=payload)

    print(response.text.encode('utf8'))


def update_SER_consumption(conception, conception_cost, electrical_load):
    url = "http://127.0.0.1:8000/api/smartmeter/1234A6789x/"

    payload = {'consumption': f'{conception}', 'conception_cost': f'{conception_cost}'}
    files = [

    ]
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': 'Basic c2FkbWluOmFkbWluMjAwOTE='
    }

    response = requests.request("PUT", url, headers=headers, data=payload, files=files)

    print(response.text.encode('utf8'))

