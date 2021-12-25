from _typeshed import Self
import datetime

class debts:
    def __init__(self, date, payable, amount, name, description, paid):
        self.date = datetime.datetime.now()
        self.payable = payable
        self.amount = amount
        self.name = name
        self.description = description
        self.paid = paid


debt1 = debts()
new_date = datetime.datetime(2022, 10, 30)
debt1.changeDate(new_date)
print( debt1.date.strftime("%x"))
