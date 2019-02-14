# -*- coding: utf-8 -*-

from odoo import fields, models, api, exceptions, _
from datetime import datetime, timedelta

ACCOUNT_TYPE = [("draft", "Draft"), ("registered", "Registered")]
PAYMENT_TYPE = [("cash", "Cash"), ("bank", "Bank")]
PROGRESS_INFO = [("un_posted", "Un Posted"), ("posted", "Posted")]
CURRENT_DATE = datetime.now().strftime("%Y-%m-%d")
CURRENT_TIME = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
CURRENT_INDIA = datetime.now().strftime("%d-%m-%Y %H:%M:%S")


# Register Payment
class RegisterPayment(models.Model):
    _name = "register.payment"
    _inherit = "mail.thread"

    date = fields.Date(string="Date", required=True, default=CURRENT_DATE)
    name = fields.Char(string="Name", readonly=True)
    person_id = fields.Many2one(comodel_name="arc.person", string="Person", required=True)
    account_type = fields.Selection(selection=ACCOUNT_TYPE, string="Account Type", required=True)
    payment_type = fields.Selection(selection=PAYMENT_TYPE, stringh="Payment Type", required=True)
    invoice_id = fields.Many2one(comodel_name="arc.invoice", string="Invoice")
    amount = fields.Float(string="Amount")
    note_id = fields.Many2one(comodel_name="journal.item", string="Note")
    progress = fields.Selection(selection=PROGRESS_INFO, string="Progress", default="draft")

    @api.model
    def create(self, vals):
        vals["name"] = self.env["ir.sequence"].next_by_code(self._name)
        return super(RegisterPayment, self).create(vals)
