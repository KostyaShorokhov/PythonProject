# conftest.py
import pytest
import requests

class BaseEndpoint:
    """Базовый класс для хранения общей информации"""
    BASE_URL = 'https://restful-booker.herokuapp.com/'

class Booking(BaseEndpoint):
    """Класс для хранения путей, связанных с бронированием"""
    BOOKING_PATH = '/booking'

    @classmethod
    def get_booking(cls, booking_id):
        return cls.BASE_URL + cls.BOOKING_PATH + '/' + str(booking_id)

    @classmethod
    def create_booking(cls):
        return cls.BASE_URL + cls.BOOKING_PATH

    @classmethod
    def update_booking(cls, booking_id):
        return cls.BASE_URL + cls.BOOKING_PATH + '/' + str(booking_id)

    @classmethod
    def delete_booking(cls, booking_id):
        return cls.BASE_URL + cls.BOOKING_PATH + '/' + str(booking_id)

@pytest.fixture(scope='session')
def base_session():
    """
    Создает базовую сессию с авторизацией через cookie.
    """
    request_body = {"username": "admin", "password": "password123"}
    auth_response = requests.post(BaseEndpoint.BASE_URL + '/auth', json=request_body)
    token = auth_response.json()['token'] if auth_response.ok else None

    session = requests.Session()
    session.cookies.set("token", token)
    return session

@pytest.fixture(scope='function')
def booking_fixture(base_session):
    booking_data = {
        "firstname": "Jim",
        "lastname": "Beam",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": "Breakfast"
    }
    response = base_session.post(Booking.create_booking(), json=booking_data)
    assert response.status_code == 200
    booking_id = response.json().get('bookingid')
    yield booking_id
    base_session.delete(Booking.delete_booking(booking_id))
