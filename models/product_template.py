from odoo import models, fields


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    # Ensure weight field exists and is visible
    # (Odoo already has this field, but we make it more prominent)
    weight = fields.Float(
        string='Weight (kg)',
        digits='Stock Weight',
        help='Weight of the product in kilograms. Used for shipping calculations.',
    )