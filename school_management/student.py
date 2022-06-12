from odoo import fields, models


class Student(models.Model):
    _name = "student_detail"
    _description = "Student information"

    Name = fields.Char(string="Name", tracking=True)
    RollNo = fields.Integer(string="ID")
    DOB = fields.Date(string="Date of Birth")
    Image = fields.Image(string="Image")
    Introduction = fields.Char(string="Introduction")
