class UserAccount:
    def __init__(self, username, password):
        self.username = username
        self.__password = password

    def set_password(self, new_password):
        self.__password = new_password

    def check_password(self, password):
        return self.__password == password


if __name__ == '__main__':
    account = UserAccount('MyCoolUsername', '<PASSWORD>')
    print(account.username)
    print(account.check_password('<PASSWORD>'))

    account.set_password('<NEW_PASSWORD>')
    print(account.check_password('<PASSWORD>'))
    print(account.check_password('<NEW_PASSWORD>'))
