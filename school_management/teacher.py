from odoo import fields, models


class Teacher(models.Model):
    _inherit = "hr.employee"
    teacher_name_designation = fields.Char(string="Designation")




