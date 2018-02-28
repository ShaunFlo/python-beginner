class emp:

    raise_amount = 1.05
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def raise1(self):
        self.pay = self.pay * self.raise_amount

# args
emp1 = emp('Shaun', 'Flores', 4000)
print(emp1.fullname())
print("before raise: %s "% emp1.pay)
emp1.raise1()
print("after raise: %s" % emp1.pay)
print("the raise was: %s percent"  % emp.raise_amount)
