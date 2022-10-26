# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
from odoo import models, fields
class ClaroVtEquipos(models.Model):
    _name = "claro.vtequipos"
    _description = "Claro Venta de Equipos"

    agencia = fields.Char('Agencia', required=False) 
    entidad_hija = fields.Float('Entidad Hija', size=20, digits=(20, 0),required=False) 
    dni_vendedor = fields.Float('DNI-Vendedor', size=20, digits=(20, 0),required=False) 
    nim = fields.Float('NIM', size=20, digits=(20, 0), required=False) 
    bill_number = fields.Float('Bill-Number', size=20, digits=(20, 0),required=False) 
    cuenta = fields.Integer('Cuenta', size=20, digits=(20, 0), required=False)
    apellido = fields.Char('Apellido', required=False) 
    nombre= fields.Char('Nombre', required=False) 
    cond_iva = fields.Char('Cond-IVA', required=False) 
    terminal = fields.Char('Terminal', required=False) 
    pro_model = fields.Char('Pro Model', required=False) 
    imei = fields.Float('IMEI', size=20, digits=(20, 0),required=False) 
    sim = fields.Float('SIM', size=20, digits=(20, 0), required=False) 
    f_migracion = fields.Datetime('Fecha-Migracion', required=False) 
    tipo_venta = fields.Char('TipoVenta', required=False) 
    forma_pago= fields.Char('Forma-Pago', required=False) 
    forma_pago_desc= fields.Float('Forma-Pago Description', size=20, digits=(20, 0),required=False) 
    monto_partida = fields.Float('Monto-Partida', required=False) 
    cod_newprince = fields.Float('Cod-NewPrince', size=20, digits=(20, 0), required=False) 
    nrocupon = fields.Char('NroCupon', required=False) 
    subsidio_remanente = fields.Float('Subsidio Remanente', required=False) 
    cater_sds_id = fields.Char('Cater Sds Id', required=False) 
    eft= fields.Float('EFTS', required=False) 
    ch = fields.Float('CH', required=False) 
    f= fields.Float('F', required=False) 
    td= fields.Float('TD', required=False) 
    tc= fields.Float('C', required=False) 
    otro= fields.Float('Otro', required=False) 

