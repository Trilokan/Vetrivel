# -*- coding: utf-8 -*-

from odoo import models, fields


class Student(models.Model):
    _name = "arc.student"

    name = fields.Char(string="Student", required=True)
    student_uid = fields.Char(string="Student ID", required=True)

    image = fields.Binary(string="Image")
    small_image = fields.Binary(string="Small Image")
    student_id = fields.Many2one(comodel_name="school.student", string="Student")

    # Academic
    academic_id = fields.Many2one(comodel_name="arc.academic", string="Academic")
    standard_id = fields.Many2one(comodel_name="arc.standard", string="Standard")
    section_id = fields.Many2one(comodel_name="arc.section", string="Section")
    activity_id = fields.Many2one(comodel_name="curricular.activity", string="Activity")
