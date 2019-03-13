# -*- coding: utf-8 -*-

from odoo import models, fields


class Standard(models.Model):
    _name = "arc.standard"

    name = fields.Many2one(comodel_name="school.standard", string="Standard", required=True)
    image = fields.Binary(string="Image")
    academic_id = fields.Many2one(comodel_name="arc.academic", string="Academic", required=True)
    section_ids = fields.One2many(comodel_name="arc.section", inverse_name="standard_id")

    # Computed
    students_count = fields.Integer(string="Students", compute="_get_students_count")
    teachers_count = fields.Integer(string="Students", compute="_get_teachers_count")
    boys_count = fields.Integer(string="Students", compute="_get_boys_count")
    girls_count = fields.Integer(string="Students", compute="_get_girls_count")

    def _get_students_count(self):
        for rec in self:
            rec.students_count = 0

        return True

    def _get_teachers_count(self):
        for rec in self:
            rec.teachers_count = 0

        return True

    def _get_boys_count(self):
        for rec in self:
            rec.boys_count = 0

        return True

    def _get_girls_count(self):
        for rec in self:
            rec.girls_count = 0

        return True
