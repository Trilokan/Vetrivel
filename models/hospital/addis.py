# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import datetime

PROGRESS_INFO = [("draft", "Draft"), ("admitted", "Admitted"), ("discharged", "Discharged")]
ADMISSION_TYPE = [("normal", "Normal"), ("emergency", "Emergency")]
CURRENT_DATE = datetime.now().strftime("%Y-%m-%d")
CURRENT_TIME = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
CURRENT_INDIA = datetime.now().strftime("%d-%m-%Y %H:%M:%S")


# Admission Discharge
class Addis(models.Model):
    _name = "patient.addis"

    image = fields.Binary(string="Image")
    name = fields.Char(string="Name", readonly=True)
    patient_id = fields.Many2one(comodel_name="arc.patient", string="Patient")
    treatment_id = fields.Many2one(comodel_name="arc.treatment", string="Treatment")
    bed_id = fields.Many2one(comodel_name="arc.bed", string="Bed")
    progress = fields.Selection(selection=PROGRESS_INFO, default="draft")
    writter = fields.Text(string="Writter", track_visibility="always")

    # Contact
    contact_person = fields.Char(string="Contact Person")
    contact_mobile = fields.Char(string="Mobile")
    contact_phone = fields.Char(string="Phone")
    contact_address = fields.Text(string="Address")
    landmark = fields.Char(string="Landmark")

    # Admission
    admission_date = fields.Date(string="Date", default=CURRENT_DATE, required=True)
    admission_type = fields.Selection(selection=ADMISSION_TYPE, default="normal")
    admission_reason = fields.Many2one(comodel_name="admission.discharge.reason", string="Reason")
    admission_reason_detail = fields.Text(string="Reason")
    admission_comment = fields.Text(string="Comment")
    admission_attachment_ids = fields.Many2many(comodel_name="ir.attachment", string="Attachment")
    admitted_by = fields.Many2one(comodel_name="arc.person", string="Admitted By")

    # Discharge
    discharge_date = fields.Date(string="Date", required=True)
    discharge_reason = fields.Many2one(comodel_name="addis.reason", string="Reason")
    discharge_reason_detail = fields.Text(string="Reason")
    discharge_comment = fields.Text(string="Comment")
    discharge_attachment_ids = fields.Many2many(comodel_name="ir.attachment", string="Attachment")
    discharge_by = fields.Many2one(comodel_name="arc.person", string="Admitted By")

    is_account_approved = fields.Boolean(string="Account Approved")
    is_doctor_approved = fields.Boolean(string="Doctor Approved")

    def patient_shifting_admission(self):
        data = {"date": self.admission_date,
                "person_id": 0,
                "shift_type": "admission",
                "progress": "shifted"}

        self.env["patient.shifting"].create(data)

    def patient_shifting_discharge(self):
        pass

    def generate_treatment(self):
        data = {"date"}
        treatment_id = self.env["arc.treatment"].create(data)

        return treatment_id

    @api.multi
    def trigger_admit(self):
        treatment_id = self.generate_treatment()
        self.patient_shifting_admission()
        self.write({"progress": "admitted",
                    "treatment_id": treatment_id.id,
                    "admitted_by": self.env.user.person_id.id})

    @api.multi
    def trigger_discharge(self):
        self.patient_shifting_discharge()
        self.write({"progress": "discharged", "discharge_by": self.env.user.person_id.id})

    @api.model
    def create(self, vals):
        vals["name"] = self.env["ir.sequence"].next_by_code(self._name)
        vals["writter"] = "Admission created by {0} on {1}".format(self.env.user.name, CURRENT_TIME_INDIA)
        return super(Addis, self).create(vals)
