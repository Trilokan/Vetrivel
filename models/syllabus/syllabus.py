# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Syllabus(models.Model):
    _name = "arc.syllabus"

    academic_id = fields.Many2one(comodel_name="arc.academic", string="Academic")
    standard_id = fields.Many2one(comodel_name="arc.standard", string="Standard")
    section_id = fields.Many2one(comodel_name="arc.section", string="Section")
    subject_id = fields.Many2one(comodel_name="school.subject", string="Subject")
    chapter_ids = fields.One2many(comodel_name="syllabus.detail", inverse_name="syllabus_id")


class SyllabusDetail(models.Model):
    _name = "syllabus.detail"

    index = fields.Char(string="Index", required=True)
    name = fields.Char(string="Name", required=True)
    parent_id = fields.Many2one(comodel_name="syllabus.detail", string="Parent ID")
    child_ids = fields.One2many(comodel_name="syllabus.detail", inverse_name="parent_id")
    description = fields.Text(string="Description")
    comment = fields.Text(string="Comment")
    syllabus_id = fields.Many2one(comodel_name="arc.syllabus", string="Syllabus")
