# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import datetime

APPOINTMENT_TYPE = [("opt", "OPT"), ("ot", "OT"), ("meeting", "Meeting")]
PROGRESS_INFO = [("cancel", "Cancel")]
CURRENT_DATE = datetime.now().strftime("%Y-%m-%d")
CURRENT_TIME = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
CURRENT_INDIA = datetime.now().strftime("%d-%m-%Y %H:%M:%S")


# Appointment
class HRAppointment(models.Model):
    _name = "hr.appointment"
    _inherit = "mail.thread"
    
    date = fields.Date(string="Date", default=CURRENT_DATE, required=True)
    name = fields.Char(string="Name", readonly=True)
    person_id = fields.Many2one(comodel_name="arc.person", string="Person",
                                default=lambda self: self.env.user.person_id.id,
                                readonly=True)
    appointment_type = fields.Selection(selection=APPOINTMENT_TYPE, default="opt", required=True)
    appointment_for = fields.Many2one(comodel_name="arc.person", string="Person")
    reason = fields.Many2one(comodel_name="appointment.reason", string="Reason")
    operation_id = fields.Many2one(comodel_name="patient.operation", string="Operation")
    comment = fields.Text(string="Comment")
    progress = fields.Selection(selection=PROGRESS_INFO, string="Progress")
    attachment_ids = fields.Many2many(comodel_name="ir.attachment", string="Attachment")

    @api.model
    def create(self, vals):
        pass
