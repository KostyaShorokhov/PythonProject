# test_bookings.py
from urllib.parse import quote_plus
from conftest import Booking


class TestBookings:
    def test_get_booking(self, base_session, booking_fixture):
        booking_id = booking_fixture
        response = base_session.get(Booking.get_booking(booking_id))
        assert response.status_code == 200
        data = response.json()
        assert isinstance(data, dict), f'Expected dictionary, received {type(data)}'

    def test_update_booking_url_encoded(self, base_session, booking_fixture):
        booking_id = booking_fixture
        update_data = {
            "firstname": "James",
            "lastname": "Brown",
            "totalprice": 10000,
            "depositpaid": True,
            "bookingdates[checkin]": "2020-11-01",  # Используйте квадратные скобки для вложенных ключей
            "bookingdates[checkout]": "2021-07-01",
            "additionalneeds": "Breakfast"
        }

        # Подготовим правильные заголовки и данные
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded',
            'Accept': 'application/x-www-form-urlencoded'
        }

        # Готовим данные в формате HTML-формы
        form_data = "&".join([f'{quote_plus(key)}={quote_plus(str(value))}' for key, value in update_data.items()])

        # Посылаем запрос с нужными заголовками и формой
        response = base_session.put(Booking.update_booking(booking_id), data=form_data, headers=headers)
        assert response.status_code == 200

    def test_update_booking_json_usage(self, base_session, booking_fixture):
        booking_id = booking_fixture
        update_data = {
            "firstname": "James",
            "lastname": "Brown",
            "totalprice": 10000,
            "depositpaid": True,
            "bookingdates": {
                "checkin": "2020-11-01",
                "checkout": "2021-07-01"
            },
            "additionalneeds": "Breakfast"
        }

        # Установка заголовков для JSON
        headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        }

        # Передача JSON-данных
        response = base_session.put(Booking.update_booking(booking_id), json=update_data, headers=headers)
        assert response.status_code == 200


