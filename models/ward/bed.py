# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import datetime

CURRENT_DATE = datetime.now().strftime("%Y-%m-%d")
CURRENT_TIME = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
CURRENT_INDIA = datetime.now().strftime("%d-%m-%Y %H:%M:%S")


# Bed
class ArcBed(models.Model):
    _name = "arc.bed"

    name = fields.Char(string="Bed", required=True)
    bed_uid = fields.Char(string="Code", required=True)
    bed_type = fields.Many2one(comodel_name="bed.type", string="Bed Type")
    amount = fields.Float(string="Amount", default=0.0)
    ward_id = fields.Many2one(comodel_name="arc.ward", string="Ward", required=True)

    @api.multi
    def name_get(self):
        result = []
        for record in self:
            name = "[{0}] {1}".format(record.bed_uid, record.name)
            result.append((record.id, name))
        return result
