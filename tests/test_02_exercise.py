from odoo.tests.common import TransactionCase
from odoo.exceptions import UserError

# Exercise 02
#
# Statement -
#   Write two tests for invoice validation:
#     1. Write a test to ensure posting an invoice (`account.move`) with an
#        invoice line (`invoice_line_ids`) changes it's state to "posted".
#     2. Write another test to ensure that we can't post an invoice
#        (`account.move`) without any invoice line (`invoice.line.ids`).
#   After running both tests, manually confirm whether the invoice
#   (`account.move`) data you just created in your tests exists in database.
#
# Helpers -
#   To create invoice, products, partner, you can use:
#     ```
#     # To create a partner
#     partner = self.env['res.partner'].create({'name': 'John Doe'})
#
#     # To create a product
#     product = self.env['product.product'].create({'name': 'Workshop Product'})
#
#     # To create an invoice with invoice lines
#     invoice = self.env['account.move'].create({
#          'move_type': 'out_invoice',
#          'partner_id': partner.id,
#          'invoice_line_ids': [(0, 0, {
#               'product_id': product.id,
#               'quantity': 1,
#               'price_unit': 50,
#           })]
#      })
#
#     # To post an invoice
#     invoice.action_post()
#     ```
#
# Facilitator Notes - 
#   Objective of this exercise:
#    - Testing expected errors
#    - Letting attendees explore what can be improved in this solution.
#      (Check ./test_02_helper.py for an improved solution)
#    - Let attendees explore why the data they create in test do not show up in
#      real database. (Explain TransactionCase here and how it's created.)
#    - Explain about other test classes and how and when they should create
#      their own test class.
#
  


class TestInvoicePostAction(TransactionCase):

    def test_post_invoice_with_line(self):
        partner = self.env['res.partner'].create({'name': 'partner_a'})
        product = self.env['product.product'].create({'name': 'Workshop Product'})
        invoice = self.env['account.move'].create({
            'move_type': 'out_invoice',
            'partner_id': partner.id,
            'invoice_line_ids': [(0, 0, {
                'product_id': product.id,
                'quantity': 1,
                'price_unit': 50,
            })]
        })
        invoice.action_post()
        self.assertEqual(invoice.state, 'posted')

    def test_post_invoice_without_lines(self):
        partner = self.env['res.partner'].create({'name': 'partner_a'})
        invoice = self.env['account.move'].create({
            'move_type': 'out_invoice',
            'partner_id': partner.id,
        })

        with self.assertRaises(UserError):
            invoice.action_post()
