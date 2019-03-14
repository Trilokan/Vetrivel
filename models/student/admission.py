# -*- coding: utf-8 -*-

from odoo import models, fields, api, exceptions
from datetime import datetime

PROGRESS_INFO = [("draft", "Draft"), ("confirmed", "Confirmed"), ("admitted", "Admitted")]
CURRENT_DATE = datetime.now().strftime("%Y-%m-%d")
CURRENT_TIME = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
CURRENT_TIME_INDIA = datetime.now().strftime("%d-%m-%Y %H:%M:%S")


# Admission
class SchoolAdmission(models.Model):
    _name = "school.admission"
    _inherit = "mail.thread"

    date = fields.Date(string="Date", default=CURRENT_DATE, required=True)
    name = fields.Char(string="Name", readonly=True)
    student_id = fields.Many2one(comodel_name="school.student", string="Student", required=True)
    image = fields.Binary(string="Image")
    academic_id = fields.Many2one(comodel_name="arc.academic", string="Academic", required=True)
    standard_id = fields.Many2one(comodel_name="arc.standard", string="Standard", required=True)
    fee_structure_id = fields.Many2one(comodel_name="fee.structure", string="Fee Structure", required=True)
    bill_id = fields.Many2one(comodel_name="arc.invoice", string="Bill", readonly=True)
    total_amount = fields.Float(string="Total Amount", default=0.0, required=True)
    progress = fields.Selection(selection=PROGRESS_INFO, default="draft")
    writter = fields.Text(string="Writter", track_visiblity="always")
    attachment_ids = fields.Many2many(comodel_name="ir.attachment", string="Attachment")

    def generate_bill(self):
        pass

    def generate_arc_student(self):
        pass

    @api.multi
    def trigger_confirm(self):
        self.generate_bill()
        writter = "Admission for {0} confirmed by {1} on {2}".format(self.student_id.name,
                                                                     self.env.user.name,
                                                                     CURRENT_TIME_INDIA)
        self.write({"progress": "confirmed", "writter": writter})

    @api.multi
    def trigger_admit(self):
        self.generate_arc_student()
        writter = "{0} Admitted by {0} on {1}".format(self.student_id.name,
                                                      self.env.user.name,
                                                      CURRENT_TIME_INDIA)
        self.write({"progress": "admitted", "writter": writter})
