import time
from unittest import TestCase
from sample import expression_two, Customer, Loan, JOURNEY_A, JOURNEY_B
from datetime import datetime, timedelta


class TestingExpressionOne(TestCase):
    def setUp(self):
        self.customers = [
            Customer(
                id=1234,
                name='Jane',
                msisdn='254722123457',
                accountNumber='xyz',
                riskband=4
            ),
            Customer(
                id=5678,
                name='John',
                msisdn='254722123456',
                accountNumber='uvw',
                riskband=3
            )
        ]

        self.loans = [
            Loan(
                id="23048w904523",
                customerId='daou2ojwfef',
                amount=900,
                dueDate=datetime.now() + timedelta(days=31),
                interest_rate=6
            ),
            Loan(
                id="23048w904523",
                customerId='baox2ojwfeg',
                amount=3000,
                dueDate=datetime.now() + timedelta(days=21),
                interest_rate=4
            )
        ]

    def test_journey_a(self):
        start_time = time.time()
        result = expression_two(self.customers[0], self.loans[0])
        work_latency = (time.time() - start_time) * 1000

        print("Expression evaluated in {work_latency} ms".format(work_latency=work_latency))

        self.assertEqual(JOURNEY_B, result)

    def test_journey_b(self):
        start_time = time.time()
        result = expression_two(self.customers[1], self.loans[1])
        work_latency = (time.time() - start_time) * 1000

        print("Expression evaluated in {work_latency} ms".format(work_latency=work_latency))

        self.assertEqual(JOURNEY_A, result)
