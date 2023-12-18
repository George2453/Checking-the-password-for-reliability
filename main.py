while True:
    def check_password_strength(password):
        """Функция для проверки надежности пароля"""
        # Проверяем длину пароля
        if len(password) < 8:
            return "\nНенадёжный пароль \n\nПричина: пароль должен быть больше 8 символов ( password )  "
        # Проверяем наличие цифр
        if not any(char.isdigit() for char in password):
            return "\nНенадёжный пароль \n\nПричина: отсутствуют цифры ( 1,2,3,4,5,6,7,8,9,0 )"
        # Проверяем наличие букв в разных регистрах
        if not any(char.isupper() for char in password) or not any(char.islower() for char in password):
            return "\nНенадёжный пароль \n\nПричина: отсутствуют буквы в разных регистрах ( А б В г Д е Ж з И )"
        # Проверяем наличие специальных символов
        special_chars = "!@#$%^&*()-+/"
        if not any(char in special_chars for char in password):
            return "\nНенадёжный пароль \n\nПричина: отсутствуют специальные символы ( !@#$%^&*()-+/ )"
        # Если все проверки пройдены, то пароль считается надежным
        return "     Ваш пароль безопасен, шанс взлома минимальный!     "

    # Пример использования
    password = input("Введите пароль для проверки >>>: ")
    print(check_password_strength(password))
