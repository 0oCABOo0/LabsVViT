class UserAccount:
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.__password = password

    def set_password(self, new_password):
        self.__password = new_password

    def check_password(self, password):
        return self.__password == password

user_account = UserAccount("Alex", "Alex@gmall.com", "123")

print("Проверка пароля:", user_account.check_password("123"))

user_account.set_password("456")

print("Проверка нового пароля:", user_account.check_password("456"))

print("Проверка старого пароля:", user_account.check_password("123"))