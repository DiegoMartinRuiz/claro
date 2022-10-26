# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
from odoo import models, fields
class ClaroSolicitudesSds(models.Model):
    _name = "claro.solicitudes_sds"
    _description = "Claro Solicitudes"

    srf_id = fields.Char('SRF ID', required=False)
    srf_identi_type = fields.Char('Srf Identification Type', required=False)
    srf_identifica_num = fields.Float('Srf Identification Number', size=15, digits=(15, 0),required=False)
    srf_sex = fields.Char('Srf Sex', required=False)
    srf_birth_date = fields.Datetime('Srf Birth Date', required=False)
    srf_client_last_name = fields.Char('Srf Client Last Name', required=False)
    srf_client_first_name = fields.Char('Srf Client First Name', required=False)
    srf_request_last_name = fields.Char('Srf Requester Last Name', required=False)
    srf_user_last_name = fields.Char('Srf User Last Name', required=False)
    srf_user_first_name = fields.Char('Srf User First Name', required=False)
    srf_billing_street = fields.Char('Srf Billing Street', required=False)
    srf_billing_number = fields.Integer('Srf Billing Number', required=False)
    srf_billing_floor = fields.Char('Srf Billing Floor', required=False)
    srf_billing_apartament = fields.Char('Srf Billing Apartment', required=False)
    srf_billing_po_box = fields.Char('Srf Billing Po Box', required=False)
    srf_mvl_codigo = fields.Integer('Srf Mvl Codigo', required=False)
    srf_client_phone = fields.Float('Srf Client Phone', size=15, digits=(15, 0),required=False)
    srf_vat_id = fields.Char('Srf Vat Id', required=False)
    srf_cuit = fields.Float('Srf Cuit', size=15, digits=(15, 0),required=False)
    srf_cpa = fields.Char('Srf Cpa', required=False)
    srf_billing_distri = fields.Char('Srf Billing District', required=False)
    srf_billing_city = fields.Char('Srf Billing City', required=False)
    geu_descrip = fields.Char('Geu Description', required=False)
    srf_bco_cmp_id = fields.Float('Srf Bco Cmp Id', required=False)
    srf_bco_cbtld = fields.Char('Srf Bco Cbt Id', required=False)
    entidad_id = fields.Char('Entidad Id', required=False)
    entidad_padre_id = fields.Char('Entidad Padre Id', required=False)
    srf_acti_date = fields.Datetime('Srf Activation Date', required=False)
    store_usu = fields.Char('Store Usuario', required=False)
    