from jinja2 import Template
from datetime import datetime, timedelta


class Customer(object):
    def __init__(self, id, name, msisdn, accountNumber, riskband):
        self.id = id
        self.name = name
        self.msisdn = msisdn
        self.accountNumber = accountNumber
        self.riskband = riskband

class Loan(object):
    def __init__(self, id, customerId, amount, dueDate, interest):
        self.id = id
        self.customerId = customerId
        self.amount = amount
        self.dueDate = dueDate
        self.interest = interest

customer = [
    Customer(
        id="23345363",
        name="jinja",
        msisdn="254702729654",
        accountNumber="o2q98382483",
        riskband=6
    ),
]

loan = [
    Loan(
        id="23048w904523",
        customerId='daou2ojwfef',
        amount="4000",
        dueDate=datetime.now() + timedelta(hours=6),
        interest="5%"
    )
]

def expression_one():
    pass


def expression_two():
    pass

def expression_three():
    pass