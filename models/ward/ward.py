# -*- coding: utf-8 -*-

from odoo import models, fields
from datetime import datetime

CURRENT_DATE = datetime.now().strftime("%Y-%m-%d")
CURRENT_TIME = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
CURRENT_INDIA = datetime.now().strftime("%d-%m-%Y %H:%M:%S")


# Ward
class ArcWard(models.Model):
    _name = "arc.ward"

    name = fields.Char(string="Ward", required=True)
    image = fields.Binary(string="Image")
    ward_uid = fields.Char(string="Code", required=True)
    bed_ids = fields.One2many(comodel_name="arc.bed", inverse_name="ward_id")
    bed_count = fields.Integer(string="Bed Count", compute="_get_bed_count")
    supervisor_id = fields.Many2one(comodel_name="arc.person", string="In-Charge")

    def _get_bed_count(self):
        for rec in self:
            rec.bed_count = 0

        return True
