# -*- coding: utf-8 -*-

from odoo import models, fields


class VendorType(models.Model):
    _name = "vendor.type"

    name = fields.Char(string="Name", required=True)
