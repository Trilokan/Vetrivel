# -*- coding: utf-8 -*-

from odoo import models, fields, api, exceptions
from datetime import datetime, timedelta

PROGRESS_INFO = [('draft', 'Draft'), ('confirmed', 'Confirmed')]
CURRENT_DATE = datetime.now().strftime("%Y-%m-%d")
CURRENT_TIME = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
CURRENT_TIME_INDIA = datetime.now().strftime("%d-%m-%Y %H:%M:%S")


class HRHiring(models.Model):
    _name = "hr.hiring"

    name = fields.Char(string="Name", readonly=True)
    date = fields.Date(string="Date", default=CURRENT_DATE, required=True)
    # emp_name = fields.Char(string="Employee Name")
    # emp_uid = ""
    attachment_ids = fields.Many2many(comodel_name="ir.attachment", string="Attachment")
    register_by = fields.Many2one(comodel_name="arc.person", string="Person", required=True)
    progress = fields.Selection(selection=PROGRESS_INFO, string="Progress", default="draft")
