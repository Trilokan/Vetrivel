# -*- coding: utf-8 -*-

from odoo import models, fields
from datetime import datetime

CURRENT_DATE = datetime.now().strftime("%Y-%m-%d")
CURRENT_TIME = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
CURRENT_INDIA = datetime.now().strftime("%d-%m-%Y %H:%M:%S")


# Notes
class HRNotes(models.Model):
    _name = "hr.notes"
    _rec_name = "person_id"

    date = fields.Date(string="Date", default=CURRENT_DATE, required=True)
    person_id = fields.Many2one(comodel_name="arc.person", string="Person",
                                default=lambda self: self.env.user.person_id.id,
                                readonly=True)
    notes = fields.Text(string="Notes", required=True)
