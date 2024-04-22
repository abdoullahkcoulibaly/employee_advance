# -*- coding: utf-8 -*-
{
    'name': "Avance employé",
    'version': '1.0',
    'author': "Abdoulaye Coulibaly",
    'maintainer': "Christopher DATO",
    'category': 'Uncategorized',
    'summary': 'Gedispa access rights',
    'description': """
        This module contains employee avance.
    """,
    'depends': ['base','stock','hr_payroll','gedispa_access_rights'],
    'data': [
        'views/stock_picking.xml',
    ],
    'installable': True,
    'license': 'LGPL-3',
}