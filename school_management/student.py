from datetime import date

from odoo import fields, models


class Student(models.Model):
    _name = "student_detail"
    _description = "Student information"

    student_name = fields.Char(string="Name", tracking=True)
    rollno = fields.Integer(string="ID")
    _sql_constraints = [('user_rollno_uniq', 'unique (rollno)',
                         "The User ID must be unique, this one is already assigned to another user.")]
    dob = fields.Date(string="Date of Birth")
    image = fields.binary(string="Image")
    introduction = fields.Text(string="Introduction")

    def _check_dates(dob):
        today = date.today()
        if today <= today:
            return dob
        else:
            return today

    _constraints = [
        (_check_dates(dob), 'Error ! Start Date must be greater then Current Date')
    ]
