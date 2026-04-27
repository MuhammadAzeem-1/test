{
    'name': 'Sale Order Priority Management',
    'version': '17.0.1.0.0',
    'category': 'Sales',
    'summary': 'Add priority field to sale orders with manager-only edit access',
    'description': """
        This module adds a priority selection field to sale orders with three levels:
        - Low
        - Medium
        - High
        
        Features:
        - Priority field visible in form view below customer field
        - High priority filter in list view
        - Field editable only by Sales Managers
        - All other users can view but not edit
    """,
    'author': 'Muhammad Azeem',
    'website': 'https://github.com/mazeem182000',
    'depends': ['sale', 'sales_team'],
    'data': [
        'security/sale_order_priority_security.xml',
        'security/ir.model.access.csv',
        'views/sale_order_views.xml',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
    'license': 'LGPL-3',
}