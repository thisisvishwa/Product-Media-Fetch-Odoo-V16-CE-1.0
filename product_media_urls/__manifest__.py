{
    'name': "Product Media via URL's",
    'version': '1.0',
    'author': "Vishwa G",
    'website': "https://thisis.com",
    'category': 'Website',
    'license': 'AGPL-3',
    'summary': 'Fetch and display product media from external URLs in Odoo 16 Community Edition',
    'description': """
Product Media via URL's Module
==============================
This module allows dynamic fetching of product images and additional media from external URLs and displays them on the website without storing them in the Odoo database.
    """,
    'depends': ['base', 'website_sale'],
    'data': [
        'security/ir.model.access.csv',
        'views/product_template_views.xml',
        'views/assets.xml',
        'data/ir_cron_data.xml',
    ],
    'demo': [
        'demo/product_demo.xml',
    ],
    'qweb': [
        'static/src/xml/product_media_template.xml',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
}