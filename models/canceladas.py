# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
from odoo import models, fields
class ClaroLineasCanceladas(models.Model):
    _name = "claro.lineascanceladas"
    _description = "Lineas Canceladas"

    coordinador = fields.Char('Coordinador', required=False) 
    vendedor = fields.Char('Vendedor', required=False) 
    sds = fields.Char('SDS', required=False) 
    cuenta = fields.Integer('Cuenta', required=False) 
    nim = fields.Float('NIM',size=15, digits=(15, 0), required=False) 
    cliente = fields.Char('Cliente', required=False) 
    fecha_activacion = fields.Datetime('Fecha de Activacion', required=False) 
    entidad = fields.Integer('Entidad', required=False) 
    fecha_cancelacion= fields.Datetime('Fecha de Cancelacion', required=False) 
    usu_cancela=fields.Char('Usuario de cancelación', required=False)