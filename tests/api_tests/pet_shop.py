import random

import pytest

from url_constants import API_URL
from utils.base_client import BaseApiMethods


@pytest.fixture(scope="module")
def api_client():
    return BaseApiMethods(API_URL)

def test_create_and_manage_user(api_client):
    # Данные нового пользователя
    new_user = {
        "id": random.randint(1, 20),
        "username": f"testUser{random.randint(1, 100)}",
        "firstName": "John",
        "lastName": "Doe",
        "email": "johndoe@example.com",
        "password": "strong_password",
        "phone": f"{random.randint(1, 10)}",
        "userStatus": 0
    }

    # 1. Создаем пользователя
    created_user = api_client.create_user(new_user)
    response=created_user.json()
    print('response == ', response)
    assert response['code'] == 200, "Ошибка при создании пользователя."

    # 2. Проверяем существование пользователя по имени
    found_user = api_client.get_user_by_user_name(new_user["username"])
    resp=found_user.json()
    print('get_user ==', resp)
    assert resp["username"] == new_user["username"], "Пользователь не найден."

    # 3. Обновляем пользователя
    new_user["firstName"] = "Jane"
    updated_user = api_client.update_user(new_user["username"], new_user)
    resp = updated_user.json()
    assert resp["firstName"] == "Jane", "Ошибка при обновлении пользователя."

    # 4. Удаляем пользователя
    deleted_user = api_client.delete_user_by_user_name(new_user["username"])
    resp = deleted_user.json()
    assert resp["code"] == 200, "Ошибка при удалении пользователя."
