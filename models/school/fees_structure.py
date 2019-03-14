# -*- coding: utf-8 -*-

from odoo import models, fields, api, exceptions
from datetime import datetime, timedelta

PROGRESS_INFO = [('draft', 'Draft'), ('confirmed', 'Confirmed')]
CURRENT_DATE = datetime.now().strftime("%Y-%m-%d")
CURRENT_TIME = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
CURRENT_TIME_INDIA = datetime.now().strftime("%d-%m-%Y %H:%M:%S")


class FeesStructure(models.Model):
    _name = "fees.structure"
    _inherit = "mail.thread"

    standard_id = ""
    academic_id = ""
    structure_detail = ""
