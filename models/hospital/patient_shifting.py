# -*- coding: utf-8 -*-

from odoo import models, fields
from datetime import datetime

PROGRESS_INFO = [("draft", "Draft"), ("shifted", "Shifted")]
CURRENT_DATE = datetime.now().strftime("%Y-%m-%d")
CURRENT_TIME = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
CURRENT_INDIA = datetime.now().strftime("%d-%m-%Y %H:%M:%S")


# Patient Shifting
class PatientShifting(models.Model):
    _name = "patient.shifting"

    date = fields.Date(string="Date", required=True)
    name = fields.Char(string="Name", readonly=True)
    person_id = fields.Many2one(comodel_name="arc.person", string="Person")
    from_bed_id = fields.Many2one(comodel_name="arc.bed", string="From")
    to_bed_id = fields.Many2one(comodel_name="arc.bed", string="To")
    progress = fields.Selection(selection=PROGRESS_INFO, default="draft")
