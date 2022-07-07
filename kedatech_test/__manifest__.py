# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name' : 'KeDaTech Material',
    'version' : '1.1',
    'summary': 'Provide Clients Material Catalog',
    'description': """
Provide Clients Material Catalog
    """,
    'category': 'Catalog',
    'website': 'alfredolubis5@gmail.com',
    'images' : [],
    'depends' : [],
    'data': [
        'security/kedatech_security.xml',
        'security/ir.model.access.csv',
        'views/base_menu_views.xml',
        'views/material_views.xml',
        'views/client_views.xml',
        'views/supplier_views.xml',
    ],
    'demo': [
    ],
    'qweb': [
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
}
