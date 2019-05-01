# -*- coding: utf-8 -*-

from odoo import models, fields
from datetime import datetime

CURRENT_DATE = datetime.now().strftime("%Y-%m-%d")
CURRENT_TIME = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
CURRENT_INDIA = datetime.now().strftime("%d-%m-%Y %H:%M:%S")


class HomeWork(models.Model):
    _name = "home.work"

    date = fields.Date(string="Date", default=CURRENT_INDIA, required=True)
    academic_id = fields.Many2one(comodel_name="arc.academic", string="Academic")
    standard_id = fields.Many2one(comodel_name="arc.standard", string="Standard")
    section_id = fields.Many2one(comodel_name="arc.section", string="Section")
    subject_id = fields.Many2one(comodel_name="arc.subject", string="Subject")
    description = fields.Text(string="Description")
    comment = fields.Text(string="Comment")
