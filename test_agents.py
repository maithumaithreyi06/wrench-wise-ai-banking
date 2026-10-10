
# test_agents.py
import unittest

from agents import (
    banking_agent,
    fraud_agent,
    loan_agent,
    supervisor_agent,
)


class TestBankingAgents(unittest.TestCase):

    def test_balance(self):
        result = banking_agent("What is my balance?")
        self.assertIn("25,000", result)

    def test_transaction_history(self):
        result = banking_agent("Show transaction history")
        self.assertIn("TXN001", result)

    def test_fraud_agent(self):
        result = fraud_agent("Check suspicious transactions")
        self.assertIn("TXN003", result)

    def test_loan_agent(self):
        result = loan_agent("Check loan", income=30000)
        self.assertIn("meet", result)

    def test_supervisor_routing(self):
        result = supervisor_agent("Check fraud")
        self.assertEqual(result["agent"], "Risk / Fraud Agent")

    def test_help_agent(self):
        result = supervisor_agent("Hello")
        self.assertEqual(result["agent"], "Banking Help Agent")


if __name__ == "__main__":
    unittest.main()
