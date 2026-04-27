{
    'name': 'Sale Order Total Weight',
    'version': '17.0.1.0.0',
    'category': 'Sales',
    'summary': 'Track total weight on sale orders with warnings and daily heavy order logging',
    'description': """
        This module adds comprehensive weight tracking to sale orders:
        
        Features:
        - Computed total_weight field based on order lines
        - Visual warning banner when weight exceeds 100 kg
        - Daily scheduled cron job to log heavy orders
        - Proper access control for weight-related operations
        - Automatic recalculation on order line changes
        
        The system automatically monitors order weights and provides
        visibility into heavy shipments requiring special handling.
    """,
    'author': 'Muhammad Azeem',
    'website': 'https://github.com/mazeem182000',
    'depends': ['sale', 'product'],
    'data': [
        'security/sale_order_weight_security.xml',
        'security/ir.model.access.csv',
        'views/sale_order_views.xml',
        'views/product_template_views.xml',
        'data/ir_cron_data.xml',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
    'license': 'LGPL-3',
}