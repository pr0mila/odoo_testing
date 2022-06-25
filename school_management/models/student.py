import self as self
from dateutil import parser
from datetime import datetime, time, date

from pkg_resources import _

from odoo.tools import DEFAULT_SERVER_DATETIME_FORMAT, DEFAULT_SERVER_DATE_FORMAT

from odoo import fields, models, api
from odoo.fields import Date


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
    subject_name = fields.Many2many('student.subject')

    _sql_constraints = [('user_roll_uniq', 'unique (roll)',
                         "The User ID must be unique, this one is already assigned to another user."),

                        ]

    @api.onchange('dob')
    def _onchange_dob(self):
        result = {}
        d2 = date.today()
        print(self.dob)
        print(d2)
        if self.dob:
            if self.dob > d2:
                result['warning'] = {'title': _('Warning'), 'message': _(
                    'The Product Unit of Measure you chose has a different category than in the product form.')}

        return result


# _constraints = [(_check_dates(dob), 'Error ! Date must be less than Current Date')]


# studen associated with Class and subject model


class Class(models.Model):
    _name = 'student.class'
    _description = "student class"

    name = fields.Char(string="Name")
    student_ids = fields.One2many('student.detail','class_name')


class Subjects(models.Model):
    _name = 'student.subject'
    _description = "student subjects"

    name = fields.Char(string="Name")
    student_sub_ids = fields.Many2one('student.detail','subject_name')


"""
class Subjects(models.Model):
"""
