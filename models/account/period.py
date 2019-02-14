# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import datetime

PROGRESS_INFO = [("draft", "Draft"), ("open", "Open"), ("closed", "Closed")]
CURRENT_DATE = datetime.now().strftime("%Y-%m-%d")
CURRENT_TIME = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
CURRENT_TIME_INDIA = datetime.now().strftime("%d-%m-%Y %H:%M:%S")


class ArcPeriod(models.Model):
    _name = "arc.period"

    name = fields.Char(string="Name", required=True)
    start_date = fields.Date(string="Start Date", required=True)
    end_date = fields.Date(string="End Date", required=True)
    progress = fields.Selection(selection=PROGRESS_INFO, default="draft", string="Progress")
    is_month = fields.Boolean(string="Is Month")
    writter = fields.Text(string="Writter", track_visibility="always")

    @api.multi
    def trigger_open(self):
        writter = "Period Open by {0} on {1}".format(self.env.user.name, CURRENT_TIME_INDIA)
        data = {"progress": "open", "writter": writter}

        self.write(data)

    @api.multi
    def trigger_close(self):
        writter = "Period Closed by {0} on {1}".format(self.env.user.name, CURRENT_TIME_INDIA)
        data = {"progress": "closed", "writter": writter}

        self.write(data)

    def generate_month_attendance(self):
        pass

    @api.model
    def create(self, vals):
        self.generate_month_attendance()
        return super(ArcPeriod, self).create(vals)
