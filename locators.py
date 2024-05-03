from selenium.webdriver.common.by import By

class Locators:
    input_field_name = (By.XPATH, './/label[text() = "Имя"]/following-sibling::input') #поле ввода имени
    input_field_email = (By.XPATH, './/label[text() = "Email"]/following-sibling::input') # поле ввода email
    input_field_password = (By.XPATH, './/label[text() = "Пароль"]/following-sibling::input') # поле ввода пароля
    registration_button = (By.XPATH, './/button[text()="Зарегистрироваться"]') # кнопка Зарегистироваться
    incorrect_password_message = (By.XPATH, './/p[text() = "Некорректный пароль"]') # сообщение об ошибке Некорректный пароль
    user_exists_message = (By.XPATH, './/div/main/div/p[text()="Такой пользователь уже существует"]') # сообщение об ошибке Такой пользователь уже существует
    main_login_button = (By.XPATH, './/button[text()="Войти в аккаунт"]') # кнопка Войти в аккаунт на главной странице
    login_button_login_page = By.XPATH, './/button[text()="Войти"]' # кнопка Войти на странице входа
    order_button = (By.XPATH, './/div/main/section[2]/div/button')  # Kнопка "Оформить заказ"
    personal_account_button = (By.XPATH, './/p[text()="Личный Кабинет"]')  # Kнопка "Личный кабинет
    recovery_pass_link = (By.XPATH, './/a[text()="Восстановить пароль"]')  # Ссылка "Восстановить пароль"
    recovery_pass_button = (By.XPATH, './/button[text()="Восстановить"]')  # Кнопка "Восстановить пароль"
    link_login_from_recovery_pass = (By.XPATH, './/a[text()="Войти"]')  #ссылка "Войти" со страницы восстановления пароля
    profile_link = (By.XPATH, './/a[text()="Профиль"]')  # ссылка "Профиль" в личном кабинете
    logout_button = (By.XPATH, './/button[text()="Выход"]')  # кнопка "Выход" из личного кабинета
    constructor_button = (By.XPATH, './/p[text()="Конструктор"]')  # кнопка "Конструктор"
    make_burger_tag_h1 = (By.XPATH, ".//h1[text()='Соберите бургер']")  # заголовок "Соберите бургер"
    logo_burgers = (By.CSS_SELECTOR, 'svg[xmlns = "http://www.w3.org/2000/svg"]')  # логотип стеллари бургерс
    span_sauses = ".//span[contains(text(),'Соусы')]"  # список "Соусы"
    span_buns = ".//span[contains(text(),'Булки')]"  # список "Булки"
    tab_select_in_constructor = ".//div[contains(@class, 'current')]/span"  # выбранный таб в конструкторе
    span_stuffing = ".//span[contains(text(),'Начинки')]"  # список "Начинки"


