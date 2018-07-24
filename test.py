from unittest import TestCase
from sample import \
    expression_three, expression_four, Customer


class TestingExpressions(TestCase):

    def test_expression_three(self):
        journey = expression_three(
            Customer(
                id="12132323",
                name="testing_journey_one",
                msisdn="0722659526",
                accountNumber="10000",
                riskband="6"
            )
        )

        self.assertEqual(journey, "journeyB")

        journey = expression_three(
            Customer(
                id="12132323",
                name="testing_journey_one",
                msisdn="07092839238",
                accountNumber="10000",
                riskband="6"
            )
        )

        self.assertEqual(journey, "journeyA")


    def test_expression_four(self):
        journey = expression_four(
            Customer(
                id="12132323",
                name="testing_journey_one",
                msisdn="0722659526",
                accountNumber="10000",
                riskband="6"
            )
        )

        self.assertEqual(journey, "journeyB")

        journey = expression_four(
            Customer(
                id="12132323",
                name="testing_journey_one",
                msisdn="07092839238",
                accountNumber="10000",
                riskband="6"
            )
        )

        self.assertEqual(journey, "journeyA")

