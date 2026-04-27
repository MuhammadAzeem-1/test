from odoo import models, fields, api


class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    line_weight = fields.Float(
        string='Line Weight (kg)',
        compute='_compute_line_weight',
        store=True,
        digits=(16, 2),
        help='Total weight for this line (product weight × quantity)'
    )

    @api.depends('product_id', 'product_uom_qty', 'product_id.weight')
    def _compute_line_weight(self):
        """Calculate weight for individual order line."""
        for line in self:
            if line.product_id and line.product_id.weight:
                line.line_weight = line.product_id.weight * line.product_uom_qty
            else:
                line.line_weight = 0.0