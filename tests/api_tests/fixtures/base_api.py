import logging
import string
from random import random

import pytest

from url_constants import API_URL
from utils.api_methods import BaseApiMethods


def setup_logger():
    # Базовая настройка уровня логирования
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)

    # Формат сообщений
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

    # Пишем в консоль
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)


# Фикстура для логирования
@pytest.fixture(scope="session", autouse=True)
def log_fixture(request):
    """Настройка общего логгера"""
    setup_logger()

import pytest


@pytest.fixture()
def generate_random_number_of_length(length):
    """
    Генерирует случайное число заданной длины.

    Args:
        length: Желаемая длина числа.

    Returns:
        Строка, представляющая случайное число заданной длины.
    """
    if length <= 0:
        return "0"

    # Генерируем строку из случайных цифр
    random_number_str = ''.join(random.choice(string.digits) for _ in range(length))

    # Если длина сгенерированной строки больше требуемой, обрезаем ее
    if len(random_number_str) > length:
      random_number_str = random_number_str[:length]

    return random_number_str


