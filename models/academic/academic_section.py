# -*- coding: utf-8 -*-

from odoo import models, fields


class AcademicSection(models.Model):
    _name = "academic.section"

    name = fields.Many2one(comodel_name="school.section", string="Section", required=True)
    year_id = fields.Many2one(comodel_name="academic.year", string="Year", required=True)
    standard_id = fields.Many2one(comodel_name="academic.standard", string="Standard", required=True)

    student_ids = fields.One2many(comodel_name="academic.student", inverse_name="section_id")
    syllabus_ids = fields.One2many(comodel_name="academic.syllabus", inverse_name="section_id")
    # Exam
    # Test
    # Time Table

