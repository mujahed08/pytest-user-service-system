from faker import Faker
from faker.providers import profile
from faker.providers import color
import requests
import json
from tests.commons.logger import get_logger

logger = get_logger('test_api.py')
fake = Faker()
fake.add_provider(profile)
fake.add_provider(color)


def test_create_role():
    role = {
        "id" : 2,
		"name" : "ROLE_ADMIN"
    }
    logger.info(role)
    response = requests.post("http://127.0.0.1:8000/roles", data=json.dumps(role))
    logger.info(response.json())
    assert response.status_code == 200

def test_update_role():
    id = 99
    role = {
        "name" : "ROLE_TEST_UPDATE"
    }
    logger.info(role)
    response = requests.put(f'http://127.0.0.1:8000/roles/{id}', data=json.dumps(role))
    logger.info(response.json())
    assert response.status_code == 200

def test_delete_role():
    id = 99
    response = requests.delete(f'http://127.0.0.1:8000/roles/{id}')
    assert response.status_code == 200

def test_get_users():
    response = requests.get("http://127.0.0.1:8000/users")
    logger.info(response.json())
    assert response.status_code == 200

def test_create_user():
    simple = fake.simple_profile()
    logger.info(simple)
    logger.info(simple['username'])
    user = {
		"name" : simple['name'],
        "username" : simple['username'],
        "password" : fake.color_name(),
        "enabled": True
    }
    logger.info(user)
    response = requests.post("http://127.0.0.1:8000/users", data=json.dumps(user))
    logger.info(response.json())
    assert response.status_code == 200

def test_get_user():
    response = requests.get("http://127.0.0.1:8000/users/4")
    logger.info(response.json())
    assert response.status_code == 200

def test_update_user():
    id = 13
    simple = fake.simple_profile()
    logger.info(simple)
    logger.info(simple['username'])
    user = {
		"name" : simple['name'],
        "enabled": False
    }
    logger.info(user)
    response = requests.put(f'http://127.0.0.1:7000/users/{id}', data=json.dumps(user))
    logger.info(response.json())
    assert response.status_code == 200

def test_delete_user():
    simple = fake.simple_profile()
    logger.info(simple)
    logger.info(simple['username'])
    user = {
		"name" : simple['name'],
        "username" : simple['username'],
        "password" : fake.color_name(),
        "enabled": True
    }
    logger.info(user)
    response = requests.post("http://127.0.0.1:8000/users", data=json.dumps(user))
    logger.info(response.json())
    user = response.json();
    id = user['id']
    deleted = requests.delete(f'http://127.0.0.1:8000/users/{id}')
    assert deleted.status_code == 200

def test_role():
    logger.info('count: %d', 5)
    assert 200 == 200

def test_assign_roles():
    roles = ['ROLE_TEST2', 'ROLE_TEST3', 'ROLE_SA']
    logger.info(roles)
    response = requests.post("http://127.0.0.1:8000/users/3/roles", data=json.dumps(roles))
    logger.info(response.json())
    assert response.status_code == 200

def test_remove_roles():
    roles = ['ROLE_TEST3', 'ROLE_TEST2']
    logger.info(roles)
    response = requests.delete("http://127.0.0.1:8000/users/3/roles", data=json.dumps(roles))
    logger.info(response.json())
    assert response.status_code == 200

def test_roles_ops():
    simple = fake.simple_profile()
    logger.info(simple)
    logger.info(simple['username'])
    user = {
		"name" : simple['name'],
        "username" : simple['username'],
        "password" : fake.color_name(),
        "enabled": True
    }
    role = {
        "id" : 99,
		"name" : "ROLE_TEST"
    }
    user_role = {
        "user" : user,
        "roles" : [role]
    }
    logger.info('	>')
    logger.info('	>')
    logger.info('	>')
    logger.info(user_role)
    response = requests.post("http://127.0.0.1:8000/roles/ops", data=json.dumps(user_role))
    logger.info(response.json())
    assert response.status_code == 200
