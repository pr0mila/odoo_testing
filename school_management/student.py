from datetime import datetime, time, date

from odoo import fields, models
from odoo.fields import Date


def _check_dates(dob):
    today = Date.today()
    if dob <= today:
        return dob
    else:
        return today


class Student(models.Model):
    _name = "student.detail"
    _description = "Student information"

    student_name = fields.Char(string="Name", tracking=True)
    roll = fields.Integer(string="ID")
    dob = fields.Date(string="Birthday")
    image = fields.Image(string="Image")
    introduction = fields.Text(string="Introduction")
    class_name = fields.Many2one('student.class')
    subject_name = fields.One2many('student.subject', 'subjects_name', string="Subjects")

    _sql_constraints = [('user_roll_uniq', 'unique (roll)',
                         "The User ID must be unique, this one is already assigned to another user."),

                        ]


#  _constraints = [(_check_dates(dob), 'Error ! Date must be less than Current Date')]


class Class(models.Model):
    _name = 'student.class'
    _description = "student class"
    class_name = fields.Char(string="Title", required=True)


class Subjects(models.Model):
    _name = 'student.subject'
    _description = "student subjects"
    subjects_name = fields.Char(string="Title", required=True)


"""

class Subjects(models.Model):
"""
