from odoo import tools, models, fields

class reporact(models.Model):
    _name = "report.activaciones"
    _description = "Reporte de Activaciones"
    _auto = False
    _inherit='hr.employee'
    dni_id = fields.Many2one('hr.employee','DNI')
    cuentas = fields.Char('res.cuenta')
