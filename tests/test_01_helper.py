from odoo.tests.common import TransactionCase
from odoo.tests import tagged

@tagged('aans')
class TestClass(TransactionCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        print("========== setup class ==========")

    @classmethod
    def tearDownClass(cls):
        super().tearDownClass()
        print("========== teardown class ==========")

    def setUp(self):
        print("------------ setup test ------------")

    def tearDown(self):
        print("------------ teardown test ------------")

    def test_case(self):
        self.assertEqual(1, 1)

    def test_case_2(self):
        self.assertEqual(1, 1)