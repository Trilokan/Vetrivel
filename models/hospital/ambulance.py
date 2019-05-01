# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import datetime

PROGRESS_INFO = [("draft", "Draft"), ("confirmed", "Confirmed"), ("Done", "Done")]
PAYMENT_INFO = [("draft", "Draft"), ("paid", "Paid")]
CURRENT_DATE = datetime.now().strftime("%Y-%m-%d")
CURRENT_TIME = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
CURRENT_INDIA = datetime.now().strftime("%d-%m-%Y %H:%M:%S")


# Ambulance
class Ambulance(models.Model):
    _name = "arc.ambulance"
    _inherit = "mail.thread"

    date = fields.Date(string="Date", required=True)
    name = fields.Char(string="Name", readonly=True)
    patient_id = fields.Many2one(comodel_name="hos.person", string="Patient")
    driver_id = fields.Many2one(comodel_name="hos.person", string="Driver")
    progress = fields.Selection(selection=PROGRESS_INFO, default="draft")
    payment = fields.Selection(selection=PAYMENT_INFO, default="draft")
    writter = fields.Text(string="Writter", track_visibility="always")

    # Contact
    contact_person = fields.Char(string="Contact Person")
    contact_mobile = fields.Char(string="Mobile")
    contact_phone = fields.Char(string="Phone")
    contact_address = fields.Text(string="Address")
    landmark = fields.Char(string="Landmark")

    # Travelling
    travel_distance = fields.Float(string="Travel Distance")
    amount_per_km = fields.Float(string="Amount (KM)")
    total_amount = fields.Float(string="Total Amount")

    is_diver_intimated = fields.Boolean(string="Is Driver Intimated")

    @api.multi
    def trigger_intimate_driver(self):
        pass

    @api.multi
    def trigger_confirm(self):
        writter = "Ambulance service confirmed by {0} on {1}".format(self.env.user.name, CURRENT_INDIA)
        self.write({"progress": "done", "writter": writter})

    @api.multi
    def trigger_done(self):
        writter = "Ambulance service done by {0} on {1}".format(self.env.user.name, CURRENT_INDIA)
        self.write({"progress": "done", "writter": writter})

    @api.multi
    def trigger_pay(self):
        writter = "Ambulance service payment by {0} on {1}".format(self.env.user.name, CURRENT_INDIA)
        self.write({"payment": "paid", "writter": writter})

    @api.model
    def create(self, vals):
        vals["name"] = self.env["ir.sequence"].next_by_code(self._name)
        vals["writter"] = "Ambulance Service created by {0} on {1}".format(self.env.user.name, CURRENT_TIME_INDIA)
        return super(Ambulance, self).create(vals)
