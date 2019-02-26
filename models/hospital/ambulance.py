# -*- coding: utf-8 -*-

from odoo import models, fields
from datetime import datetime

PROGRESS_INFO = [("draft", "Draft"), ("shifted", "Shifted")]
CURRENT_DATE = datetime.now().strftime("%Y-%m-%d")
CURRENT_TIME = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
CURRENT_INDIA = datetime.now().strftime("%d-%m-%Y %H:%M:%S")


# Ambulance
class Ambulance(models.Model):
    _name = "arc.ambulance"

    date = fields.Date(string="Date", required=True)
    name = fields.Char(string="Name", readonly=True)
