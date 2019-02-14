# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import datetime

PROGRESS_INFO = [("un_posted", "Un Posted"), ("posted", "Posted")]
CURRENT_DATE = datetime.now().strftime("%Y-%m-%d")
CURRENT_TIME = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
CURRENT_INDIA = datetime.now().strftime("%d-%m-%Y %H:%M:%S")


class ArcJournal(models.Model):
    _name = "arc.journal"

    date = fields.Date(string="Date", required=True, default=CURRENT_DATE)
    name = fields.Char(string="Name", readonly=True)
    journal_type_id = fields.Many2one(comodel_name="journal.type", string="Journal Type", required=True)
    period_id = fields.Many2one(comodel_name="arc.period", string="Period", readonly=True)
    reference = fields.Char(string="Reference")
    progress = fields.Selection(selection=PROGRESS_INFO, string="Progress", default="un_posted")
    item_ids = fields.One2many(comodel_name="journal.item", inverse_name="journal_id")

    @api.model
    def create(self, vals):
        vals["name"] = self.env["ir.sequence"].next_by_code(self._name)
        return super(ArcJournal, self).create(vals)
