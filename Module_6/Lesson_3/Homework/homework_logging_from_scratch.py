import getpass
import hashlib
import logging
import time

logger = logging.getLogger("password_checker")


def check_password(password: str) -> tuple[bool, dict]:
    validation_check = {
        "has_upper": False,
        "has_lower": False,
        "has_digit": False,
        "has_special": False,
        "is_eight_len": False,
    }

    special_symbols = "!@#$%^&*()-+=_"

    if len(password) >= 8:
        validation_check["is_eight_len"] = True

    for char in password:
        if char.isupper():
            validation_check["has_upper"] = True
        elif char.islower():
            validation_check["has_lower"] = True
        elif char.isdigit():
            validation_check["has_digit"] = True
        elif char in special_symbols:
            validation_check["has_special"] = True

    if all(validation_check.values()):
        return True, validation_check
    else:
        return False, validation_check


def input_password():
    password: str = getpass.getpass()

    if not password:
        logger.warning("Вы ввели пустой пароль.")
        return False

    is_good_pass, check = check_password(password)

    if is_good_pass:
        logger.info("Пароль хороший")
    else:
        return_text = "Пароль не надёжный: для хорошего пароля требуется:\n"
        for category in check:
            if not check[category]:
                if category == "is_eight_len":
                    return_text += f"- {category}: длина пароля должна быть как минимум 8 символов\n"
                elif category == "has_digit":
                    return_text += f"- {category}: пароль должен содержать как минимум одну цифра\n"
                elif category == "has_upper":
                    return_text += f"- {category}: пароль должен содержать как минимум одну большую букву\n"
                elif category == "has_lower":
                    return_text += f"- {category}: пароль должен содержать как минимум одну маленькую букву\n"
                elif category == "has_special":
                    return_text += f"- {category}: пароль должен содержать как минимум один специальный символ (!@#$%^&*()-+=_)\n"
        logger.warning(return_text)

    try:
        hasher = hashlib.md5()
        logger.debug(f"Мы создали объект hasher {hasher!r}")

        hasher.update(password.encode("utf-8"))

        if hasher.hexdigest() == "098f6bcd4621d373cade4e832627b4f6":
            return True
    except ValueError as exc:
        logger.exception("Вы ввели некорректный символ", exc_info=exc)

    return False


def set_attempts() -> int:
    attempts: int = 0

    right_pass = False
    while not right_pass:
        try:
            attempts = int(
                input("Введите кол-во попыток для ввода пароля (от 2 до 10): ")
            )

            if not (2 <= attempts <= 10):
                raise ValueError

        except ValueError:
            time.sleep(0.3)

            logger.warning(
                "Количество попыток должно быть целочисленным значением от 2 до 10!"
            )

        else:
            right_pass = True

    return attempts


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    logger.info("Вы пытаетесь аутентифицироваться в Skillbox")
    time.sleep(0.3)
    count_number: int = set_attempts()
    tries = count_number
    logger.info(f"У вас есть {count_number} попыток")

    while tries > 0:
        if input_password():
            exit(0)
        tries -= 1

    logger.error(f"Пользователь {count_number} раз ввёл неправильный пароль!")
    exit(1)
