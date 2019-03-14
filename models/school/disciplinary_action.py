# -*- coding: utf-8 -*-

from odoo import models, fields, api, exceptions
from datetime import datetime, timedelta

PROGRESS_INFO = [('draft', 'Draft'), ('action_taken', 'Action Taken')]
CURRENT_DATE = datetime.now().strftime("%Y-%m-%d")
CURRENT_TIME = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
CURRENT_TIME_INDIA = datetime.now().strftime("%d-%m-%Y %H:%M:%S")


class DisciplinaryActions(models.Model):
    _name = "disciplinary.action"
    _inherit = "mail.thread"

    name = fields.Char(string="Name", readonly=True)
    date = fields.Date(string="Date", default=CURRENT_DATE, required=True)
    student_id = fields.Many2one(comodel_name="arc.student", string="Student", required=True)
    complaint_id = fields.Many2one(comodel_name="student.complaint", string="Complaint", required=True)
    details = fields.Text(string="Disciplinary Actions", required=True)
    attachment_ids = fields.Many2many(comodel_name="ir.attachment", string="Attachment")
    complaints_by = fields.Many2one(comodel_name="arc.person", string="Complaints By", required=True)
    progress = fields.Selection(selection=PROGRESS_INFO, string="Progress", default="draft")
    writter = fields.Char(string="Writter", track_visibility="always")

    @api.multi
    def trigger_action_taken(self):
        writter = "Disciplinary Actions register by {0} on {1}".format(self.env.user.name, CURRENT_TIME_INDIA)
        self.write({"progress": "action_taken", "writter": writter})

    @api.model
    def create(self, vals):
        vals["name"] = self.env["ir.sequence"].next_by_code(self._name)
        return super(DisciplinaryActions, self).create(vals)
