# Регистрация - test_registration.py
Успешная регистрация: test_successful_registration

Регистрация с некорректным паролем: test_registration_with_invalid_password

Регистрация с уже существующим логином: test_existing_account_registration

# Вход - test_login.py
Вход по кнопке «Войти в аккаунт» на главной: test_login_from_main_page_login

Вход через кнопку «Личный кабинет»: test_login_from_main_page_personal

Вход через кнопку в форме регистрации: test_login_from_register_page

Вход через кнопку в форме восстановления пароля: test_login_from_recovery_page

# Переход в личный кабинет - test_move.py
Переход по клику на «Личный кабинет» для неавторизованного пользователя: test_personal_account_redirect

Переход из личного кабинета в конструктор для неавторизованного пользователя: test_navigation_via_constructor

Переход по клику на «Личный кабинет» для авторизованного пользователя: test_personal_account_redirect_to_personal_account

Переход из личного кабинета в конструктор для авторизованного пользователя: test_navigation_via_constructor_personal_account

Переход по клику на «Конструктор»: test_navigation_via_constructor

Переход по клику на логотип Stellar Burgers: test_navigation_via_logo

Переход по клику на «Конструктор» (авториз.польз.): test_navigation_via_constructor_personal_account

Переход по клику на логотип Stellar Burgers (авториз. польз.): test_navigation_via_logo_personal_account

# Выход из аккаунта - test_logout.py
Выход по кнопке «Выйти» в личном кабинете: test_personal_account_logout

# Раздел «Конструктор» - test_constructor_navigation.py
Переход к разделу «Булки»: test_switch_to_buns_section

Переход к разделу «Соусы»: test_switch_to_sauces_section

Переход к разделу «Начинки»: test_switch_to_fillings_section