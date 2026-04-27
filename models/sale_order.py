from odoo import models, fields, api
import logging

_logger = logging.getLogger(__name__)


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    total_weight = fields.Float(
        string='Total Weight (kg)',
        compute='_compute_total_weight',
        store=True,
        digits=(16, 2),
        help='Total weight of all order lines in kilograms'
    )
    
    is_heavy_order = fields.Boolean(
        string='Heavy Order',
        compute='_compute_is_heavy_order',
        store=True,
        help='Automatically set to True if total weight exceeds 100 kg'
    )

    @api.depends('order_line.product_id', 'order_line.product_uom_qty', 'order_line.product_id.weight')
    def _compute_total_weight(self):
        """
        Compute total weight based on product weight * quantity for each line.
        Recalculates whenever order lines, products, or quantities change.
        """
        for order in self:
            total = 0.0
            for line in order.order_line:
                if line.product_id and line.product_id.weight:
                    # Weight is stored per unit, multiply by quantity
                    total += line.product_id.weight * line.product_uom_qty
            
            order.total_weight = total
            
            # Log significant weight changes
            if total > 100:
                _logger.info(
                    f"Sale Order {order.name} has heavy weight: {total:.2f} kg "
                    f"(Customer: {order.partner_id.name})"
                )

    @api.depends('total_weight')
    def _compute_is_heavy_order(self):
        """Mark orders as heavy if they exceed 100 kg threshold."""
        for order in self:
            order.is_heavy_order = order.total_weight > 100.0

    @api.model
    def cron_log_heavy_orders(self):
        """
        Scheduled cron job that runs daily to log all heavy orders.
        Finds orders exceeding 100 kg and logs them for monitoring.
        """
        heavy_orders = self.search([
            ('is_heavy_order', '=', True),
            ('state', 'in', ['draft', 'sent', 'sale'])
        ])
        
        if heavy_orders:
            _logger.warning(
                f"=== DAILY HEAVY ORDERS REPORT ==="
            )
            _logger.warning(
                f"Found {len(heavy_orders)} heavy orders (>100 kg) requiring attention:"
            )
            
            for order in heavy_orders:
                _logger.warning(
                    f"  • Order: {order.name} | "
                    f"Customer: {order.partner_id.name} | "
                    f"Weight: {order.total_weight:.2f} kg | "
                    f"State: {order.state} | "
                    f"Total: {order.amount_total:.2f} {order.currency_id.name}"
                )
            
            _logger.warning(
                f"=== END HEAVY ORDERS REPORT ==="
            )
        else:
            _logger.info("Daily heavy orders check: No heavy orders found.")
        
        return True