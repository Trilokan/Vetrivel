# -*- coding: utf-8 -*-

from odoo import models, fields


class SchoolSection(models.Model):
    _name = "school.section"

    name = fields.Char(string="Section", required=True)
