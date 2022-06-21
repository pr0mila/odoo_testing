from odoo import fields, models


# hr.employee inherited by Teacher model

class Teacher(models.Model):
    _inherit = "hr.employee"
    teacher_name_designation = fields.Char(string="Designation")
    class_name = fields.One2many('teacher.class', 'name', string="Subjects")


# teacher associated model Class
class Class(models.Model):
    _name = 'teacher.class'
    _description = "teacher class"
    name = fields.Char(string="Classes")
