from odoo.tests.common import TransactionCase

# Exercise 01
# 
# Statement -
#   Write two tests on a product:
#     1. Verify that when you create a product with listing price, the field is
#        stored correctly.
#     2. Verify that when you add some tag on a product, the tag is correctly
#        linked.
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


class TestProductBasics(TransactionCase):

    def test_product_price(self):
        product = self.env['product.product'].create({
            'name': 'Test Product',
            'lst_price': 99.0,
        })
        self.assertEqual(product.list_price, 99.0)

    def test_product_category(self):
        product_tag = self.env['product.tag'].create({'name': 'my-tag'})
        product = self.env['product.product'].create({
            'name': 'Test Product',
            'lst_price': 99.0,
            'all_product_tag_ids': [product_tag.id]
        })
        self.assertEqual(self.product.all_product_tag_ids.name, 'my-tag')
