# -*- coding: utf-8 -*-

from odoo import models, fields
from datetime import datetime


# Operation Theater
class OperationTheater(models.Model):
    _name = "operation.theater"

    image = fields.Binary(string="Image")
    name = fields.Char(string="Name", required=True)
    theater_uid = fields.Char(string="Code", required=True)
    supervisor_id = fields.Many2one(comodel_name="arc.person", string="In-Charge")
    equipment_ids = fields.Many2many(comodel_name="arc.asserts", string="Equipments")
    facility_detail = fields.Html(string="Facility Details")
    operation_ids = fields.One2many(comodel_name="arc.operation", inverse_name="ot_id")


