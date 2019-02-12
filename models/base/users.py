# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ArcUsers(models.Model):
    _name = "res.users"
    _inherit = "res.users"

    person_id = fields.Many2one(comodel_name="arc.person", string="Person")

