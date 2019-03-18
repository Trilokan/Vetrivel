# -*- coding: utf-8 -*-

from odoo import models, fields
from datetime import datetime

CURRENT_DATE = datetime.now().strftime("%Y-%m-%d")
CURRENT_TIME = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
CURRENT_INDIA = datetime.now().strftime("%d-%m-%Y %H:%M:%S")


# Bed Status
class BedStatus(models.TransientModel):
    _name = "bed.status"

    wards_count = fields.Integer(string="Total Wards")
    beds_count = fields.Integer(string="Total Bed")
    occupied_count = fields.Integer(string="Occupied")
    vacant_count = fields.Integer(string="Vacant")
    icu_ward_id = fields.One2many(comodel_name="icu.ward", inverse_name="status_id")
    ccu_ward_id = fields.One2many(comodel_name="ccu.ward", inverse_name="status_id")
    general_ward_id = fields.One2many(comodel_name="general.ward", inverse_name="status_id")


# ICU Ward
class ICUWard(models.TransientModel):
    _name = "icu.ward"

    bed_id = fields.Many2one(comodel_name="arc.bed")
    patient_id = fields.Many2one(comodel_name="arc.person")
    image = fields.Binary(string="Image")
    occupied_from = fields.Date(string="Occupied From")
    is_occupied = fields.Boolean(string="Is Occupied")
    status_id = fields.Many2one(comodel_name="bed.status")


# ICU Ward
class CCUWard(models.TransientModel):
    _name = "ccu.ward"

    bed_id = fields.Many2one(comodel_name="arc.bed")
    patient_id = fields.Many2one(comodel_name="arc.person")
    occupied_from = fields.Date(string="Occupied From")
    is_occupied = fields.Boolean(string="Is Occupied")
    status_id = fields.Many2one(comodel_name="bed.status")


# General Ward
class GeneralWard(models.TransientModel):
    _name = "general.ward"

    bed_id = fields.Many2one(comodel_name="arc.bed")
    patient_id = fields.Many2one(comodel_name="arc.person")
    occupied_from = fields.Date(string="Occupied From")
    is_occupied = fields.Boolean(string="Is Occupied")
    status_id = fields.Many2one(comodel_name="bed.status")
