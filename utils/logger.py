import logging


def get_logger(name: str) -> logging.Logger:
    """
    Возвращает настроенный логгер с обработчиком StreamHandler и соответствующим форматом.
    """
    # Получаем существующий логгер или создаем новый
    logger = logging.getLogger(name)

    # Устанавливаем уровень логирования
    logger.setLevel(logging.DEBUG)

    # Очищаем предыдущие обработчики, чтобы избежать дублирования
    for hdlr in logger.handlers[:]:
        logger.removeHandler(hdlr)

    # Настраиваем новый обработчик
    handler = logging.StreamHandler()
    handler.setLevel(logging.DEBUG)

    # Простой формат вывода
    formatter = logging.Formatter('%(asctime)s | %(name)s | %(levelname)s | %(message)s')
    handler.setFormatter(formatter)

    # Прикрепляем обработчик к логгеру
    logger.addHandler(handler)

    return logger
