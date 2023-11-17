# -*- coding: utf-8 -*-
{
    'name': "Esi Lecture",

    'summary': """
        CRUD Book Management Module""",

    'description': """     
         The "Book Management" module in Odoo streamlines efficient book management. It simplifies tracking, adding, deleting, and modifying book information. The module also includes advanced features for exploring authors and assessing book popularity through a liking system.
    """,

    'author': "Cameron et Mamoun",
    'website': "/www.he2b.be",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Tools',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'application': True,
}
