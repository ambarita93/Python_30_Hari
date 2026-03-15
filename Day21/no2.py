class PersonAccount:
    def __init__(self, first_name, last_name,incomes, expenses):
        self.first_name = first_name
        self.last_name = last_name
        self.incomes = incomes
        self.expenses = expenses

    def total_income(self):
        return self.incomes
    
    def total_expense(self):
        return self.expenses
    
    def account_info(self):
        print(f"Account of {self.first_name} {self.last_name} has {self.incomes} for income and {self.expenses} for expense.")

    def add_income(self,incomes):
        self.incomes = self.incomes + incomes
        

    def add_expense(self,expenses):
        self.expenses = self.expenses + expenses
    
    def account_balance(self):
        print(f"The balance is {self.incomes-self.expenses}")
    
p1 = PersonAccount('Handy','Ambarita',1000,400)
p1.account_info()
p1.add_expense(200)
p1.account_balance()
p1.add_income(2000)
p1.account_info()
p1.account_balance()
print(p1.total_expense())
print(p1.total_income())