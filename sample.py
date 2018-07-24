from jinja2 import Template
from datetime import datetime, timedelta

customer = [
    dict(
        id="23345363",
        name="jinja",
        msisdn="254702729654",
        accountNumber="o2q98382483",
        riskband=6
    ),
]

loan = [
    dict(
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