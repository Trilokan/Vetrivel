# -*- coding: utf-8 -*-

from odoo import models, fields
from datetime import datetime

CURRENT_DATE = datetime.now().strftime("%Y-%m-%d")
CURRENT_TIME = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
CURRENT_INDIA = datetime.now().strftime("%d-%m-%Y %H:%M:%S")


# Operation Theater
class OperationTheater(models.Model):
    _name = "operation.theater"

    name = fields.Char(string="Name", required=True)
    theater_uid = fields.Char(string="Code", required=True)
    in_charge_id = fields.Many2one(comodel_name="arc.person", string="In-Charge")
    # equipment_ids = fields.One2many(comodel_name="")


