# -*- coding: utf-8 -*-

from odoo import models, fields


class TimeTable(models.Model):
    _name = "time.table"

    mon_p1 = fields.Many2one(comodel_name="")
    tue_p1 = fields.Many2one(comodel_name="")
    wed_p1 = fields.Many2one(comodel_name="")
    thu_p1 = fields.Many2one(comodel_name="")
    fri_p1 = fields.Many2one(comodel_name="")
    sat_p1 = fields.Many2one(comodel_name="")
    sun_p1 = fields.Many2one(comodel_name="")

    mon_p2 = fields.Many2one(comodel_name="")
    tue_p2 = fields.Many2one(comodel_name="")
    wed_p2 = fields.Many2one(comodel_name="")
    thu_p2 = fields.Many2one(comodel_name="")
    fri_p2 = fields.Many2one(comodel_name="")
    sat_p2 = fields.Many2one(comodel_name="")
    sun_p2 = fields.Many2one(comodel_name="")

    mon_p1 = fields.Many2one(comodel_name="")
    tue_p1 = fields.Many2one(comodel_name="")
    wed_p1 = fields.Many2one(comodel_name="")
    thu_p1 = fields.Many2one(comodel_name="")
    fri_p1 = fields.Many2one(comodel_name="")
    sat_p1 = fields.Many2one(comodel_name="")
    sun_p1 = fields.Many2one(comodel_name="")
