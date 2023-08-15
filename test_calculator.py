import unittest

import calculator


class TestCalculator(unittest.TestCase):
    def test_calculate_payments(self):
        p1 = 2000
        m1 = [[5000, 0.06], [10000, 0.05], [8000, 0.07]]
        e1 = [0, 668.63, 1331.37]
        r1 = calculator.calculate_payments(p1, m1)
        self.assertEqual(len(e1), len(r1))
        for rv, ev in zip(r1, e1):
            self.assertAlmostEqual(rv, ev)
        self.assertAlmostEqual(
            sum(e1), p1
        )  # Verify expected allocations aligns with the payment
        self.assertAlmostEqual(sum(r1), p1)

        # More cases here
