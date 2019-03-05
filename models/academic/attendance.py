# -*- coding: utf-8 -*-

from odoo import models, fields

PROGRESS_INFO = [("draft", "Draft"), ("register", "Register")]


class AttendanceRegister(models.Model):
    _name = "attendance.register"

    date = fields.Date(string="Date", required=True)
    section_id = fields.Many2one(comodel_name="", string="")
    attendance_details = ""
    progress = ""

    # Gender
    total_male = ""
    total_female = ""

    # Present
    total_present = ""
    total_male_present = ""
    total_female_present = ""

    # Absent
    total_absent = ""
    total_male_absent = ""
    total_female_absent = ""


class AttendanceDetails(models.Model):
    _name = ""

    student_id = ""
    present = ""
    attendance_id = ""
    