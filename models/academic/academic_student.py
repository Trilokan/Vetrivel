# -*- coding: utf-8 -*-

from odoo import models, fields


class AcademicStudent(models.Model):
    _name = "academic.student"

    section_id = fields.Many2one(comodel_name="school.section", string="Section", required=True)
    student_id = fields.Many2one(comodel_name="school.student", string="Student", required=True)
    student_uid = fields.Char(string="Student ID", related="student_id.student_uid")

