import logging
import string
from random import random

import pytest


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
