import pytest
import requests

# Url
from main import post_pet_store, delete_pet_store

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
    # print(response)
    # print(response.status_code)
    # print(response_body)
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
    # print(response.url)

    response_body = response.json()
    # print(response_body)
    assert status_code == response.status_code
    assert id == response_body['id']
    assert email == response_body['email']
    assert password == response_body['password']
    assert phone == response_body['phone']


def test_post_pet():
    # Configuration
    expected_status_code = 200
    expected_id = 2345678
    expected_name = 'dodoko'
    expected_status = 'available'

    # request configuration
    endpoint = 'pet'
    json_path = 'C:/Users/William/PycharmProjects/fts_132_iterasys/test/db/pet1.json'
    json_config = 'rb'

    # Execute
    #  response = requests.post(

    #     url=f'{url_base}/pet',
    #     data=open('C:/Users/William/PycharmProjects/fts_132_iterasys/test/db/pet1.json', 'rb'),
    #     headers=headers
    # )

    # response_body = response.json()

    # response_delete = delete_pet_store(url_base, endpoint, expected_id)
    # response_delete_clean = response_delete.json()
    # print(response_delete_clean)
    delete_pet_store(url_base, endpoint, expected_id)

    response = post_pet_store(url_base, endpoint, json_path, json_config, headers)
    response_body = response.json()

    assert expected_status_code == response.status_code
    assert expected_id == response_body['id']
    assert expected_name == response_body['name']
    assert expected_status == response_body['status']


def test_get_pet():
    # Podemos criar dependencia entre os testes nessa situação? Ou o ideal seria criar um função pra isso?
    # request configuration
    endpoint = 'pet'
    json_path = 'C:/Users/William/PycharmProjects/fts_132_iterasys/test/db/pet1.json'
    json_config = 'rb'

    status_code = 200
    id = 2345678
    name = "dodoko"
    status = "available"

    post_pet_store(url_base, endpoint, json_path, json_config, headers)

    response = requests.get(

        url=f'{url_base}/pet/{id}',
        headers=headers
    )

    response_body = response.json()

    assert status_code == response.status_code
    assert id == response_body['id']
    assert name == response_body['name']
    assert status == response_body['status']


def test_put_pet():
    expected_status_code = 200
    expected_id = 2345678
    expected_name = "dodoko 5.0"
    expected_status = "available"

    response = requests.put(

        url=f'{url_base}/pet',
        data=open('C:/Users/William/PycharmProjects/fts_132_iterasys/test/db/pet2.json', 'rb'),
        headers=headers
    )

    response_body = response.json()

    assert expected_status_code == response.status_code
    assert expected_id == response_body['id']
    assert expected_name == response_body['name']
    assert expected_status == response_body['status']


def test_delete_pet():
    expected_status_code = 200
    expected_code = 200
    expected_type = "unknown"
    expected_message = "2345678"

    id = 2345678

    response = requests.delete(url=f'{url_base}/pet/{id}')

    response_body = response.json()

    assert expected_status_code == response.status_code
    assert expected_code == response_body['code']
    assert expected_type == response_body['type']
    assert expected_message == response_body['message']
