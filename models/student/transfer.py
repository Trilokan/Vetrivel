# -*- coding: utf-8 -*-

from odoo import models, fields, api, exceptions
from datetime import datetime

PROGRESS_INFO = [("draft", "Draft"), ("confirmed", "Confirmed"), ("approved", "Approved")]
CURRENT_DATE = datetime.now().strftime("%Y-%m-%d")
CURRENT_TIME = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
CURRENT_TIME_INDIA = datetime.now().strftime("%d-%m-%Y %H:%M:%S")


# School Transfer
class SchoolTransfer(models.Model):
    _name = "school.transfer"
    _inherit = "mail.thread"

    date = fields.Date(string="Date", default=CURRENT_DATE, required=True)
    name = fields.Char(string="Name", readonly=True)
    image = fields.Binary(string="Image")
    student_id = fields.Many2one(comodel_name="arc.student", string="Student", required=True)
    progress = fields.Selection(selection=PROGRESS_INFO, default="draft")
    reason = fields.Many2one(comodel_name="transfer.reason", required=True)
    reason_detail = fields.Text(string="Reason In Detail")
    certificate = fields.Html(string="Transfer Certificate", readonly=True)
    writter = fields.Text(string="Writter", track_visiblity="always")
    attachment_ids = fields.Many2many(comodel_name="ir.attachment", string="Attachment")

    # No dues
    is_account_approved = fields.Boolean(string="Is Accounts Approved")

    @api.multi
    def trigger_confirm(self):
        writter = "Transfer Certificate for {0} confirmed by {1} on {2}".format(self.student_id.name,
                                                                                self.env.user.name,
                                                                                CURRENT_TIME_INDIA)
        self.write({"progress": "confirmed", "writter": writter})

    @api.multi
    def trigger_transfer(self):
        if not self.is_account_approved:
            raise exceptions.ValidationError("Error! Admission Processed only after the Teacher/Accounts approval")

        writter = "{0} Transfer Certificate issued by {0} on {1}".format(self.student_id.name,
                                                                         self.env.user.name,
                                                                         CURRENT_TIME_INDIA)
        self.write({"progress": "approved", "writter": writter})
