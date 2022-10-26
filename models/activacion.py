# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
from odoo import models, fields
class ClaroActivacion(models.Model):
    _name = "claro.activacion"
    _description = "Claro Activaciones"
    store = fields.Char('Store', required=False)
    agente = fields.Char('Agente', required=False)
    subagente = fields.Char('Subagente', required=False)
    coordinador = fields.Char('Coordinador', required=False)
    vendedor = fields.Char('Vendedor', required=False)
    dni_vendedor = fields.Char('DNI Vendedor', required=False)
    entidad = fields.Integer('Entidad', required=False)
    sds = fields.Char('SDS', required=False)
    nim = fields.Char('Nim', required=False)
    nse = fields.Char('NSE', required=False)
    imei = fields.Float('IMEI', size=15, digits=(15, 0),required=False) 
    cuenta = fields.Integer('Cuenta', required=False)
    titular = fields.Char('Titular', required=False)
    bloque = fields.Char('Bloque', required=False)
    mercado = fields.Char('Mercado', required=False)
    equipo = fields.Char('Equipo', required=False)
    promocion = fields.Integer('Promoción', required=False)
    plan = fields.Char('Plan', required=False)
    forma_pago = fields.Char('Forma-pago', required=False)
    fecha_act = fields.Char('Fecha-Activ', required=False)
    fecha_vta = fields.Char('Fecha-Venta', required=False)
    presuspendida = fields.Char('Presuspendida', required=False)
    pos = fields.Char('POS', required=False)
    nombre_pos = fields.Char('Nombre-POS', required=False)
    ciudad = fields.Char('Ciudad-POS', required=False)
    provincia = fields.Char('Dpto/Pcia-POS', required=False)