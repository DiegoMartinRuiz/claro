# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
from odoo import models, fields
class ClaroTerminalesgsm(models.Model):
    _name = "claro.gsm"
    _description = "Claro Terminales GSM"

    id_terminal = fields.Float('ID Terminal',size=20, digits=(20, 0), required=False) 
    estado_id = fields.Integer('Estado ID', required=False)  
    imei = fields.Float('IMEI', size=20, digits=(20, 0),required=False) 
    cod_producto = fields.Float('Codigo de Producto',size=15, digits=(15, 0), required=False) 
    descripcion = fields.Char('Descripcion', required=False) 
    entidad = fields.Integer('Entidad', required=False) 
    f_activa = fields.Datetime('Fecha de Activacion', required=False) 
   