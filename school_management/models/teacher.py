from odoo import fields, models
from .student import Subjects


# hr.employee inherited by Teacher model

class Teacher(models.Model):
    _inherit = "hr.employee"

    teacher_name_designation = fields.Char(string="Designation")
    class_name = fields.Many2many('student.subject')
