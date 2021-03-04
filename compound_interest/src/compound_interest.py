class CompoundInterest:
    def __init__(self, amount, rate, number_of_years):
        self.amount = amount
        self.rate = rate / 100.00
        self.number_of_years = number_of_years
        self.times_compounded = 12

    def calculate_final_investment(self):
        return round(self.amount(1 + (self.rate/self.times_compounded)) ** (self.times_compounded * self.number_of_years), 2)