# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import datetime

ACTIVITY_TYPE = [("co_curricular", "Co-Curricular"), ("extra_curricular", "Extra-Curricular")]
PROGRESS_INFO  = [("draft", "Draft"), ("confirmed", "Confirmed")]
CURRENT_DATE = datetime.now().strftime("%Y-%m-%d")
CURRENT_TIME = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
CURRENT_TIME_INDIA = datetime.now().strftime("%d-%m-%Y %H:%M:%S")


class CurricularActivity(models.Model):
    _name = "curricular.activity"
    _inherit = "mail.thread"

    date = fields.Date(string="Date", default=CURRENT_DATE, required=True)
    name = fields.Char(string="Name", readonly=True)
    activity = fields.Char(string="Activity", required=True)
    image = fields.Binary(string="Image")
    venue = fields.Char(string="Venue")
    supervisor_id = fields.Many2one(comodel_name="arc.person", string="Supervisor")
    start_date = fields.Date(string="Start Date")
    end_date = fields.Date(string="End Date")
    instructions = fields.Html(string="Instructions")
    activity_type = fields.Selection(selection=ACTIVITY_TYPE, string="Activity Type", required=True)
    student_ids = fields.Many2many(comodel_name="arc.student", string="Student")
    teacher_ids = fields.Many2many(comodel_name="arc.person", string="Teacher")
    attachment_ids = fields.Many2many(comodel_name="ir.attachment", string="Attachment")
    progress = fields.Selection(selection=PROGRESS_INFO, default="draft")

    @api.multi
    def trigger_confirm(self):
        self.write({"progress": "confirmed"})
