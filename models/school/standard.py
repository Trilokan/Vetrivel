# -*- coding: utf-8 -*-

from odoo import models, fields


class Standard(models.Model):
    _name = "school.standard"

    name = fields.Char(string="Standard", required=True)
