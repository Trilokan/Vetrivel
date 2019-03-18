# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import datetime

APPOINTMENT_TYPE = [("opt", "OPT"), ("ot", "OT"), ("meeting", "Meeting")]
PROGRESS_INFO = [("cancel", "Cancel")]
CURRENT_DATE = datetime.now().strftime("%Y-%m-%d")
CURRENT_TIME = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
CURRENT_INDIA = datetime.now().strftime("%d-%m-%Y %H:%M:%S")


# Appointment
class AppointmentReason(models.Model):
    _name = "appointment.reason"

    name = fields.Char(string="Reason", required=True)
    appointment_type = fields.Selection(selection=APPOINTMENT_TYPE, string="Appointment Type", required=True)
