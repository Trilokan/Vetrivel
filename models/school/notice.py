# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import datetime

PROGRESS_INFO = [("draft", "Draft"), ("confirmed", "Confirmed"), ("cancel", "Cancel")]
CURRENT_DATE = datetime.now().strftime("%Y-%m-%d")
CURRENT_TIME = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
CURRENT_TIME_INDIA = datetime.now().strftime("%d-%m-%Y %H:%M:%S")


class SchoolNotice(models.Model):
    _name = "school.notice"
    _inherit = "mail.thread"

    date = fields.Date(string="Date", required=True)
    name = fields.Char(string="Name", readonly=True)
    notice = fields.Char(string="Notice", required=True)
    notice_detail = fields.Html(string="Notice Detail")
    progress = fields.Selection(selection=PROGRESS_INFO, default="draft")
    attachment_ids = fields.Many2many(comodel_name="ir.attachment", string="Attachment")
    writter = fields.Text(string="Writter", track_visibility="always")

    @api.multi
    def trigger_confirm(self):
        writter = "School Notice confirm by {0} on {1}".format(self.env.user.name, CURRENT_TIME_INDIA)
        self.write({"progress": "confirmed", "writter": writter})

    @api.multi
    def trigger_cancel(self):
        writter = "School Notice cancel by {0} on {1}".format(self.env.user.name, CURRENT_TIME_INDIA)
        self.write({"progress": "cancel", "writter": writter})

    @api.model
    def create(self, vals):
        vals["notice"] = self.env["ir.sequence"].next_by_code(self._name)
        return super(SchoolNotice, self).create(vals)

