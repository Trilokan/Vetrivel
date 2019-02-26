# -*- coding: utf-8 -*-

from odoo import models, fields
from datetime import datetime

CURRENT_DATE = datetime.now().strftime("%Y-%m-%d")
CURRENT_TIME = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
CURRENT_INDIA = datetime.now().strftime("%d-%m-%Y %H:%M:%S")


# Bed
class ArcBed(models.Model):
    _name = "arc.bed"

    name = fields.Char(string="Bed", required=True)
    bed_uid = fields.Char(string="Code", required=True)
    ward_id = fields.Many2one(comodel_name="arc.ward", string="Ward")
