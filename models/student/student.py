# -*- coding: utf-8 -*-

from odoo import models, fields

BLOOD_GROUP = [('a+', 'A+'), ('b+', 'B+'), ('ab+', 'AB+'), ('o+', 'O+'),
               ('a-', 'A-'), ('b-', 'B-'), ('ab-', 'AB-'), ('o-', 'O-')]
GENDER = [('male', 'Male'), ('female', 'Female')]


class Student(models.Model):
    _name = "arc.student"

    name = fields.Char(string="Student", required=True)
    student_uid = fields.Char(string="Student ID", required=True)

    image = fields.Binary(string="Image")
    small_image = fields.Binary(string="Small Image")
