from odoo import fields, models


class Teacher(models.Model):
    _inherit = "hr.employee"
    take_class = fields.Char(string="Classes")
