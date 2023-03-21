from typing import List


class Account:
    def __init__(self, owner: str, amount: int = 0):
        self.owner = owner
        self.amount = amount
        self._transactions: List[int] = []

    @property   # getter
    def balance(self) -> int:
        return self.amount + sum(self._transactions)

    def handle_transaction(self, transaction_amount: int) -> [Exception, str]:
        balance = self.balance
        if balance + transaction_amount < 0:
            raise ValueError("sorry cannot go in debt!")
        else:
            self._transactions.append(transaction_amount)
            account_balance = self.balance
            return f"New balance: {account_balance}"

    def add_transaction(self, amount: int) -> [Exception, str]:
        if not isinstance(amount, int):
            raise ValueError("please use int for amount")
        else:
            add_transaction = self.handle_transaction(amount)
            return add_transaction

    def __str__(self) -> str:   # print an instance
        owner = self.owner
        amount = self.amount
        return f"Account of {owner} with starting amount: {amount}"

    def __repr__(self) -> str:   # print a representational string of an instance
        owner = self.owner
        amount = self.amount
        return f"Account({owner}, {amount})"

    def __len__(self) -> int:
        total_number_of_transactions = len(self._transactions)   # self._transactions.__len__()
        return total_number_of_transactions

    def __getitem__(self, item) -> int:
        index = item
        transaction = self._transactions[index]   # self._transactions.__getitem__(item)
        return transaction

    def __reversed__(self) -> reversed:
        reversed_order_of_transactions = reversed(self._transactions)   # self._transactions.__reversed__()
        return reversed_order_of_transactions

    def __gt__(self, other) -> bool:   # >
        return self.balance > other.balance

    # def __lt__(self, other) -> bool:
    #     return self.balance < other.balance

    def __ge__(self, other) -> bool:   # >=
        return self.balance >= other.balance

    # def __le__(self, other) -> bool:
    #     return self.balance <= other.balance

    def __eq__(self, other) -> bool:   # ==
        return self.balance == other.balance

    # def __ne__(self, other) -> bool:
    #     return self.balance != other.balance

    def __add__(self, other) -> object:
        first_owner = self.owner
        second_owner = other.owner
        owner = f"{first_owner}&{second_owner}"
        amount = self.amount + other.amount
        new_account = Account(owner, amount)
        new_account_transactions = self._transactions + other._transactions
        new_account._transactions = new_account_transactions
        return new_account
