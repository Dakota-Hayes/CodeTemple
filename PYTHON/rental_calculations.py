class RentalCalculation():
    def __init___(self):
        self.rent = 0.00
        self.units = 0.00
        self.income = 0.00
        self.tax = 0.00
        self.insurance = 0.00
        self.utilities = 0.00
        self.hoa = 0.00
        self.landscaping = 0.00
        self.vacancy_percent = 0.00
        self.vacancy = 0.00
        self.repairs = 0.00
        self.capex = 0.00
        self.property_management = 0.00
        self.property_management_percent = 0.00
        self.mortgage = 0.00
        self.expenses = 0.00
        self.cash_flow = 0.00
        self.annual_cash_flow = 0.00
        self.down_payment = 0.00
        self.closing_costs = 0.00
        self.rehab_costs = 0.00
        self.misc_costs = 0.00
        self.total_costs = 0.00
        self.cash_return = 0.00
        self.return_score = ""
        pass
    def income_calculator(self):
        self.rent = float(input("What is the monthly rent?:"))
        self.units = float(input("How many units are available?:"))
        self.income = self.rent * self.units
        pass
    def expense_calculator(self):
        self.tax = float(input("What is the property tax?:"))
        self.insurance = float(input("What is the monthly insurance amount?:"))
        self.utilities = float(input("What are the monthly utility costs?:"))
        self.hoa = float(input("What is the monthly HOA cost?:"))
        self.landscaping = float(input("What are the monthly landscaping costs?:"))
        self.vacancy_percent = float(input("What is the vacancy percent?:"))
        self.vacancy = self.income * self.vacancy_percent
        self.repairs = float(input("What amount is set aside for repairs?:"))
        self.capex = float(input("What amount is set aside for capital expenses?:"))
        self.property_management_percent = float(input("What percent in decimal value is going to property management?:"))
        self.property_management = self.income * self.property_management_percent
        self.mortgage = float(input("What is the monthly mortgage?:"))
        self.expenses = self.tax + self.insurance + self.utilities + self.hoa + self.landscaping + self.vacancy + self.repairs + self.capex + self.property_management + self.mortgage
        pass
    def cash_flow_calculator(self):
        self.cash_flow = self.income - self.expenses
        self.annual_cash_flow = self.cash_flow * 12
        pass
    def initial_cost_calculator(self):
        self.down_payment = float(input("What was the initial down payment?:"))
        self.closing_costs = float(input("What was the closing cost?:"))
        self.rehab_costs = float(input("How much was put in for repairs?:"))
        self.misc_costs = float(input("Other costs?:")) 
        self.total_costs = self.down_payment + self.closing_costs + self.rehab_costs + self.misc_costs
        pass
    def cash_return_calculator(self):
        self.cash_return = self.annual_cash_flow / self.total_costs
        self.cash_return = self.cash_return * 100
        pass
    def return_score_calculator(self):
        if self.cash_return < 1:
            self.return_score = "poor"
        elif self.cash_return < 3:
            self.return_score = "okay"
        elif self.cash_return < 5:
            self.return_score = "average"
        elif self.cash_return < 7:
            self.return_score = "good"
        else:
            self.return_score = "great"
        pass
    def print_all(self):
        print(self.rent,"rent")
        print(self.units,"units")
        print(self.income,"income")
        print(self.tax,"tax")
        print(self.insurance,"insurance")
        print(self.utilities,"utilities")
        print(self.hoa,"hoa")
        print(self.landscaping,"landscaping")
        print(self.vacancy_percent,"vacancy percent")
        print(self.vacancy,"vacancy")
        print(self.repairs,"repairs")
        print(self.capex,"capex")
        print(self.property_management,"property management")
        print(self.property_management_percent,"property management percent")
        print(self.mortgage,"mortgage")
        print(self.expenses,"expenses")
        print(self.cash_flow,"cash flow")
        print(self.annual_cash_flow,"annual cash flow")
        print(self.down_payment,"down payment")
        print(self.closing_costs,"closing costs")
        print(self.rehab_costs,"rehab costs")
        print(self.misc_costs,"misc costs")
        print(self.total_costs,"total costs")
        print(self.cash_return,"cash return")
        print(self.return_score,"return score")
        pass
    def run_calculations(self):
        self.income_calculator()
        self.expense_calculator()
        self.cash_flow_calculator()
        self.initial_cost_calculator()
        self.cash_return_calculator()
        self.return_score_calculator()
        self.print_all()
        pass

rental_calculation_1 = RentalCalculation()
rental_calculation_1.run_calculations()
