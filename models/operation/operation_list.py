# -*- coding: utf-8 -*-

from odoo import models, fields
from datetime import datetime

CURRENT_DATE = datetime.now().strftime("%Y-%m-%d")
CURRENT_TIME = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
CURRENT_INDIA = datetime.now().strftime("%d-%m-%Y %H:%M:%S")


# List Of Operation
class OperationList(models.Model):
    _name = "operation.list"

    name = fields.Char(string="Operation", required=True)
    operation_uid = fields.Char(string="Code", required=True)
    attachment_ids = fields.Many2many(comodel_name="ir.attachment", string="Attachment")
    procedure = fields.Html(string="Operation Procedures")
