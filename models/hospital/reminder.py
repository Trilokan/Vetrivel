# -*- coding: utf-8 -*-

from odoo import models, fields
from datetime import datetime

CURRENT_DATE = datetime.now().strftime("%Y-%m-%d")
CURRENT_TIME = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
CURRENT_INDIA = datetime.now().strftime("%d-%m-%Y %H:%M:%S")


# Notes
class HRReminder(models.Model):
    _name = "hr.reminder"

    date = fields.Date(string="Date", default=CURRENT_DATE, required=True)
    person_id = fields.Many2one(comodel_name="arc.person", string="Person",
                                default=lambda self: self.env.user.person_id.id,
                                required=True)
    remind_on = fields.Datetime(string="Remind On", required=True)
    is_remind = fields.Boolean(string="Is Remind", readonly=True)
    message = fields.Text(string="Message", required=True)

    def cron_trigger_remind(self):
        self.is_remind = True
