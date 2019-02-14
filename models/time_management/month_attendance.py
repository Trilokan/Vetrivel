# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import datetime

PROGRESS_INFO = [("draft", "Draft"), ("open", "Open"), ("closed", "Closed")]
CURRENT_DATE = datetime.now().strftime("%Y-%m-%d")
CURRENT_TIME = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
CURRENT_TIME_INDIA = datetime.now().strftime("%d-%m-%Y %H:%M:%S")


class MonthAttendance(models.Model):
    _name = "month.attendance"

    period_id = fields.Many2one(comodel_name="arc.period", string="Period",
                                domain="[('is_month', '=', True)]")
    month_detail = fields.One2many(comodel_name="daily.attendance", inverse_name="month_id")
    progress = fields.Selection(PROGRESS_INFO, string='Progress', default="draft")

    _sql_constraints = [('unique_period_id', 'unique (period_id)', 'Error! Month must be unique')]

    @api.multi
    def trigger_open(self):
        pass

    @api.multi
    def trigger_close(self):
        pass
