from unittest import TestCase
from sample import expression_one, Customer, JOURNEY_A, JOURNEY_B


class TestingExpressionOne(TestCase):
    def setUp(self):
        self.customers = [
            Customer(
                id=1234,
                name='John',
                msisdn='200',
                accountNumber='xyz',
                riskband=4
            ),
            Customer(
                id=5678,
                name='Jane',
                msisdn='300',
                accountNumber='uvw',
                riskband=3
            )
        ]

    def test_riskband_4(self):
        self.assertEqual(expression_one(self.customers[0]), JOURNEY_A)

    def test_riskband_not_4(self):
        self.assertEqual(expression_one(self.customers[1]), JOURNEY_B)
