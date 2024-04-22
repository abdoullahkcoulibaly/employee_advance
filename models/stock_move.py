from odoo import _, api, Command, fields, models


class StockMove(models.Model):
    _inherit = "stock.move"

    standard_price = fields.Float('Coût', related='product_id.standard_price', digits='Product Price', readonly=False)
