# -*- coding: utf-8 -*-

from odoo import models, fields


class AcademicStandard(models.Model):
    _name = "academic.standard"

    name = fields.Many2one(comodel_name="school.standard", string="Standard", required=True)
    year_id = fields.Many2one(comodel_name="academic.year", string="Year", required=True)
    total_male = fields.Integer(string="Total Male", compute="_get_total_male")
    total_female = fields.Integer(string="Total Male", compute="_get_total_male")
    total_staff = fields.Integer(string="Total Male", compute="_get_total_male")
    section_ids = fields.One2many(comodel_name="academic.section", inverse_name="standard_id")

    def _get_total_male(self):
        for rec in self:
            rec.total_male = 0
        return True

    def _get_total_female(self):
        for rec in self:
            rec.total_female = 0
        return True

    def _get_total_staff(self):
        for rec in self:
            rec.total_staff = 0
        return True
    