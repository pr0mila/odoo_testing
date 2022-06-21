from dateutil import parser
from datetime import datetime, time, date
from odoo.tools import DEFAULT_SERVER_DATETIME_FORMAT, DEFAULT_SERVER_DATE_FORMAT

from odoo import fields, models
from odoo.fields import Date





def _check_dates(dob):
    d1 = datetime.strptime(str(dob), "%Y/%m/%d").date()
    d2 = date.today()
    if d1 > d2:
        return d2
    else:
        d1


# model for student
class Student(models.Model):
    _name = "student.detail"
    _description = "Student information"

    name = fields.Char(string="Name")
    roll = fields.Integer(string="ID")
    dob = fields.Date(string="Birthday")
    image = fields.Image(string="Image")
    introduction = fields.Text(string="Introduction")
    class_name = fields.Many2one('student.class')
    subject_name = fields.Many2many('student.subject', 'name', string="Subjects",   index=True)

    _sql_constraints = [('user_roll_uniq', 'unique (roll)',
                         "The User ID must be unique, this one is already assigned to another user."),

                        ]
    # _constraints = [(_check_dates(dob), 'Error ! Date must be less than Current Date')]


# studen associated with Class and subject model

class Class(models.Model):
    _name = 'student.class'
    _description = "student class"

    name = fields.Char(string="Name")
    id = fields.Integer(string="id")


class Subjects(models.Model):
    _name = 'student.subject'
    _description = "student subjects"

    name = fields.Char(string="Name")


"""

class Subjects(models.Model):
"""
