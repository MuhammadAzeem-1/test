from odoo import models, fields, api


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    priority = fields.Selection(
        selection=[
            ('low', 'Low'),
            ('medium', 'Medium'),
            ('high', 'High'),
        ],
        string='Priority',
        default='medium',
        required=True,
        tracking=True,
        help='Priority level for this sale order',
    )

    @api.onchange('priority')
    def _onchange_priority(self):
        """Optional: Add notification when priority changes to high"""
        if self.priority == 'high':
            return {
                'warning': {
                    'title': 'High Priority Order',
                    'message': 'This order has been marked as high priority and requires immediate attention.',
                }
            }