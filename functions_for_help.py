import random
import string


# генерация имени из букв латинского алфавита
# верхнего и нижнего регистра
def random_name():
    return (f"{''.join(random.choice(string.ascii_uppercase) for i in range(1))}"
            f"{''.join(random.choice(string.ascii_lowercase) for i in range(4))}")


# генерация почты из букв латинского алфавита и цифр
def random_email():
    return (f"{''.join(random.choice(string.ascii_lowercase) for i in range(4))}_"
            f"{''.join(random.choice(string.ascii_lowercase) for i in range(6))}_"
            f"{random.randint(1000, 9999)}@yandex.ru")


# генерация пароля из букв латинского алфавита и цифр
# длина пароля - 6 символов
def random_password():
    return ''.join(random.sample(string.ascii_letters + string.digits, 6))

# генерация пароля из букв латинского алфавита и цифр
# длина меньше 6 символов
def random_incorrect_password():
    return ''.join(random.sample(string.ascii_letters + string.digits, 5))

# генерация почты только с именем почтового ящика
def mail_without_domen():
    return f"{''.join(random.choice(string.ascii_lowercase) for i in range(5))}_{random.randint(1000, 9999)}"

print(mail_without_domen())

# генерация почты с ошибкой в домене
def mail_with_error_domain():
    return f"{''.join(random.choice(string.ascii_lowercase) for i in range(5))}_{random.randint(1000, 9999)}@yandex."
