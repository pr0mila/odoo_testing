
from datetime import datetime, time, date

from odoo import fields, models


def _check_dates(dob):
    today = date.today()
    if today <= today:
        return dob
    else:
        return today


class Student(models.Model):
    _name = "student_detail"
    _description = "Student information"

    student_name = fields.Char(string="Name", tracking=True)
    roll = fields.Integer(string="ID")
    dob = fields.Date(string="Birthday")
    image = fields.Image(string="Image")
    introduction = fields.Text(string="Introduction")

    _sql_constraints = [('user_roll_uniq', 'unique (roll)',
                         "The User ID must be unique, this one is already assigned to another user."),

                        ]
    _constraints = [ (_check_dates(dob), 'Error ! Date must be less than Current Date')]


"""
class Class(models.Model):
class Subjects(models.Model):
"""