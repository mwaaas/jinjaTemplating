from jinja2 import Template, Environment
from time import perf_counter as pc
import argparse
from datetime import datetime, timedelta

JOURNEY_A, JOURNEY_B = "Journey A", "Journey B"
FILTERS = {}


def custom_expression(customer):
    if customer.msisdn == "0722659526":
        return "journeyB"
    else:
        return "journeyA"


FILTERS['custom_expression'] = custom_expression


# initialize jinja2 environment
env = Environment(keep_trailing_newline=True)
env.filters.update(FILTERS)


class Customer(object):
    def __init__(self, id, name, msisdn, accountNumber, riskband):
        self.id = id
        self.name = name
        self.msisdn = msisdn
        self.accountNumber = accountNumber
        self.riskband = riskband


class Loan(object):
    def __init__(self, id, customerId, amount, dueDate, interest_rate):
        self.id = id
        self.customerId = customerId
        self.amount = amount
        self.dueDate = dueDate
        self.interest_rate = interest_rate


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
        interest_rate=5
    )
]


def expression_one(customer):
    """
    if customer.riskband > 4 assign JOURNEY_A else assign JOURNEY_B
    """
    expression = "{% if customer.riskband==4 %}{{JOURNEY_A}}{% else %}{{JOURNEY_B}}{% endif %}"
    t = env.from_string(expression)
    return t.render(dict(
        customer=customer,
        JOURNEY_A=JOURNEY_A,
        JOURNEY_B=JOURNEY_B
    ))


def expression_two(customer, loan):
    target_date = datetime.today() + timedelta(days=30)
    expr = "{% if loan.dueDate >= target_date and loan.amount < 1000 and loan.interest_rate > 5 %}" \
           "{{JOURNEY_B}}{% elif customer.name == name and customer.msisdn == msisdn %}" \
           "{{JOURNEY_A}}" \
           "{% else %}DEFAULT{% endif %}"
    template = env.from_string(expr)
    return template.render(
        target_date=target_date,
        customer=customer,
        loan=loan,
        JOURNEY_A=JOURNEY_A,
        JOURNEY_B=JOURNEY_B,
        name="John",
        msisdn="254722123456"
    )


def expression_three(customer):
    """
    Using custom expressions
    If customer.msisdn = “0722659526” assign journeyB else journeyC
    :param Customer:
    :return:
    """
    expression = "{{customer|custom_expression}}"

    template = env.from_string(expression)
    return template.render(dict(customer=customer))


def expression_four(customer):
    """
    Just like expression three but using function instead of filters
    Using custom functions
    :param customer:
    :return:
    """
    expression = "{{custom_function(customer)}}"

    template = env.from_string(expression)
    return template.render(dict(customer=customer, custom_function=custom_expression))


def timed(fun, *args):
    test_num = []
    for i in range(1000):
        t0 = pc()
        r = fun(*args)
        time_taken = (pc() - t0) * 1000
        test_num.append(time_taken)

    avarage_time_taken = sum(test_num)/len(test_num)
    print('{} execution took {} miliseconds.'.format(fun.__name__, avarage_time_taken))
    return avarage_time_taken


def expression_four_benchmark():
    return timed(
        expression_four,
        Customer(
            id="12132323",
            name="testing_journey_one",
            msisdn="0722659526",
            accountNumber="10000",
            riskband="6"
        )
    )


def expression_three_benchmark():
    return timed(
        expression_three,
        Customer(
            id="12132323",
            name="testing_journey_one",
            msisdn="0722659526",
            accountNumber="10000",
            riskband="6"
        )
    )


def expression_two_benchmark():
    return timed(
        expression_two,
        Customer(
            id="12132323",
            name="testing_journey_one",
            msisdn="0722659526",
            accountNumber="10000",
            riskband="6"
        ),
        Loan(
            id="23048w904523",
            customerId='daou2ojwfef',
            amount=900,
            dueDate=datetime.now() + timedelta(days=31),
            interest=6
        )
    )


def expression_one_benchmark():
    return timed(
        expression_one,
        Customer(
            id=5678,
            name='Jane',
            msisdn='300',
            accountNumber='uvw',
            riskband=3
        )
    )


if __name__ == "__main__":
    parser = argparse.ArgumentParser("expression_function")
    parser.add_argument('expression', type=str)

    args = parser.parse_args()
    globals()['expression_%s_benchmark'% args.expression]()