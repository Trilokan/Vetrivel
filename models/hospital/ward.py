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
    ward_uid = fields.Char(string="Code", required=True)
    bed_ids = fields.One2many(comodel_name="arc.bed", inverse_name="ward_id")
