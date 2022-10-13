class Account:
    def __init__(self, name: str, passport: str, phone_number: str, start_balance: int = 0):
        self.__name = name
        self.__passport = passport
        self.__phone_number = phone_number
        self.__balance = start_balance

    def full_info(self) -> str:
        return f'{self.__name} баланс: {self.__balance} руб. паспорт: {self.__passport} т.{self.__phone_number}'

    def __repr__(self) -> str:
        return f'{self.__name} баланс: {self.__balance} руб.'

    @property
    def balance(self) -> int:
        return f'{self.__balance} руб.'

    def deposit(self, amount: int) -> None:
        self.__balance += amount

    def withdraw(self, amount: int) -> None:
        """
        Снятие суммы с текущего счета
        :param amount: сумма
        """
        if self.__balance - amount < 0:
            raise ValueError('Недостаточно средств')
        else:
            self.__balance -= amount

    # TODO-1: напишите реализацию метода transfer()

    def transfer(self, target_account: 'Account', amount: int) -> None:
        """
        Перевод денег на счет другого клиента
        :param target_account: счет клиента для перевода
        :param amount: сумма перевода
        :return:
        """
        if self.__balance - amount < 0:
            raise ValueError('Недостаточно средств')
        self.__balance -= amount
        target_account.__balance += amount




account1 = Account("Иван", "3230 634563", "+7-900-765-12-34", 1000)
account2 = Account("Алексей", "+7-901-744-22-99", "3232 456124", 200)

print(account1)
print(account2)

# Переводим деньги с первого аккаунт на второй:
try:
    account1.transfer(account2, 500)
except ValueError as e:
    print(e)

# Проверяем изменения баланса:
print(account1)
print(account2)

# Переводим еще с первого аккаунт на второй:
try:
    account1.transfer(account2, 600)
except ValueError as e:
    print(e)

# Проверяем изменения баланса:
print(account1)
print(account2)
