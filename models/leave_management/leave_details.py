# -*- coding: utf-8 -*-

from odoo import fields, models, api, exceptions, _
from datetime import datetime, timedelta


# Leave Details
class LeaveDetails(models.Model):
    _name = "leave.details"
    _inherit = "mail.thread"

    work_sheet_id = fields.Many2one(comodel_name="work.sheet", string="Work Sheet")
    opening = fields.Float(string="Opening")
    leave_credit = fields.Float(string="Leave Credit")
    leave_taken = fields.Float(string="Leave Taken")
    closing = fields.Float(string="Closing")
