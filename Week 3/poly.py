class Transaction:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance

    def process(self):
        pass


class Deposit(Transaction):
    def process(self, amount):
        self.balance += amount

        print(f"The amount ({amount}) was deposited.")


class Withdrawal(Transaction):
    def process(self, amount):
        if amount > self.balance:
            print(f"Withdrawal failed. Insufiicient funds")
        else:
            self.balance -= amount
            print(f"The amount ({amount}) was withdrawn")


class Transfer(Transaction):
    target_account_balance = 0

    def process(self, amount, target_account):
        if amount > self.balance:
            print(f"Insufficient funds for {self.account_holder} to send {amount}.")
        else:
            self.balance -= amount
            target_account.balance += amount
            print(
                f"{self.account_holder} transferred {amount} to {target_account.account_holder}."
            )
            print(
                f"Transferer Balance: {self.balance} | Target Balance: {target_account.balance}"
            )


person1 = Transaction("Tyra", 20000)
person2 = Transaction("Biggs", 10000)

deposit = Deposit(person1.account_holder, person1.balance)

deposit.balance = person1.balance
deposit.process(3000)
person1.balance = deposit.balance
print(person1.balance)


transfer = Transfer(person1.account_holder, person1.balance)
transfer.balance = person1.balance
transfer.process(4000, target_account=person2)
person2.balance = transfer.target_account.balance
