# -*- coding: utf-8 -*-

from odoo import models, fields
from datetime import datetime

CURRENT_DATE = datetime.now().strftime("%Y-%m-%d")
CURRENT_TIME = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
CURRENT_INDIA = datetime.now().strftime("%d-%m-%Y %H:%M:%S")


# Bed
class BedStatus(models.TransientModel):
    _name = "bed.status"

    wards_count = ""
    beds_count = ""
    occupied_count = ""