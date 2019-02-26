# -*- coding: utf-8 -*-

from odoo import models, fields


class Section(models.Model):
    _name = "school.section"

    name = fields.Char(string="Section", required=True)
