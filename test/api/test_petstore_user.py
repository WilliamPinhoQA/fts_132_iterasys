import pytest
import requests

# Url

url_base = 'https://petstore.swagger.io/v2'
headers = {'Content-Type': 'application/json'}


def test_add_user():
    # Configuration
    expected_status_code = 200
    expected_code = 200
    expected_type = 'unknown'
    expected_message = '4217'

    # Execute
    response = requests.post(
        url=f'{url_base}/user',
        data=open('C:/Users/William/PycharmProjects/fts_132_iterasys/test/db/user1.json', 'rb'),
        headers=headers

    )

    response_body = response.json()
    #print(response)
    #print(response.status_code)
    #print(response_body)
    # Validation

    assert expected_status_code == response.status_code
    assert expected_code == response_body['code']
    assert expected_type == response_body['type']
    assert expected_message == response_body['message']


def test_get_user():
    status_code = 200
    id = 4217
    username = 'will'
    firstName = 'wd'
    lastName = 'st5434ring'
    email = 'bola@gmail.com'
    password = 'laidsman217'
    phone = '4000238922'
    userStatus = 1

    response = requests.get(
        url=f'{url_base}/user/' + str(username),
        headers=headers
    )
    #print(response.url)

    response_body = response.json()
    #print(response_body)
    assert status_code == response.status_code
    assert id == response_body['id']
