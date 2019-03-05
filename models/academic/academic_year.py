# -*- coding: utf-8 -*-

from odoo import models, fields


class AcademicYear(models.Model):
    _name = "academic.year"

    name = fields.Many2one(comodel_name="school.year", string="Year", required=True)
    standard_ids = fields.One2many(comodel_name="academic.standard", inverse_name="year_id")
