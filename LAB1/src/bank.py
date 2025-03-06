class InsufficientFundsError(Exception):
    pass

class BankAccount:
    def __init__(self, initial_balance=0.0):
        if initial_balance < 0:
            raise ValueError("Początkowy stan konta nie może być ujemny.")
        self._balance = initial_balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Kwota wpłaty musi być większa niż zero.")
        self._balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Kwota wypłaty musi być większa niż zero.")
        if amount > self._balance:
            raise InsufficientFundsError("Niewystarczające środki na koncie.")
        self._balance -= amount

    def get_balance(self):
        return self._balance