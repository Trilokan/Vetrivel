# -*- coding: utf-8 -*-

from odoo import models, fields, api

PROGRESS_INFO = [("draft", "Draft"),
                 ("confirmed", "Confirmed"),
                 ("done", "Done"),
                 ("cancel", "Cancel")]


class ArcTest(models.Model):
    _name = "arc.test"

    date = fields.Date(string="Date", default="", required=True)
    name = fields.Char(string="Name", readonly=True)
    academic_id = fields.Many2one(comodel_name="arc.academic", string="Academic")
    standard_id = fields.Many2one(comodel_name="arc.standard", string="Standard")
    section_id = fields.Many2one(comodel_name="arc.section", string="Section", required=True)
    subject_id = fields.Many2one(comodel_name="arc.subject", string="Subject", required=True)
    syllabus_id = fields.Many2one(comodel_name="arc.syllabus", string="Syllabus", required=True)
    teacher_id = fields.Many2one(comodel_name="arc.person", string="Teacher", required=True)
    total_marks = fields.Float(string="Total Marks", default=0.0, required=True)
    test_detail = fields.One2many(comodel_name="arc.test.detail", inverse_name="test_id")
    progress = fields.Selection(selection=PROGRESS_INFO, default="draft")

    @api.multi
    def add_test_detail(self):
        pass

    @api.multi
    def trigger_done(self):
        self.write({"progress": "done"})

    @api.model
    def create(self, vals):
        vals["name"] = 0
        section_id = self.env["arc.section"].search([("id", "=", vals["section_id"])])

        vals["academic_id"] = section_id
        vals["standard_id"] = section_id
        vals["academic_id"] = section_id
        vals["academic_id"] = section_id
        return super(ArcTest, self).create(vals)


class ArcTestDetail(models.Model):
    _name = "arc.test.detail"

    student_id = fields.Many2one(comodel_name="arc.student", string="Student")
    marks = fields.Float(string="Total Marks")
    test_id = fields.Many2one(comodel_name="arc.test", string="Test")
    progress = fields.Selection(selection=PROGRESS_INFO, related="test_id.progress")
