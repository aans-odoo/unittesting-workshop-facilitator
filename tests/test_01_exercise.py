from odoo.tests.common import TransactionCase
from odoo.fields import Command

# Exercise 01
# 
# Statement -
#   Write two tests on a product:
#     1. Verify that when you set the product’s list price, the field is stored
#        correctly.
#     2. Verify that when you assign the tag to a product to a category, the tag
#        is correctly linked.
# 
# Helpers -
#   To create a product and tag you can use:
#     ```
#     product_tag = self.env['product.tag'].create({'name': 'Test Tag'})
#     product = self.env['product.product'].create({
#         'name': 'Test Product',
#         'lst_price': 99.0,
#         'all_product_tag_ids': [product_tag.id],
#     })
#     ```
# 
# Facilitator Notes - 
#   Objective of this exercise:
#   - Use lifecycle methods to perform common setup once (setUpClass) 
#     instead of repeating the same product creation logic in every test.
#     (Show different lifecycle methods from ./test_01_helper.py)
#
#   - Use Command helpers (Command.create, Command.update, Command.unlink) 
#     when working with x2many fields instead of writing IDs directly.
#     (List reasons why we have to use this)
# 

class TestProductBasics(TransactionCase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.product = cls.env['product.product'].create({
            'name': 'Test Product',
            'lst_price': 99.0,
        })

    def test_product_price(self):
        self.assertEqual(self.product.list_price, 99.0)

    def test_product_category(self):
        self.product.update({
            'all_product_tag_ids': [Command.create({'name': 'my-tag'})]
        })
        self.assertEqual(self.product.all_product_tag_ids.name, 'my-tag')
