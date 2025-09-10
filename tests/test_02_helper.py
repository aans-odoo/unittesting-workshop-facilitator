from odoo.tests.common import TransactionCase
from odoo.exceptions import UserError  
from odoo.fields import Command

class TestInvoicePostAction(TransactionCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        partner = cls.env['res.partner'].create({'name': 'partner_a'})
        cls.invoice = cls.env['account.move'].create({
            'move_type': 'out_invoice',
            'partner_id': partner.id,
        })

    def test_post_invoice_without_lines_improved(self):
        with self.assertRaises(UserError):
            self.invoice.action_post()

    def test_post_invoice_with_line_improved(self):
        self.invoice.update({
            'invoice_line_ids': [Command.create({
                'product_id': self.env['product.product'].create({'name': 'Workshop Product'}).id,
                'quantity': 1,
                'price_unit': 50,
            })]
        })
        self.invoice.action_post()
        self.assertEqual(self.invoice.state, 'posted')
