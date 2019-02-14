# -*- coding: utf-8 -*-

from odoo import fields, models, api, exceptions, _
from datetime import datetime, timedelta


# Work Sheet
class WorkSheet(models.Model):
    _name = "work.sheet"
    _inherit = "mail.thread"

    name = fields.Char(string="Name", readonly=True)
    employee_id = fields.Many2one(comodel_name="hr.employee", string="Employee", required=True)
    month_id = fields.Many2one(comodel_name="month.attendance", string="Month", required=True)
    month_days = fields.Float(string="Days in Month", default=0.0, required=True)
    total_days = fields.Float(string="Total Days", default=0.0, required=True)
    schedule_days = fields.Float(string="Schedule Days", default=0.0, required=True)
    holidays = fields.Float(string="Holidays", default=0.0, required=True)
    present_days = fields.Float(string="Present Days", default=0.0, required=True)
    ot_days = fields.Float(string="Total Days", default=0.0, required=True)
    co_days = fields.Float(string="Total Days", default=0.0, required=True)
    lop_days = fields.Float(string="Total Days", default=0.0, required=True)
    leave_days = fields.Float(string="Leave Days", default=0.0, required=True)
    leave_details = fields.One2many(comodel_name="leave.details", inverse_name="work_sheet_id")
    payslip_id = fields.Many2one(comodel_name="pay.slip", string="Payslip")
