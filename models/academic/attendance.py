# -*- coding: utf-8 -*-

from odoo import models, fields, api

PROGRESS_INFO = [("draft", "Draft"), ("register", "Register")]


class StudentAttendance(models.Model):
    _name = "student.attendance"

    date = fields.Date(string="Date", required=True)
    section_id = fields.Many2one(comodel_name="arc.section", string="Section")
    attendance_details = fields.One2many(comodel_name="student.attendance.detail", inverse_name="attendance_id")
    progress = fields.Selection(selection=PROGRESS_INFO, string="Progress", default="draft")

    # Gender
    total_male = fields.Integer(string="")
    total_female = fields.Integer(string="")

    # Present
    total_present = fields.Integer(string="")
    total_male_present = fields.Integer(string="")
    total_female_present = fields.Integer(string="")

    # Absent
    total_absent = fields.Integer(string="Total Absent")
    total_male_absent = fields.Integer(string="")
    total_female_absent = fields.Integer(string="")

    @api.multi
    def trigger_register(self):
        self.write({"progress": "register"})

    @api.multi
    def trigger_attendance_detail(self):
        recs = self.section_id.student_ids

        detail = []
        for rec in recs:
            detail.append({"student_id": 0,
                           "attendance_id": self.id})

        self.env["student.attendance.detail"].create(detail)


class StudentAttendanceDetails(models.Model):
    _name = "student.attendance.detail"

    student_id = fields.Many2one(comodel_name="arc.student", string="Student")
    attendance = fields.Boolean(string="Present/Absent")
    attendance_id = fields.Many2one(comodel_name="attendance.register", string="Attendance")
    progress = fields.Selection(selection=PROGRESS_INFO, related="attendance_id.progress")
