from odoo import fields, models


class Teacher(models.Model):
    _inherit = "hr.employee"
    teacher_name_designation = fields.Char(string="Designation")
    subject_name = fields.One2many('teacher.class', 'class_name', string="Classes")


class Class(models.Model):
    _name = 'teacher.class'
    _description = "teacher class"
    class_name = fields.Char(string="Title", required=True)
