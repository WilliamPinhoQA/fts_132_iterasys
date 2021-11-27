import json

import requests

status_code = 200
id = 4217
username = 'will'
firstName = 'wd'
lastName = 'st5434ring'
email = 'bola@gmail.com'
password = 'laidsman217'
phone = '4000238922'
userStatus = 1

# Url
from main import post_pet_store, delete_pet_store

url_base = 'https://petstore.swagger.io/v2/user'
headers = {'Content-Type': 'application/json'}


def test_add_user():
    # Configuration
    expected_status_code = 200
    expected_code = 200
    expected_type = 'unknown'
    expected_message = '4217'

    # Execute
    response = requests.post(
        url={url_base},
        data=open('C:/Users/William/PycharmProjects/fts_132_iterasys/test/db/user1.json', 'rb'),
        headers=headers

    )

    response_body = response.json()
    # print(response)
    # print(response.status_code)
    # print(response_body)
    # Validation

    assert expected_status_code == response.status_code
    assert expected_code == response_body['code']
    assert expected_type == response_body['type']
    assert expected_message == response_body['message']


def test_get_user():
    response = requests.get(
        url=f'{url_base}/' + str(username),
        headers=headers
    )
    # print(response.url)

    response_body = response.json()
    # print(response_body)
    assert status_code == response.status_code
    assert id == response_body['id']
    assert email == response_body['email']
    assert password == response_body['password']
    assert phone == response_body['phone']


def test_user_login():
    user_headers = headers
    # sintaxe para add elementos como autorizações no header
    user_headers['username'] = f'{username}'
    user_headers['password'] = f'{password}'
    # print(user_headers)
    code = 200
    message = 'logged in user session:'

    response = requests.get(
        url=f'{url_base}/login',
        headers=user_headers
    )

    response_body = response.json()
    api_login_session = response_body['message'].translate({ord(i): None for i in 'logged in user session:'})

    print(api_login_session)

    print(user_headers)
    assert status_code == response.status_code
    assert code == response_body['code']
    assert message in response_body['message']
    assert isinstance(int(api_login_session), int)