# -*- coding: utf-8 -*-

from odoo import models, fields


class SchoolStandard(models.Model):
    _name = "school.standard"

    name = fields.Char(string="Standard", required=True)
