# -*- coding: utf-8 -*-

from odoo import models, fields, api, exceptions
from datetime import datetime, timedelta

PROGRESS_INFO = [('draft', 'Draft'),
                 ('confirmed', 'Waiting For Approval'),
                 ('cancelled', 'Cancelled'),
                 ('approved', 'Approved')]
CURRENT_DATE = datetime.now().strftime("%Y-%m-%d")
CURRENT_TIME = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
CURRENT_TIME_INDIA = datetime.now().strftime("%d-%m-%Y %H:%M:%S")


class HRPromotion(models.Model):
    _name = "hr.promotion"

    name = fields.Char(string="Name", readonly=True)
    date = fields.Date(string="Date", default=CURRENT_DATE, required=True)
    person_id = fields.Many2one(comodel_name="arc.person", string="Person", required=True)
    details = fields.Text(string="Promotion Details", required=True)
    attachment_ids = fields.Many2many(comodel_name="ir.attachment", string="Attachment")
    promoted_by = fields.Many2one(comodel_name="arc.person", string="Person", required=True)
    progress = fields.Selection(selection=PROGRESS_INFO, string="Progress", default="draft")
