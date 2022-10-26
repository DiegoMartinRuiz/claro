# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Claro',
    'version': '1.0',
    'category': 'Sales',
    'author': 'Diego Ruiz',
    'depends': [],
    'description': """
Este modulo tiene como objetivo la integracion de toda la informacion necesaria para el seguimiento de las
actividades registradas en los sistemas de CLARO
    """,
    'data': [
        'views/claro_principal.xml',
        'views/cancelaciones.xml',
        'views/claro_activacion.xml',
        'views/claro_pagos_asoc_sds.xml',
        'views/claro_solicitudes_sds.xml',
        'views/claro_solicitudes.xml',
        'views/claro_terminalesgsm.xml',
        'views/claro_vta_equipos.xml',
        #'views/claro_reportes_activacion.xml',
        'security/ir.model.access.csv', 
    ],
 
    'installable': True,
    'auto_install': False,
    'license': 'LGPL-3',
    'application': True, 
}
