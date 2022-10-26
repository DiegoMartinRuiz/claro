# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
from odoo import models, fields
class ClaroSolicitudes(models.Model):
    _name = "claro.solicitudes"
    _description = "Claro Solicitudes"

    srf_id = fields.Integer('SRF ID', required=True)
    n6 = fields.Integer('6', required=False)
    srf_activation_date = fields.Datetime('Srf Activation Date', required=False)
    agente = fields.Char('Agente', required=False)
    subagente = fields.Integer('SubAgente', required=False)
    srf_blc_block_code = fields.Char('Srf Blc Block Code', required=False)
    blc_mkc_market_code = fields.Char('Blc MKC Market Code', required=False)
    srf_celular_number3 = fields.Integer('Srf Cellular Number3', required=False)
    srf_celular_number5 = fields.Integer('Srf Cellular Number5', required=False)
    srf_celular_number7 = fields.Integer('Srf Cellular Number7', required=False)
    srf_account_number1 = fields.Integer('Srf Account Number1', required=False)
    srf_account_number2 = fields.Integer('Srf Account Number2',size=15, digits=(15, 0), required=False)
    srf_spn_spc_id = fields.Integer('SRF SPN SPC ID', required=False)
    srf_rpl_id = fields.Char('SRF RPL ID', required=False)
    decode_srf_est_id = fields.Integer('Decode SRF Est ID', required=False)
    srf_equipament_receipt = fields.Integer('Srf Equipment Receipt', required=False)
    pro_type = fields.Char('Pro Type', required=False)
    srf_pro_id = fields.Char('SRF Pro ID', required=False)
    srf_hex_esn = fields.Char('SRF HEX ESN', required=False)
    decode_srf_coe_cel_id = fields.Integer('Decode Srf Coe Cet Id', required=False)
    srf_debit_number = fields.Char('Srf Debit Number', required=False)
    srf_coe_id = fields.Integer('SRF COE ID', required=False)
    srf_a_promotores_ent_id = fields.Char('SRF A Promotores ent ID', required=False)
    srf_vend_ent_id = fields.Char('Srf A Vendedores Ent Id', required=False)
    srf_form_number = fields.Char('SRF Form Number', required=False)
    srf_vendedor_dni = fields.Integer('Srf Vendedor Dni', required=False)
    srf_aent_descrip_code = fields.Char('Srf Aent Descriptive Code', required=False)
    entidad_padre_id = fields.Integer('Entidad Padre Id', required=False)
    entidad_id = fields.Integer('Entidad Id', required=False)
    usp_id_mav = fields.Char('USP ID MAV', required=False)