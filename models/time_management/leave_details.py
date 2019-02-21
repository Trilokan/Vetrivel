# -*- coding: utf-8 -*-

from odoo import fields, models, api, exceptions, _
from datetime import datetime, timedelta


# Leave Details
class LeaveDetails(models.Model):
    _name = "leave.details"
    _inherit = "mail.thread"

    work_id = fields.Many2one(comodel_name="work.sheet", string="Work Sheet")
    level_id = fields.Many2one(comodel_name="leave.level", string="Leave Level", required=True)
    sequence = fields.Integer(string="Sequence")
    type_id = fields.Many2one(comodel_name="leave.type", string="Leave Type", required=True)
    opening = fields.Float(string="Opening")
    credit = fields.Float(string="Leave Credit")
    reconcile = fields.Float(string="Leave Taken")
    closing = fields.Float(string="Closing")
