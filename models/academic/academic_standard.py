# -*- coding: utf-8 -*-

from odoo import models, fields


class AcademicStandard(models.Model):
    _name = "academic.standard"

    name = fields.Many2one(comodel_name="school.standard", string="Standard", required=True)
    year_id = fields.Many2one(comodel_name="academic.year", string="Year", required=True)
    section_ids = fields.One2many(comodel_name="academic.section", inverse_name="standard_id")
