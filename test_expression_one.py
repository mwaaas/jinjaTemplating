import time
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
        start_time = time.time()
        result = expression_one(self.customers[0])
        work_latency = (time.time() - start_time) * 1000

        print("Expression evaluated in {work_latency} ms".format(work_latency=work_latency))

        self.assertEqual(result, JOURNEY_A)

    def test_riskband_not_4(self):
        start_time = time.time()
        result = expression_one(self.customers[1])
        work_latency = (time.time() - start_time) * 1000

        print("Expression evaluated in {work_latency} ms".format(work_latency=work_latency))

        self.assertEqual(result, JOURNEY_B)
