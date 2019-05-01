# -*- coding: utf-8 -*-

from odoo import models, fields
from datetime import datetime

CURRENT_DATE = datetime.now().strftime("%Y-%m-%d")
CURRENT_TIME = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
CURRENT_INDIA = datetime.now().strftime("%d-%m-%Y %H:%M:%S")


# Operation
class ArcOperation(models.Model):
    _name = "arc.operation"

    name = fields.Char(string="Operation", required=True)
    treatment_id = ""
    doctor_id = fields.Many2one(comodel_name="arc.person", string="Doctor", required=True)
    assistant_ids = fields.Many2many(comodel_name="arc.person", string="Assistants", required=True)
    is_account_approved = ""
    is_procedure_completed = ""
    date = fields.Date(string="Date")
    ot_id = fields.Many2one(comodel_name="operation.theater", string="Operation Theater")
    operation_list_id = ""
    attachment_ids = ""


