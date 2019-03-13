# -*- coding: utf-8 -*-

from odoo import models, fields


class Test(models.Model):
    _name = "arc.test"

    name = fields.Char(string="Name")
    date = fields.Date(string="Date")
    subject_id = fields.Many2one(comodel_name="school.subject", string="Subject")
    academic_id = fields.Many2one(comodel_name="arc.academic", string="Academic")
    teacher_id = fields.Many2one(comodel_name="arc.person", string="Teacher")
    syllabus_ids = fields.Many2many(comodel_name="arc.syllabus", string="Syllabus")
    evaluation_ids = ""
    comment = ""
    progress = ""

