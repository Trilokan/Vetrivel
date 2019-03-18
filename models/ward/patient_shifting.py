# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import datetime

PROGRESS_INFO = [("draft", "Draft"), ("shifted", "Shifted")]
SHIFT_TYPE = [("internal", "Internal"), ("admission", "Admission"), ("discharge", "Discharge")]
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
    shift_type = fields.Selection(selection=SHIFT_TYPE, string="Shifting")
    progress = fields.Selection(selection=PROGRESS_INFO, default="draft")

    @api.model
    def create(self, vals):
        vals["name"] = self.env["ir.sequence"].next_by_code(self._name)
        return super(PatientShifting, self).create(vals)
