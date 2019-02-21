# -*- coding: utf-8 -*-

from odoo import models, fields


# Designation
class HRDesignation(models.Model):
    _name = "hr.designation"

    name = fields.Char(string="Designation", required=True)
    type_id = fields.Many2one(comodel_name="employee.type", string="Employee Type", required=True)

    _sql_constraints = [("name", "unique(name)", "Designation must be unique")]
