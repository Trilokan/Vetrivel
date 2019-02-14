# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import datetime

PROGRESS_INFO = [("un_posted", "Un Posted"), ("posted", "Posted")]
CURRENT_DATE = datetime.now().strftime("%Y-%m-%d")
CURRENT_TIME = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
CURRENT_INDIA = datetime.now().strftime("%d-%m-%Y %H:%M:%S")


class JournalItem(models.Model):
    _name = "journal.item"

    date = fields.Date(string="Date", required=True, default=CURRENT_DATE)
    name = fields.Char(string="Name", readonly=True)
    invoice_id = fields.Many2one(comodel_name="arc.invoice", string="Invoice")
    journal_type_id = fields.Many2one(comodel_name="journal.type", string="Journal Type", required=True)
    person_id = fields.Many2one(comodel_name="arc.person", string="Person")
    description = fields.Text(string="Description")
    credit = fields.Float(string="Credit", required=True, default=0.0)
    debit = fields.Float(string="Debit", required=True, default=0.0)
    full_reconcile_id = fields.Many2one(comodel_name="arc.reconcile", string="Full Reconcile")
    part_reconcile_id = fields.Many2one(comodel_name="arc.reconcile", string="Part Reconcile")
    journal_id = fields.Many2one(comodel_name="arc.journal", string="Journal Entry")
    progress = fields.Selection(selection="", string="Progress", related="journal_id.progress")

    @api.model
    def create(self, vals):
        if (vals["credit"] > 0) or (vals["debit"] > 0):
            vals["name"] = self.env["ir.sequence"].next_by_code(self._name)
            return super(JournalItem, self).create(vals)
