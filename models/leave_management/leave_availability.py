# -*- coding: utf-8 -*-

from odoo import models, fields, api, exceptions
from datetime import datetime

PROGRESS_INFO = [("draft", "Draft"), ("posted", "Posted")]
CURRENT_DATE = datetime.now().strftime("%Y-%m-%d")
CURRENT_TIME = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
CURRENT_INDIA = datetime.now().strftime("%d-%m-%Y %H:%M:%S")


class LeaveAvailability(models.TransientModel):
    _name = "leave.availability"

    person_id = fields.Many2one(comodel_name="arc.person", string="Employee")
    leave_detail = fields.One2many(comodel_name="leave.availability.detail", inverse_name="available_id")

    @api.onchange("person_id")
    def onchange_person_id(self):
        if self.person_id.id:
            employee_id = self.env["hr.employee"].search([("person_id", "=", self.person_id.id)])
            pass


class LeaveAvailabilityDetail(models.TransientModel):
    _name = "leave.availability.detail"

    available_id = fields.Many2one(comodel_name="leave.availability", string="Leave Type")
    type_id = fields.Many2one(comodel_name="leave.type", string="Leave Type")
    available = fields.Float(string="Available")
