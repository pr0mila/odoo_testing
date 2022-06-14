

# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name' : 'School Management',
    'version' : '1.0',
    'summary': 'School Management and Maintenance',
    'sequence': 10,
    'description': """
    School Management and Maintenance
    """,
    'category': 'Human Resources/Employees',
    'website': 'https://promila.info/',
    'images' : [],
    'depends' : ['hr'],
    'data': [
        'ir.model.access.csv',
        #'security.xml',
        'student.xml',



    ],
    'demo': [],
    'installable': True,
    'application': True,
    'auto_install': False,
}

