# -*- coding: utf-8 -*-

{
    'name': 'Personal Expense',
    'summary': 'Track your money flow',
    'description': """
        Help you to track money flow
    """,
    'version': '0.0',
    'category': 'Accounting',
    'images': [

    ],
    'author': 'Mehedi',
    'support': 'mehedi360272@gmail.com',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/menus.xml',
        'views/money_flow_views.xml',
        'views/income.xml',
        'views/expense.xml',
        'report/money_flow_report.xml',
        'views/dashboard.xml',
        ],

    'installable': True,
    'application': True,
    'assets': {
        
    },
    'license': 'LGPL-3',
    'price': -9,
    'currency': 'USD',
}
