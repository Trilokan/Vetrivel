# -*- coding: utf-8 -*-

from odoo import models, fields


class EmployeeType(models.Model):
    _name = "employee.type"

    name = fields.Char(string="Name", required=True)
