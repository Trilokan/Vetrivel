# -*- coding: utf-8 -*-

from odoo import models, fields


class SchoolYear(models.Model):
    _name = "school.year"

    name = fields.Char(string="Year", required=True)
