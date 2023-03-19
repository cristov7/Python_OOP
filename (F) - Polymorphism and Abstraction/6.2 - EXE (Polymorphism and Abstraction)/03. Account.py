from typing import List


class Account:
    def __init__(self, owner: str, amount: int = 0):
        self.owner = owner
        self.amount = amount
        self._transactions: List[int] = []

    @property   # getter
    def balance(self):
        return self.amount + sum(self._transactions)

    def handle_transaction(self, transaction_amount: int) -> [Exception, str]:
        if self.balance + transaction_amount < 0:
            raise ValueError("sorry cannot go in debt!")
        else:
            self._transactions.append(transaction_amount)
            account_balance = self.balance
            return f"New balance: {account_balance}"

    def add_transaction(self, amount: int) -> [Exception, str]:
        if not isinstance(amount, int):
            raise ValueError("please use int for amount")
        else:
            return self.handle_transaction(amount)

    def __str__(self) -> str:   # print
        owner = self.owner
        amount = self.amount
        return f"Account of {owner} with starting amount: {amount}"

    def __repr__(self) -> str:   # representational string
        owner = self.owner
        amount = self.amount
        return f"Account({owner}, {amount})"

    def __len__(self) -> int:
        return len(self._transactions)

    def __getitem__(self, index) -> int:   # iterate over and receive each transaction
        return self._transactions[index]

    def __reversed__(self):   # reverse the order of transactions
        return reversed(self._transactions)

    def __gt__(self, other) -> bool:   # >
        return self.balance > other.balance

    def __ge__(self, other) -> bool:   # >=
        return self.balance >= other.balance

    def __eq__(self, other) -> bool:   # ==
        return self.balance == other.balance

    # def __lt__(self, other) -> bool:
    #     return self.balance < other.balance

    # def __le__(self, other) -> bool:
    #     return self.balance <= other.balance

    # def __ne__(self, other) -> bool:
    #     return self.balance != other.balance

    def __add__(self, other) -> object:
        owner = f"{self.owner}&{other.owner}"
        amount = self.amount + other.amount
        new_account = Account(owner, amount)
        new_account._transactions = self._transactions + other._transactions
        return new_account
