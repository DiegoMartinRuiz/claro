# -*- coding: utf-8 -*-

from odoo import models, fields
class ClaroPagosAsoc(models.Model):
    _name = "claro.pagossds"
    _description = "Pagos Asociados SDS"

    id_sds = fields.Float('Id Sds', size=15, digits=(15, 0),required=False)
    f_act = fields.Datetime('Fecha Activación', required=False) 
    nim = fields.Float('NIM', size=15, digits=(15, 0),required=False) 
    bill_number = fields.Float('Bill Number',size=15, digits=(15, 0), required=False) 
    cta = fields.Float('Cuenta',size=15, digits=(15, 0), required=False) 
    tipo_pago = fields.Char('Tipo Pago', required=False) 
    ent_pago = fields.Char('Entidad Pago', required=False) 
    coe_id= fields.Char('COE ID', required=False) 
    forma_pago = fields.Integer('Forma Pago', required=False) 
    cuotas = fields.Integer('Cuotas', required=False) 
    cod_auto = fields.Integer('Cod Aut', required=False) 
    num_tarjeta = fields.Char('Numero de Tarjeta', required=False) 
    importe = fields.Float('Importe', required=False) 
 
