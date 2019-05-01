# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import datetime

CURRENT_DATE = datetime.now().strftime("%Y-%m-%d")
CURRENT_TIME = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
CURRENT_INDIA = datetime.now().strftime("%d-%m-%Y %H:%M:%S")


# Admission Discharge Reason
class AddisReason(models.Model):
    _name = "addis.reason"

    name = fields.Char(string="Reason", required=True)
    is_admission = fields.Boolean(string="Is Admission")
    is_discharge = fields.Boolean(string="Is Discharge")

