class PersonAccount:
    def __init__(self, first_name: str, last_name: str):
        self.first_name = first_name
        self.last_name = last_name
        self._incomes = 0
        self._expenses = 0

    @property
    def total_income(self) -> int:
        return self._incomes

    @property
    def total_expense(self) -> int:
        return self._expenses

    def account_info(self) -> str:
        return f"Account of {self.first_name} {self.last_name} has {self._incomes} for income and {self._expenses} for expense."

    def add_income(self, amount: int):
        if amount > 0:
            self._incomes += amount
        else:
            print("Income amount should be positive.")

    def add_expense(self, amount: int):
        if amount > 0:
            self._expenses += amount
        else:
            print("Expense amount should be positive.")

    def account_balance(self) -> int:
        return self._incomes - self._expenses

def main():
    p1 = PersonAccount('Handy', 'Ambarita')
    p1.add_income(1000)
    p1.add_expense(400)
    print(p1.account_info())

    p1.add_expense(200)
    print(f"The balance is {p1.account_balance()}")

    p1.add_income(2000)
    print(p1.account_info())
    print(f"The balance is {p1.account_balance()}")

    print(f"Total expense: {p1.total_expense}")
    print(f"Total income: {p1.total_income}")

if __name__ == "__main__":
    main()
